from qt_core import *

from gui.themes.themes import theme
from gui.widgets.py_icon import tinted_pixmap


class PyIconButton(QPushButton):
    # botão quadrado só com ícone (ex.: sino de notificações) com bolinha opcional
    def __init__(self, icon_path="", size=38, icon_size=20, parent=None):
        super().__init__(parent)
        self.icon_path = icon_path
        self.icon_size = icon_size
        self.has_badge = False
        self.setFixedSize(size, size)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        theme.theme_changed.connect(self.update)

    def set_badge(self, visible):
        self.has_badge = visible
        self.update()

    def paintEvent(self, event):
        colors = theme.colors
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # fundo no hover
        if self.underMouse():
            painter.setPen(Qt.PenStyle.NoPen)
            painter.setBrush(QColor(colors["bg"]))
            painter.drawRoundedRect(self.rect(), 10, 10)

        x = (self.width() - self.icon_size) / 2
        y = (self.height() - self.icon_size) / 2
        painter.drawPixmap(int(x), int(y), tinted_pixmap(self.icon_path, colors["muted"], self.icon_size))

        if self.has_badge:
            painter.setPen(QPen(QColor(colors["surface"]), 2))
            painter.setBrush(QColor(colors["accent"]))
            painter.drawEllipse(QPointF(x + self.icon_size - 3, y + 3), 4, 4)
        painter.end()

    def enterEvent(self, event):
        self.update()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.update()
        super().leaveEvent(event)
