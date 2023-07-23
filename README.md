
<p align="center">
  <br>
  <a href="https://ergin.dev"><img src="https://raw.githubusercontent.com/EyupErgin/DroidDetective/main/.img/DroidDetective.png" width="600px" alt="HuntRthys"></a>
</p>
<h4 align="center">Modern Extended Static Analysis Tool for Analyzing Android APK Files<br> Version: v1.0 </h4>

---

## :globe_with_meridians:	About DroidDetective
DroidDetective is an extended static analysis tool designed to analyze Android APK files. It provides valuable information about APK files, such as file details, hashes, APK information, version details, and extended information like permissions, activities, services, and receivers.

## :notebook:	Features
DroidDetective offers you the following features.

### Basic Informations:
- File Name,
- File Type,
- File Size.

### Hash Informations:
- MD5,
- SHA-1,
- SHA-256.

### APK Informations:
- Application Name,
- Package Name.

### APK Version Informations:
- Internal Version,
- Displayed Version,
- Target SDK Version,
- Minimum SDK Version,
- Maximum SDK Version.

### APK Activity Informations:
- Permissions,
- Activities,
- Services,
- Receivers.

## :inbox_tray:	Install DroidDetective
1. Clone the project repository or download the zip file:
```bash
git clone https://github.com/eyupergin/droiddetective.git
```
2. Install the required Python packages by running the following command:
```bash
pip3 install -r requirements.txt
```

## :desktop_computer:	Use DroidDetective
### Basic Usage
- List arguments:
```
python3 main.py -h
```
- To scan a single APK file:
```
python3 main.py <APK_FILE_PATH> -a
```

### Arguments and Advanced Usage
```
"-a" or "--all": Analyze the APK file with all available options.
"-fs" or "--filesize": Display the file size of the APK.
"-fn" or "--filename": Display the file name of the APK.
"-ft" or "--filetype": Display the file type of the APK.
"-md5" or "--md5hash": Display the MD5 hash of the APK.
"-sha1" or "--sha1hash": Display the SHA-1 hash of the APK.
"-sha256" or "--sha256hash": Display the SHA-256 hash of the APK.
"-an" or "--appname": Display the Application Name in the output.
"-pn" or "--packname": Display the Package Name in the output.
"-iv" or "--intversion": Display the Internal Version in the output.
"-dv" or "--disversion": Display the Displayed Version in the output.
"-tsdk" or "--targetsdk": Display the Target SDK Version in the output.
"-misdk" or "--minsdk": Display the Minimum SDK Version in the output.
"-masdk" or "--maxsdk": Display the Maximum SDK Version in the output.
"-perm" or "--permissions": Display Permissions in the output.
"-acts" or "--activities": Display Activities in the output.
"-serv" or "--services": Display Services in the output.
"-recs" or "--receivers": Display Receivers in the output.
"-json" or "--json": Save the analysis results as a JSON file.
```

### Usage Format:
```
python3 main.py <APK_FILE_PATH> -[argument]
```

## :mag_right: Results
DroidDetective APK Analyzer tool visualizes the scanning results in a tabular format and prints them to the console. 
Additionally, you can choose to save the results to a JSON file.

```

 ______            _     _ ______                                _
(______)          (_)   | (______)         _                 _  (_)               |  Version: v1.0
 _     _ ____ ___  _  __| |_     _ _____ _| |_ _____  ____ _| |_ _ _   _ _____    |  Developed by Eyup Sukru ERGIN
| |   | / ___) _ \| |/ _  | |   | | ___ (_   _) ___ |/ ___|_   _) | | | | ___ |   |  --------------------------------------
| |__/ / |  | |_| | ( (_| | |__/ /| ____| | |_| ____( (___  | |_| |\ V /| ____|   |  https://ergin.dev
|_____/|_|   \___/|_|\____|_____/ |_____)  \__)_____)\____)  \__)_| \_/ |_____)   |  https://github.com/eyupergin/droiddetective

Extended Static Analysis Tool for Analyzing Android APK Files.

[+] Basic Info:
    - File Size: 155792351
    - File Name: example.apk
    - File Type: APK

[+] Hash Info:
    - MD5: 5ed55262e1d560253b1a763627214e76
    - SHA-1: 91dfae9c4c37208e0b600b397d3f78ffa35f0326
    - SHA-256: 811cc0ba2f625b5d41eaa6f59714fb55f34ca3833975204b3ffeca77e262415a

[+] APK Info:
    - Application Name: Example
    - Package Name: com.example.rome

[+] APK Version:
    - Internal Version: 1972
    - Displayed Version: 8.33.0
    - Target SDK Version: 33
    - Minimum SDK Version: 24
    - Maximum SDK Version: None

[+] Extended APK Info:
    - Permissions:
       android.permission.ACCESS_COARSE_LOCATION
       android.permission.ACCESS_FINE_LOCATION
       android.permission.ACCESS_NETWORK_STATE
       ...


    - Activities:
       com.appboy.ui.AppboyWebViewActivity
       com.appboy.ui.activities.AppboyContentCardsActivity
       ...


    - Services:
       androidx.room.MultiInstanceInvalidationService
       androidx.work.impl.background.systemalarm.SystemAlarmService
       androidx.work.impl.background.systemjob.SystemJobService
       ...


    - Receivers:
       androidx.work.impl.background.systemalarm.ConstraintProxy$BatteryChargingProxy
       androidx.work.impl.background.systemalarm.ConstraintProxy$BatteryNotLowProxy
       androidx.work.impl.background.systemalarm.ConstraintProxy$NetworkStateProxy
       ...

[+] [INFO] APK Analyze Finished.
```
```json
{
    "basicInfo": {
        "fileName": "example.apk",
        "fileSize": 155792351,
        "fileType": "APK"
    },
    "hashInfo": {
        "MD5": "5ed55262e1d560253b1a763627214e76",
        "SHA1": "91dfae9c4c37208e0b600b397d3f78ffa35f0326",
        "SHA256": "811cc0ba2f625b5d41eaa6f59714fb55f34ca3833975204b3ffeca77e262415a"
    }
}
```

---

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

### Contributing
Repo Update Date: 23-07-2023 <br>
> If you would like to contribute to this project, please open an issue or submit a pull request. Any contributions and suggestions are welcome!

### Contact
If you have any questions or suggestions, please feel free to contact me.<br>
E-mail: ergindev@gmail.com <br>
Website: www.ergin.dev <br>
LinkedIn: www.linkedin.com/in/eyupergin<br>
