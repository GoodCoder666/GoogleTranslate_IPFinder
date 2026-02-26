<div align="center">

<h1>GoogleTranslate_IPFinder</h1>

<a href="https://github.com/GoodCoder666/GoogleTranslate_IPFinder/releases"><img alt="GitHub release" src="https://img.shields.io/github/release/GoodCoder666/GoogleTranslate_IPFinder.svg" /></a>
<a href="https://github.com/GoodCoder666/GoogleTranslate_IPFinder/releases"><img alt="GitHub Release Date" src="https://img.shields.io/github/release-date/GoodCoder666/GoogleTranslate_IPFinder.svg" /></a>
<a href="https://github.com/GoodCoder666/GoogleTranslate_IPFinder/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/github/license/GoodCoder666/GoogleTranslate_IPFinder.svg" /></a>
<a href="https://github.com/GoodCoder666/GoogleTranslate_IPFinder/releases"><img alt="GitHub Release Downloads" src="https://img.shields.io/github/downloads/GoodCoder666/GoogleTranslate_IPFinder/total?color=teal" /></a>
<a href="https://github.com/GoodCoder666/GoogleTranslate_IPFinder/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/GoodCoder666/GoogleTranslate_IPFinder.svg?style=social" /></a>

简体中文 | <a href="./README.en.md">English</a>

</div>

## 项目简介

谷歌翻译 API 服务器（`translate.googleapis.com`）在中国大陆的 IP 地址扫描、测速工具。

<details>
    <summary>项目背景</summary>
    Google 于 2022 年 9 月停止了中国大陆 GWS 服务器的翻译服务。本项目旨在帮助用户找到能够使用翻译的 GWS IP 并覆盖本地域名解析结果来实现对谷歌翻译服务器的访问。
</details>

<details>
    <summary>免责声明</summary>
    使用此开源软件时，请您遵守当地法律法规以及 Google 的相关规定。<strong>一切违法/违规用途后果自负。</strong>
</details>

稳定版下载地址：

- [https://github.com/GoodCoder666/GoogleTranslate_IPFinder/releases](https://github.com/GoodCoder666/GoogleTranslate_IPFinder/releases)

预览版（alpha）下载地址：

- Windows: [https://github.com/GoodCoder666/GoogleTranslate_IPFinder/releases/download/alpha/checker-win-x64.exe](https://github.com/GoodCoder666/GoogleTranslate_IPFinder/releases/download/alpha/checker-win-x64.exe)
- Mac OS: [https://github.com/GoodCoder666/GoogleTranslate_IPFinder/releases/download/alpha/checker-mac.zip](https://github.com/GoodCoder666/GoogleTranslate_IPFinder/releases/download/alpha/checker-mac.zip)

> [!NOTE]
>
> **本项目仅在 Windows 11 下测试通过。** 若程序在其他操作系统下无法正常工作，请[提出 issue](https://github.com/GoodCoder666/GoogleTranslate_IPFinder/issues/new)。
>
> *由于 Python 的限制，本项目不支持 Windows 7 及以下。*

## 快速上手

无特殊需求的使用步骤（测速+写入Hosts）：

1. 下载对应系统的可执行文件（链接见上方）。
2. 使用管理员/sudo权限打开。**只有这样才能使用 Hosts 写入功能。**
3. 选择“测速”，等待操作完成。
4. 点击“写入Hosts”，谷歌翻译 API 即可正常使用。

> [!TIP]
>
> 区分“测速”和“扫描”：
>
> - **测速**：从待测速的 IP（即 IP 库）中找出可用 IP，并按照响应时间排序。此操作完成后可以写入 Hosts。
> - **扫描**：从 GWS 的 IP 段中找到可用的 IP，并置于 IP 库中。*由于 GWS 网络极为庞大，即使是扫描预设的一小部分通常也需要很长时间。*
>
> 一般来说，启动程序后直接选择“测速”（使用默认 IP 库）再写入 Hosts 即可恢复谷歌翻译网络服务。

Windows 11 系统演示如下：

![](screenshots/1.gif)

> [!WARNING]
>
> **IPv6 地址的稳定性普遍不好，不到万不得已尽量不要使用。**
>
> 考虑到 IP 稳定性的问题，在默认设置下，所有 IP 都必须至少通过 3 次测试才会显示在测速结果中。如果想验证单个 IP 的稳定性，请使用「调试」功能。
>
> 若必须使用 IPv6，建议在「设置 > 测速」中将测速次数调整至最大值 10。
>
> 关于 IP 可用性问题的讨论请移步 [#42](https://github.com/GoodCoder666/GoogleTranslate_IPFinder/issues/42)。

## 从源代码运行

从源代码运行的方法适用于所有支持图形界面的操作系统，只需 Python >= 3.10（推荐 3.12 及以上版本）。

对于 Linux 系统：

```bash
$ git clone https://github.com/GoodCoder666/GoogleTranslate_IPFinder.git
$ cd GoogleTranslate_IPFinder
$ pip3 install PySide6 aiohttp
$ python3 run.py
```

对于非 Linux 系统：

```shell
git clone https://github.com/GoodCoder666/GoogleTranslate_IPFinder.git
cd GoogleTranslate_IPFinder
pip install -r requirements.txt
python run.py
```

## 关于在线同步功能

[官方 IPv4 地址库](https://github.com/GoodCoder666/gtdb) 内置在程序中，不定期随功能更新。您可以通过 `导入->在线服务` 同步最新的 IP 库。同时提供 GoogleTranslateIpCheck 中的两个 IP 库供选择（感谢 @Ponderfly）。三个库的网址如下：

- 官方 IPv4：https://raw.githubusercontent.com/GoodCoder666/gtdb/main/src/ip.txt
- 扩展 IPv4：https://raw.githubusercontent.com/Ponderfly/GoogleTranslateIpCheck/master/src/GoogleTranslateIpCheck/GoogleTranslateIpCheck/ip.txt
- 扩展 IPv6：https://raw.githubusercontent.com/Ponderfly/GoogleTranslateIpCheck/master/src/GoogleTranslateIpCheck/GoogleTranslateIpCheck/IPv6.txt

另有新收录的[超级地址库](https://github.com/GoodCoder666/gtdb/tree/main/full)，建议在上面的所有 IP 全部失效时尝试。

同时，若 GitHub Raw 无法连接，程序将尝试使用 [ghproxy](https://ghproxy.net/) 镜像，请耐心等待。

## 版权说明

本项目使用 [GPLv3](https://github.com/GoodCoder666/GoogleTranslate_IPFinder/blob/main/LICENSE) 版权许可。IP 扫描逻辑参考 [gscan_quic](https://codeberg.org/antigng/gscan_quic)。

类似的项目：[hcfyapp/google-translate-cn-ip](https://github.com/hcfyapp/google-translate-cn-ip) [Ponderfly/GoogleTranslateIpCheck](https://github.com/Ponderfly/GoogleTranslateIpCheck) [csyezheng/ip-scanner](https://github.com/csyezheng/ip-scanner)

