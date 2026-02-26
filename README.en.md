<div align="center">

<h1>GoogleTranslate_IPFinder</h1>

<a href="https://github.com/GoodCoder666/GoogleTranslate_IPFinder/releases"><img alt="GitHub release" src="https://img.shields.io/github/release/GoodCoder666/GoogleTranslate_IPFinder.svg" /></a>
<a href="https://github.com/GoodCoder666/GoogleTranslate_IPFinder/releases"><img alt="GitHub Release Date" src="https://img.shields.io/github/release-date/GoodCoder666/GoogleTranslate_IPFinder.svg" /></a>
<a href="https://github.com/GoodCoder666/GoogleTranslate_IPFinder/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/github/license/GoodCoder666/GoogleTranslate_IPFinder.svg" /></a>
<a href="https://github.com/GoodCoder666/GoogleTranslate_IPFinder/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/GoodCoder666/GoogleTranslate_IPFinder.svg?style=social" /></a>

<a href="./README.md">简体中文</a> | English

</div>

## About the Project

An IP address scanner and speed testing tool for the Google Translate API server (`translate.googleapis.com`) in mainland China.

<details>
    <summary>Project Background</summary>
    Google stopped translation services on GWS servers in mainland China in September 2022. This project aims to help users find usable GWS IPs for translation and override local DNS resolution results to regain access to Google Translate servers.
</details>

<details>
    <summary>Disclaimer</summary>
    When using this open-source software, please comply with local laws and regulations, as well as relevant Google policies. <strong>You are solely responsible for any consequences arising from illegal or non-compliant use.</strong>
</details>

Stable release download link:

- [https://github.com/GoodCoder666/GoogleTranslate_IPFinder/releases](https://github.com/GoodCoder666/GoogleTranslate_IPFinder/releases)

Preview release (alpha) download links:

- Windows: [https://github.com/GoodCoder666/GoogleTranslate_IPFinder/releases/download/alpha/checker-win-x64.exe](https://github.com/GoodCoder666/GoogleTranslate_IPFinder/releases/download/alpha/checker-win-x64.exe)
- Mac OS: [https://github.com/GoodCoder666/GoogleTranslate_IPFinder/releases/download/alpha/checker-mac.zip](https://github.com/GoodCoder666/GoogleTranslate_IPFinder/releases/download/alpha/checker-mac.zip)

<details>
    <summary>About the English translations</summary>
    We <a href="https://github.com/GoodCoder666/GoogleTranslate_IPFinder/issues/38">noticed</a> that the tool might also be helpful in other countries/regions, thus English translations are added on 21 Sep, 2024. This document is mostly translated with <strong>Gemini 3.1 Pro</strong> and the UI is translated all by myself. Feel free to open an issue if something is wrong.
</details>

> [!NOTE]
>
> **This project has only been tested on Windows 11.** If the program does not work properly on other operating systems, please [open an issue](https://github.com/GoodCoder666/GoogleTranslate_IPFinder/issues/new).
>
> *Due to Python limitations, this project does not support Windows 7 and below.*

## Quick Start

Standard usage steps (Speed test + Write to Hosts):

1. Download the executable file for your respective system (links above).
2. Open with administrator/sudo privileges. **This is required to use the Write to Hosts feature.**
3. Select "Speedtest" and wait for the operation to complete.
4. Click "Write to Hosts", and the Google Translate API will function normally.

> [!TIP]
>
> Difference between "Speed Test" and "Scan":
>
> - **Speed Test**: Finds available IPs from the IPs to be tested (i.e., the IP library) and sorts them by response time. After this operation is complete, you can write the results to your Hosts file.
> - **Scan**: Finds available IPs from GWS IP ranges and puts them into the IP library. *Because the GWS network is extremely large, scanning even a small preset portion usually takes a long time.*
>
> Generally, after starting the program, you can directly select "Speed Test" (using the default IP library) and then write to Hosts to restore the Google Translate web service.

Windows 11 system demonstration:

![](screenshots/1.gif)

> [!WARNING]
>
> **The stability of IPv6 addresses is generally poor; try to avoid using them unless absolutely necessary.**
>
> Considering IP stability issues, under default settings, all IPs must pass at least 3 tests before being displayed in the speed test results. If you want to verify the stability of a single IP, please use the "Debug" feature.
>
> If you must use IPv6, it is recommended to adjust the test count to the maximum value of 10 under "Settings > Speedtest".
>
> For discussions regarding IP availability issues, please refer to [#42](https://github.com/GoodCoder666/GoogleTranslate_IPFinder/issues/42).

## Running from Source Code

Running from source code is applicable to all operating systems that support graphical interfaces. It requires Python >= 3.10 (3.12 and above is recommended).

For Linux systems:

```bash
$ git clone https://github.com/GoodCoder666/GoogleTranslate_IPFinder.git
$ cd GoogleTranslate_IPFinder
$ pip3 install PySide6 aiohttp
$ python3 run.py
```

For non-Linux systems:

```shell
git clone https://github.com/GoodCoder666/GoogleTranslate_IPFinder.git
cd GoogleTranslate_IPFinder
pip install -r requirements.txt
python run.py
```

## Development Roadmap

* [x] IP Speed Test
* [x] IP Scan
* [x] Automatically Write to Hosts
* [x] Automatically Fetch IP List
* [x] Speed Test/Scan Progress Bar
* [x] Custom Scan IP Ranges

... (If you have other feature requests, feel free to raise them in [issues](https://github.com/GoodCoder666/GoogleTranslate_IPFinder/issues))

## About the Online Sync Feature

The [Official IPv4 Address Library](https://github.com/GoodCoder666/gtdb) is built into the program and is updated periodically alongside feature updates. You can sync the latest IP library via `Import -> Online Services`. Additionally, two IP libraries from GoogleTranslateIpCheck are provided as options (Thanks to @Ponderfly). The URLs for the three libraries are as follows:

* Official IPv4: https://raw.githubusercontent.com/GoodCoder666/gtdb/main/src/ip.txt
* Extended IPv4: https://raw.githubusercontent.com/Ponderfly/GoogleTranslateIpCheck/master/src/GoogleTranslateIpCheck/GoogleTranslateIpCheck/ip.txt
* Extended IPv6: https://raw.githubusercontent.com/Ponderfly/GoogleTranslateIpCheck/master/src/GoogleTranslateIpCheck/GoogleTranslateIpCheck/IPv6.txt

There is also a newly included [Super Address Library](https://github.com/GoodCoder666/gtdb/tree/main/full), which is recommended to try when all the above IPs become invalid.

Additionally, if GitHub Raw cannot be connected, the program will attempt to use the [ghproxy](https://ghproxy.net/) mirror. Please be patient.

## License

This project is licensed under the [GPLv3](https://github.com/GoodCoder666/GoogleTranslate_IPFinder/blob/main/LICENSE) license. The IP scanning logic is inspired by [gscan_quic](https://codeberg.org/antigng/gscan_quic).

Similar projects: [hcfyapp/google-translate-cn-ip](https://github.com/hcfyapp/google-translate-cn-ip) | [Ponderfly/GoogleTranslateIpCheck](https://github.com/Ponderfly/GoogleTranslateIpCheck) | [csyezheng/ip-scanner](https://github.com/csyezheng/ip-scanner)
