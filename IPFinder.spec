from pathlib import Path
import sys

root = Path(SPECPATH)
icon = root / 'resources' / 'icons' / ('icon.icns' if sys.platform == 'darwin' else 'icon.ico')

excluded_modules = [
    # Unused stdlib features
    'tkinter', 'unittest', 'pydoc', 'pdb', 'doctest', 'curses',
    'xml', 'csv', 'ftplib', 'multiprocessing', 'statistics',
    'tarfile', 'py_compile', 'bz2', 'lzma', 'compression.zstd',
    'concurrent.futures.process', 'concurrent.futures.interpreter',
    'concurrent.interpreters',
    # Unused QtNetwork module
    'PySide6.QtNetwork',
    # Unused aiohttp modules
    'aiohttp.worker', 'aiohttp.web', 'aiohttp.web_app',
    'aiohttp.web_exceptions', 'aiohttp.web_fileresponse', 'aiohttp.web_log',
    'aiohttp.web_middlewares', 'aiohttp.web_protocol', 'aiohttp.web_request',
    'aiohttp.web_response', 'aiohttp.web_routedef', 'aiohttp.web_runner',
    'aiohttp.web_server', 'aiohttp.web_urldispatcher', 'aiohttp.web_ws',
    'aiohttp._websocket.reader_c', 'aiohttp._websocket.mask',
]

a = Analysis(
    [str(root / 'run.py')],
    pathex=[str(root)],
    hookspath=[str(root / '.github' / 'pyinstaller_hooks')],
    excludes=excluded_modules,
)

# Remove unused OpenGL driver
a.binaries = [entry for entry in a.binaries if Path(entry[0]).name.lower() != 'opengl32sw.dll']

# Remove unused bundled Qt translations
a.datas = [
    entry for entry in a.datas
    if not (entry[0].replace('\\', '/').startswith('PySide6/')
            and '/translations/' in entry[0].replace('\\', '/')
            and entry[0].endswith('.qm'))
]

pyz = PYZ(a.pure)
exe = EXE(
    pyz, a.scripts, a.binaries, a.datas, [],
    name='main',
    console=False,
    strip=False,
    upx=False,
    icon=str(icon),
)

if sys.platform == 'darwin':
    app = BUNDLE(exe, name='main.app', icon=str(icon), bundle_identifier=None)
