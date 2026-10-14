from qt_core import *

from gui.themes.themes import theme


class PyDonutChart(QWidget):
    # gráfico de rosca. sem dados: anel cinza
    def __init__(self, parent=None):
        super().__init__(parent)
        self._segments = []
        self._center_text = ""
        self.setMinimumSize(130, 130)
        theme.theme_changed.connect(self.update)

    # segments: lista de (valor, cor) | cor = chave da paleta ("green") ou hex
    def set_data(self, segments, center_text=""):
        self._segments = [(float(v), c) for v, c in segments if float(v) > 0]
        self._center_text = center_text
        self.update()

    def clear(self):
        self.set_data([])

    def paintEvent(self, event):
        colors = theme.colors
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        side = min(self.width(), self.height()) - 4
        thickness = side * 0.26
        rect = QRectF((self.width() - side) / 2 + thickness / 2,
                      (self.height() - side) / 2 + thickness / 2,
                      side - thickness, side - thickness)

        pen = QPen(QColor(colors["track"]), thickness)
        pen.setCapStyle(Qt.PenCapStyle.FlatCap)
        painter.setPen(pen)

        total = sum(v for v, _ in self._segments)
        if total <= 0:
            painter.drawArc(rect, 0, 360 * 16)
        else:
            # começa no topo e segue no sentido horário
            start = 90 * 16
            for value, color in self._segments:
                span = int(-360 * 16 * value / total)
                pen.setColor(QColor(theme.color(color)))
                painter.setPen(pen)
                painter.drawArc(rect, start, span)
                start += span

        if self._center_text:
            font = painter.font()
            font.setPixelSize(17)
            font.setBold(True)
            painter.setFont(font)
            painter.setPen(QColor(colors["text"]))
            painter.drawText(self.rect(), Qt.AlignmentFlag.AlignCenter, self._center_text)
        painter.end()
