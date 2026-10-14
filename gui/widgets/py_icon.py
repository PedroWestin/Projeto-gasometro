import os
from functools import lru_cache

from PySide6.QtCore import QRectF
from PySide6.QtGui import QColor, QGuiApplication, QPainter, QPixmap
from PySide6.QtSvg import QSvgRenderer
from qt_core import *

from gui.themes.themes import theme

# pasta dos icones relativa a este arquivo (funciona de qualquer diretório)
ICONS_DIR = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "images", "icons"))


@lru_cache(maxsize=256)
def _render(icon_name, color, size, dpr):
    pixmap = QPixmap(int(size * dpr), int(size * dpr))
    pixmap.setDevicePixelRatio(dpr)
    pixmap.fill(Qt.GlobalColor.transparent)

    painter = QPainter(pixmap)
    painter.setRenderHint(QPainter.RenderHint.Antialiasing)
    QSvgRenderer(os.path.join(ICONS_DIR, icon_name)).render(painter, QRectF(0, 0, size, size))
    # pinta o icone com a cor desejada (mesma técnica do PyPushButton)
    painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceIn)
    painter.fillRect(pixmap.rect(), QColor(color))
    painter.end()
    return pixmap


def tinted_pixmap(icon_name, color, size=20):
    screen = QGuiApplication.primaryScreen()
    dpr = screen.devicePixelRatio() if screen else 1.0
    return _render(icon_name, color, size, dpr)


class PyIconLabel(QWidget):
    # icone SVG que acompanha a cor do tema ativo
    def __init__(self, icon_name="", size=18, color="muted", parent=None):
        super().__init__(parent)
        self.icon_name = icon_name
        self.icon_size = size
        self.color_key = color
        self.setFixedSize(size, size)
        theme.theme_changed.connect(self.update)

    def paintEvent(self, event):
        if not self.icon_name:
            return
        painter = QPainter(self)
        painter.drawPixmap(0, 0, tinted_pixmap(self.icon_name, theme.color(self.color_key), self.icon_size))
        painter.end()
