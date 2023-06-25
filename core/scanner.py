import requests
import time
import urllib3
import warnings
from bs4 import BeautifulSoup
import argparse
import pandas as pd
from tabulate import tabulate
from colorama import Fore, Style
import sys
import threading

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
warnings.filterwarnings('ignore', message='Unverified HTTPS request')

def get_title(url):
    try:
        response = requests.get(url, verify=False, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.find("title")
        return title
    except requests.exceptions.RequestException:
        return None

def sanitize_url(url):
    if url.startswith("http://"):
        url = url[7:]
    elif url.startswith("https://"):
        url = url[8:]
    return url

def get_first_word(string):
    words = string.split()
    if words:
        return words[0]
    return ""

def scan_ip(ip):
    ip = ip.strip()
    try:
        url = f"http://{sanitize_url(ip)}:443/admin/console/index.html"
        time.sleep(1)
        title = get_title(url)

        if title is None or ("Rhadamanthys" not in title.text and "Admin" not in title.text):
            return None

        api_url = f"http://ip-api.com/json/{ip}"
        response = requests.get(api_url)
        data = response.json()

        if "countryCode" not in data or "as" not in data:
            return None

        as_info = get_first_word(data["as"])

        result = {
            "STATUS": f"{Fore.GREEN}[C2 DETECTED]{Style.RESET_ALL}",
            "IP ADDRESS": ip,
            "CN": data.get("countryCode", ""),
            "ASN": as_info,
            "PAGE TITLE": title.text,
            "FULL URL": url
        }

        return result
    except requests.exceptions.RequestException:
        return None
      
def scan_ip_with_thread(ip, lock, success_count):
    result = scan_ip(ip)
    if result is not None:
        lock.acquire()
        if ip not in success_count:
            success_count[ip] = 0
        success_count[ip] += 1 
        results.append(result)
        lock.release()

def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-t", "--target", help="Single IP address to scan")
    group.add_argument("-f", "--file", help="Text file containing IP addresses to scan")
    parser.add_argument("-oJ", "--output", help="Output JSON filename")
    parser.add_argument("-mT", "--multithread", type=int, metavar="N", help="Enable multithreading with N threads")
    args = parser.parse_args()

    if args.target:
        ip_list = [args.target]
    elif args.file:
        with open(args.file, "r") as f:
            ip_list = f.readlines()

    if not ip_list:
        print("[INFO] No IP addresses found in the input.")
        return

    table_data = []
    global results
    results = []
    success_count = {}
    lock = threading.Lock()

    def loading_animation():
        animation = ["[    ]", "[=   ]", "[==  ]", "[=== ]", "[ ===]", "[  ==]", "[   =]", "[    ]"]
        for frame in animation:
            time.sleep(0.2)
            print("" + frame, end="\r")

    def process_ips(ip_list):
        if "-mT" in sys.argv:
            for ip in ip_list:
                ip = ip.strip()
                if ip not in success_count:
                    success_count[ip] = 0  
                print(f"\tScanning IP address: {ip} | Detected Rhadamanthys C2: {success_count[ip]}", end="\r")
                loading_animation()
                scan_ip_with_thread(ip, lock, success_count)

            sys.stdout.write("\033[K")
            total_scanned = len(ip_list)
            detected_c2_count = sum(success_count.values())

        else:
            for ip in ip_list:
                ip = ip.strip()
                if ip not in success_count:
                    success_count[ip] = 0
                print(f"\tScanning IP address: {ip} | Detected Rhadamanthys C2: {success_count[ip]}", end="\r")
                loading_animation()
                scan_ip_with_thread(ip, lock, success_count)

            sys.stdout.write("\033[K")
            total_scanned = len(ip_list)
            detected_c2_count = sum(success_count.values())

            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")
            print(f"\n[INFO] Total Scanned IP Addresses: {total_scanned} | {Fore.GREEN}Detected C2: {detected_c2_count}{Style.RESET_ALL}", end="\n"+"\n")

    if args.multithread:
        thread_count = min(max(args.multithread, 1), 5)
        threads = []
        split_size = (len(ip_list) + thread_count - 1) // thread_count
        for i in range(thread_count):
            start = i * split_size
            end = (i + 1) * split_size
            thread = threading.Thread(target=process_ips, args=(ip_list[start:end],))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()
    else:
        process_ips(ip_list)

    for result in results:
        table_data.append([
            result.get("STATUS", ""),
            result.get("IP ADDRESS", ""),
            result.get("CN", ""),
            result.get("ASN", ""),
            result.get("PAGE TITLE", ""),
            result.get("FULL URL", "")
        ])

    headers = [
        "STATUS",
        "IP ADDRESS",
        "CN",
        "ASN",
        "PAGE TITLE",
        "FULL URL"
    ]

    df = pd.DataFrame(table_data, columns=headers)

    pd.set_option("display.max_colwidth", None)
    pd.set_option("display.width", None)
    pd.set_option("display.max_rows", None)
    pd.set_option("display.max_columns", None)

    if not df.empty:
        df = df.reset_index(drop=True)
        df.index += 1
        print(tabulate(df, headers, tablefmt="simple"))
    else:
        print("[INFO] No C2 servers detected.")

    if args.output:
        df.to_json(args.output, orient="records")
        print(f"[INFO] Results saved to {args.output}")

if __name__ == "__main__":
    main()
