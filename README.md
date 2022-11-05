# GoogleTranslate_IPFinder

谷歌翻译服务器`translate.googleapis.com`在中国大陆的IP地址扫描、测速工具。

项目使用Python编写，GUI使用的是PySide6（Qt for Python 6）。

## 快速上手

### 使用打包好的可执行文件（仅限Windows系统）

从[Releases](https://github.com/GoodCoder666/GoogleTranslate_IPFinder/releases)页面下载`checker.exe`，双击运行即可。

文件大小约为31 MB，由GitHub Actions自动打包发布，建议使用IDM/NDM等多线程下载器进行下载。

### 从源代码运行（适用于所有操作系统）

在命令行中依次执行如下命令（请提前安装好Python>=3.6和Git）：

```shell
git clone https://github.com/GoodCoder666/GoogleTranslate_IPFinder.git
pip install -r requirements.txt
python main.py
```

## 版权说明

本项目使用GPLv3版权许可。

类似的项目：[hcfyapp/google-translate-cn-ip](https://github.com/hcfyapp/google-translate-cn-ip) [Ponderfly/GoogleTranslateIpCheck](https://github.com/Ponderfly/GoogleTranslateIpCheck)