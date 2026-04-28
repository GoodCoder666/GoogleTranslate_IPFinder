import difflib
import html

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QDialog, QDialogButtonBox, QLabel, QTextBrowser, QVBoxLayout

__all__ = ['dlgHostsDiff']

class dlgHostsDiff(QDialog):
    def __init__(self, parent, old_lines, new_lines):
        super().__init__(parent)
        self.setWindowTitle(self.tr('确认更新 Hosts 文件'))
        self.resize(700, 500)

        self.notice = QLabel(self.tr('即将修改系统 Hosts 文件，请仔细检查以下变更。'), self)
        self.notice.setWordWrap(True)

        self.browser = QTextBrowser(self)
        self.browser.setLineWrapMode(QTextBrowser.LineWrapMode.NoWrap)
        self.browser.setStyleSheet('font-family: Consolas, monospace; font-size: 13px; padding: 4px; background: #fff; color: #000;')

        self.bbox = QDialogButtonBox(self)
        self.confirm_btn = self.bbox.addButton(self.tr('确认修改'), QDialogButtonBox.AcceptRole)
        self.confirm_btn.setDefault(False)
        self.confirm_btn.setAutoDefault(False)
        self.cancel_btn = self.bbox.addButton(self.tr('取消'), QDialogButtonBox.RejectRole)
        self.cancel_btn.setDefault(True)
        self.cancel_btn.setAutoDefault(True)
        self.bbox.accepted.connect(self.accept)
        self.bbox.rejected.connect(self.reject)

        layout = QVBoxLayout(self)
        layout.addWidget(self.notice)
        layout.addWidget(self.browser)
        layout.addWidget(self.bbox)

        self._render_diff(old_lines, new_lines)

    def _render_diff(self, old_lines, new_lines):
        styles = {
            '-': 'color: #c24; background: #fee;',
            '+': 'color: #2a4; background: #efe;',
            ' ': 'color: #888;'
        }

        diff_idx = -1
        lines = []
        for line in difflib.ndiff(old_lines, new_lines):
            if line.startswith('?'):
                continue
            op, text = line[0], html.escape(line[2:])
            if diff_idx == -1 and op != ' ':
                diff_idx = len(lines)
            lines.append(f"<span style='{styles[op]}'>{op} {text}</span>")

        if diff_idx == -1:
            self.confirm_btn.setEnabled(False)
            self.notice.setText(self.tr('Hosts 无需任何修改。'))
        else:
            anchor_idx = diff_idx - 5
            if anchor_idx > 0:
                lines[anchor_idx] = f"<a name='diff'></a>{lines[anchor_idx]}"
                QTimer.singleShot(10, lambda: self.browser.scrollToAnchor('diff'))

        html_content = '\n'.join(lines)
        self.browser.setHtml(f"<pre style='margin: 0;'>{html_content}</pre>")
