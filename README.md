
<p align="center">
  <br>
  <a href="https://ergin.dev"><img src="https://raw.githubusercontent.com/EyupErgin/HuntRthys/main/.img/banner-gray.png" width="400px" alt="HuntRthys"></a>
</p>
<h4 align="center">Modern and Fast Rhadamanhys Command and Control Server Detection Tool<br> Version: v1.3 </h4>

---

## :scorpion:	About HuntRthys
HuntRthys is a specific, modern and fast command and control detection tool written to detect Command and Control (C2) servers used by the Rhadamanthys Stealer Malware. HuntRthys provides the most reliable and fastest detection among 6 different methods determined as a result of studies on the characteristics and detectability of Rhadamanthys C2 servers.

### :spider: About Rhadamanthys Stealer Malware
Rhadamanthys Stealer Malware was first identified in September 2022 by a team of researchers at ThreatMon Threat Intelligence, including myself, on a Russian hacker forum. Since its announcement, this malware has continued to evolve. Every day, many new command and control servers are being purchased to serve the Rhadamanthys Stealer malware. Rhadamanthys has been distributed as Stealer Malware since its discovery and its characteristics have not changed. It has its own C2 Command and Control Management Panel. Don't forget to check my blog for more information about the Rhadamanthys malware and the residential control server.

## :notebook:	Features
HuntRthys offers you the following features.

- Specific and fast scanner,
- Single IP address scanner,
- Multi IP address scanner,
- Extended IP info,
- Extended URL info,
- Extended Web Page info,
- Modern tabular format,
- Wide range of results,
- Multithreading support.

## :inbox_tray:	Install HuntRthys
1. Clone the project repository or download the zip file:
```bash
git clone https://github.com/eyupergin/huntrthys.git
```
2. Install the required Python packages by running the following command:
```bash
pip3 install -r requirements.txt
```
## :desktop_computer:	Use HuntRthys
HuntRthys is used via a command-line interface. Below are examples of basic usage.

### Basic Usage
- List arguments:
```bash
python3 main.py -h
```
- To scan a single IP address:
```bash
python3 main.py -t <IP_ADDRESS>
```
- To scan IP addresses from a file:
```bash
python3 main.py -f <FILE_NAME.txt>
```

### Advanced Usage
- To perform scanning with multi-threading:
```bash
python3 huntrthys.py -f <FILE_NAME.txt> -mT <THREAD_COUNT>
```
Note: The **"-mT"** parameter allows up to **5** threads.

- To save the scanner results to a JSON file:
```bash
python huntrthys.py -t <IP_ADDRESS> -oJ <OUTPUT_FILE.json>
```
## :mag_right: Results
HuntRthys C2 Scanner tool visualizes the scanning results in a tabular format and prints them to the console. 
Additionally, you can choose to save the results to a JSON file.

Here is an example output of the results:
```
______  __             ________________________
___  / / ____  __________  /___  __ __  /___  /______  _________  |  Version: v1.3
__  /_/ /_  / / __  __ _  ____  /_/ _  ____  __ __  / / __  ___/  |  Developed by Eyup Sukru ERGIN
_  __  / / /_/ /_  / / / /_ _  _, _// /_ _  / / _  /_/ /_(__  )   |  --------------------------------------
/_/ /_/  \__,_/ /_/ /_/\__/ /_/ |_| \__/ /_/ /_/_\__, / /____/    |  https://ergin.dev
                                                /____/            |  https://github.com/eyupergin/huntrthys

Specific Rhadamanthys Command and Control Server Detection Tool

[INFO] Total Scanned IP Addresses: 3 | Detected C2: 3

    STATUS         IP ADDRESS      CN    ASN      PAGE TITLE          FULL URL
--  -------------  --------------  ----  -------  ------------------  --------------------------------------------------
 1  [C2 DETECTED]  192.138.111.11  CH    AS51852  Rhadamanthys Admin  http://192.138.111.11:443/admin/console/index.html
 2  [C2 DETECTED]  192.138.111.11  CH    AS51852  Rhadamanthys Admin  http://192.138.111.11:443/admin/console/index.html
 3  [C2 DETECTED]  192.138.111.11  CH    AS51852  Rhadamanthys Admin  http://192.138.111.11:443/admin/console/index.html
```

---

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

### Contributing
Repo Update Date: 17-08-2023 <br>
> If you would like to contribute to this project, please open an issue or submit a pull request. Any contributions and suggestions are welcome!

### Contact
If you have any questions or suggestions, please feel free to contact me.<br>
E-mail: ergindev@gmail.com <br>
Website: www.ergin.dev <br>
LinkedIn: www.linkedin.com/in/eyupergin<br>
