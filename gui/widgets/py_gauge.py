import math

from qt_core import *

from gui.themes.themes import theme


class PyGauge(QWidget):
    # medidor semicircular com ponteiro (nível do botijão em %)
    # sem dados: desenha apenas o trilho
    def __init__(self, parent=None):
        super().__init__(parent)
        self._value = None
        self._status = ""
        self._tone = "green"
        self.setMinimumSize(120, 92)
        self.setMaximumSize(140, 100)
        theme.theme_changed.connect(self.update)

    # value: 0 a 100 | status: texto exibido abaixo (ex.: "CHEIO")
    # tone: "green", "accent" (laranja) ou "red"
    def set_value(self, value, status="", tone="green"):
        self._value = None if value is None else max(0.0, min(100.0, float(value)))
        self._status = status
        self._tone = tone
        self.update()

    def clear(self):
        self.set_value(None)

    def paintEvent(self, event):
        colors = theme.colors
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        thickness = 9
        label_height = 18
        radius = min(self.width() / 2 - thickness / 2 - 2,
                     self.height() - label_height - thickness / 2 - 6)
        cx = self.width() / 2
        cy = 4 + thickness / 2 + radius
        arc_rect = QRectF(cx - radius, cy - radius, radius * 2, radius * 2)

        # trilho (semicírculo da esquerda para a direita, passando pelo topo)
        pen = QPen(QColor(colors["track"]), thickness)
        pen.setCapStyle(Qt.PenCapStyle.RoundCap)
        painter.setPen(pen)
        painter.drawArc(arc_rect, 180 * 16, -180 * 16)

        if self._value is None:
            painter.setPen(Qt.PenStyle.NoPen)
            painter.setBrush(QColor(colors["faint"]))
            painter.drawEllipse(QPointF(cx, cy), 3.5, 3.5)
            painter.end()
            return

        color = QColor(theme.color(self._tone))
        fraction = self._value / 100

        # arco do valor
        if fraction > 0:
            pen.setColor(color)
            painter.setPen(pen)
            painter.drawArc(arc_rect, 180 * 16, int(-180 * 16 * fraction))

        # ponteiro
        angle = math.radians(180 - 180 * fraction)
        length = radius - 2
        tip = QPointF(cx + math.cos(angle) * length, cy - math.sin(angle) * length)
        needle = QPen(color, 2.2)
        needle.setCapStyle(Qt.PenCapStyle.RoundCap)
        painter.setPen(needle)
        painter.drawLine(QPointF(cx, cy), tip)
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(color)
        painter.drawEllipse(QPointF(cx, cy), 3.5, 3.5)

        # texto do status
        if self._status:
            font = painter.font()
            font.setPixelSize(10)
            font.setBold(True)
            font.setLetterSpacing(QFont.SpacingType.AbsoluteSpacing, 0.8)
            painter.setFont(font)
            painter.setPen(color)
            text_rect = QRectF(0, cy + thickness / 2 + 6, self.width(), label_height)
            painter.drawText(text_rect, Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop, self._status)
        painter.end()
