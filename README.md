# GoogleTranslate_IPFinder

谷歌翻译 API 服务器（`translate.googleapis.com`）在中国大陆的 IP 地址扫描、测速工具。

项目使用 Python 编写，GUI 使用的是 `PySide6`（Qt for Python 6）。

稳定版下载地址：

- [https://github.com/GoodCoder666/GoogleTranslate_IPFinder/releases](https://github.com/GoodCoder666/GoogleTranslate_IPFinder/releases)

预览版（alpha）下载地址：

- Windows: [https://github.com/GoodCoder666/GoogleTranslate_IPFinder/releases/download/alpha/checker-win-x64.exe](https://github.com/GoodCoder666/GoogleTranslate_IPFinder/releases/download/alpha/checker-win-x64.exe)
- Mac OS: [https://github.com/GoodCoder666/GoogleTranslate_IPFinder/releases/download/alpha/checker-mac.zip](https://github.com/GoodCoder666/GoogleTranslate_IPFinder/releases/download/alpha/checker-mac.zip)

关于 IP 可用性问题的讨论请移步 [Discussion #19](https://github.com/GoodCoder666/GoogleTranslate_IPFinder/discussions/19)。

## 快速上手

无特殊需求的使用步骤（测速+写入Hosts）：

1. 下载对应系统的可执行文件（链接见上方）。
2. 使用管理员/sudo权限打开。
3. 选择“测速”，等待操作完成。
4. 点击“写入Hosts”，谷歌翻译 API 即可正常使用。

Windows 11 系统演示如下：

![](screenshots/1.gif)

## 屏幕截图

![](screenshots/2.png)

## 注意事项

- 本项目仅在 Windows 11 下测试通过，其他操作系统若有运行问题请开 issue。
- 由于 Python 的限制，本项目不支持 Windows 7 及以下。
- 若要使用 Hosts 写入功能，请使用管理员权限（Windows）或 sudo（其他系统）打开。
- IPv6 地址的稳定性普遍不好，不到万不得已尽量不要使用。考虑到 IP 稳定性的问题，所有 IP 都必须至少通过 3 次测试才会显示在测速结果中。如果想验证单个 IP 的稳定性，请使用「调试」功能。

## 功能对比

|     功能     |       本项目       | [GoogleTranslateIpCheck](https://github.com/Ponderfly/GoogleTranslateIpCheck) | [google-translate-cn-ip](https://github.com/hcfyapp/google-translate-cn-ip) | [ip-scanner](https://github.com/csyezheng/ip-scanner) | [gscan_quic](https://codeberg.org/antigng/gscan_quic) |
| :----------: | :----------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :---------------------------------------------------: | :---------------------------------------------------: |
|   IP 收集    | :heavy_check_mark: |                      :heavy_check_mark:                      |                      :heavy_check_mark:                      |                  :heavy_check_mark:                   |                          :x:                          |
|   IP 扫描    | :heavy_check_mark: |                      :heavy_check_mark:                      |                             :x:                              |                  :heavy_check_mark:                   |                  :heavy_check_mark:                   |
|   IP 测速    | :heavy_check_mark: |                      :heavy_check_mark:                      |                      :heavy_check_mark:                      |                          :x:                          |                          :x:                          |
|  HOSTS 写入  | :heavy_check_mark: |                      :heavy_check_mark:                      |                             :x:                              |                          :x:                          |                          :x:                          |
| GUI 图形界面 | :heavy_check_mark: |                             :x:                              |                             :x:                              |                          :x:                          |                          :x:                          |

## 快速上手

### 使用打包好的可执行文件（仅限 Windows 和 Mac OS）

从[Releases](https://github.com/GoodCoder666/GoogleTranslate_IPFinder/releases/tag/alpha)页面下载对应系统的可执行文件，运行即可。

- Windows: [https://github.com/GoodCoder666/GoogleTranslate_IPFinder/releases/download/alpha/checker-win-x64.exe](https://github.com/GoodCoder666/GoogleTranslate_IPFinder/releases/download/alpha/checker-win-x64.exe)
- Mac OS: [https://github.com/GoodCoder666/GoogleTranslate_IPFinder/releases/download/alpha/checker-mac.zip](https://github.com/GoodCoder666/GoogleTranslate_IPFinder/releases/download/alpha/checker-mac.zip)

文件由GitHub Actions自动打包发布，如果下载慢可以用IDM/NDM等多线程下载器进行下载。

### 从源代码运行（适用于所有操作系统）

先决条件：

- Python >= 3.6
- Git

对于 Linux 系统：

```bash
$ git clone https://github.com/GoodCoder666/GoogleTranslate_IPFinder.git
$ cd GoogleTranslate_IPFinder
$ pip3 install PySide6
$ python3 main.py
```

对于非 Linux 系统：

```shell
git clone https://github.com/GoodCoder666/GoogleTranslate_IPFinder.git
cd GoogleTranslate_IPFinder
pip install -r requirements.txt
python main.py
```

## 开发计划

- [x] IP 测速
- [x] IP 扫描
- [x] 自动写入 Hosts
- [x] 自动获取 IP 列表
- [x] 测速/扫描进度条
- [ ] 自定义扫描 IP 段

...（若有其他需求欢迎在 [issues](https://github.com/GoodCoder666/GoogleTranslate_IPFinder/issues) 中提出）

## 关于在线同步功能

本项目作者提供的 IP 库在打开软件时会自动导入。程序还提供了在线导入其他 IP 库的功能，地址如下：

- 精简 IPv4：
  - 官方：https://unpkg.com/@hcfy/google-translate-ip/ips.txt
  - 备用1（ghproxy 镜像）：https://mirror.ghproxy.com/https://raw.githubusercontent.com/hcfyapp/google-translate-cn-ip/master/packages/google-translate-ip/ips.txt
  - 备用2（jsDelivr CDN）：https://cdn.jsdelivr.net/npm/@hcfy/google-translate-ip/ips.txt
- 扩展 IPv4：
  - 官方1：https://raw.githubusercontent.com/Ponderfly/GoogleTranslateIpCheck/master/src/GoogleTranslateIpCheck/GoogleTranslateIpCheck/ip.txt
  - 官方2：https://mirror.ghproxy.com/https://raw.githubusercontent.com/Ponderfly/GoogleTranslateIpCheck/master/src/GoogleTranslateIpCheck/GoogleTranslateIpCheck/ip.txt
- 标准 IPv6：
  - 官方1：https://raw.githubusercontent.com/Ponderfly/GoogleTranslateIpCheck/master/src/GoogleTranslateIpCheck/GoogleTranslateIpCheck/IPv6.txt
  - 官方2：https://mirror.ghproxy.com/https://raw.githubusercontent.com/Ponderfly/GoogleTranslateIpCheck/master/src/GoogleTranslateIpCheck/GoogleTranslateIpCheck/IPv6.txt

程序会自动选择可用的地址并导入 IP 库（设置备用网址是因为 raw.githubusercontent.com 访问不稳定）。导入一般需要 5-10 秒，请耐心等待。

感谢 @hcfyapp 和 @Ponderfly 提供的 IP 库。

## 版权说明

本项目使用 [GPLv3](https://github.com/GoodCoder666/GoogleTranslate_IPFinder/blob/main/LICENSE) 版权许可。IP 扫描逻辑参考 [https://codeberg.org/antigng/gscan_quic](https://codeberg.org/antigng/gscan_quic)。

类似的项目：[hcfyapp/google-translate-cn-ip](https://github.com/hcfyapp/google-translate-cn-ip) [Ponderfly/GoogleTranslateIpCheck](https://github.com/Ponderfly/GoogleTranslateIpCheck) [csyezheng/ip-scanner](https://github.com/csyezheng/ip-scanner)

