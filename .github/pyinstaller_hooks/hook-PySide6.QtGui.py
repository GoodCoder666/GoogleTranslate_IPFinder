"""Remove unused QtGui plugins."""
from pathlib import Path
import sys

from PyInstaller.utils.hooks.qt import add_qt6_dependencies

hiddenimports, binaries, datas = add_qt6_dependencies(__file__)

def keep_plugin(source):
    path = Path(source)
    plugin = path.stem.removeprefix('lib')
    category = path.parent.name

    if category == 'generic' and plugin == 'qtuiotouchplugin':
        return False

    if category == 'imageformats':
        return plugin == 'qico'

    if category == 'iconengines':
        return False

    if category == 'platforms':
        if sys.platform == 'win32':
            return plugin == 'qwindows'
        if sys.platform == 'darwin':
            return plugin == 'qcocoa'

    return True

binaries = [(source, destination) for source, destination in binaries if keep_plugin(source)]
