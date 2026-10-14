from datetime import date

from qt_core import *

from gui.themes.themes import theme

WEEKDAYS = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"]
MONTHS = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]


def last_days_labels(count=7):
    today = date.today().toordinal()
    return [WEEKDAYS[date.fromordinal(today - i).weekday()] for i in range(count - 1, -1, -1)]


def last_months_labels(count=6):
    today = date.today()
    months = [(today.month - 1 - i) % 12 for i in range(count - 1, -1, -1)]
    return [MONTHS[m] for m in months]


class PyBarChart(QWidget):
    # gráfico de barras. Configurável no pages.ui por propriedades dinâmicas:
    #   tone   -> cor das barras: "blue" ou "accent" (laranja)
    #   period -> rótulos automáticos: "days7" (últimos 7 dias) ou "months6" (últimos 6 meses)
    # sem valores: mostra só os rótulos e o aviso "Sem dados"
    def __init__(self, parent=None):
        super().__init__(parent)
        self._values = []
        self._labels = []
        self._max_value = None
        self.setMinimumHeight(150)
        theme.theme_changed.connect(self.update)

    def event(self, e):
        if e.type() == QEvent.Type.DynamicPropertyChange:
            self.update()
        return super().event(e)

    # values: um valor por barra | max_value: valor que ocupa 100% da altura (opcional)
    def set_values(self, values, max_value=None):
        self._values = [float(v) for v in values]
        self._max_value = max_value
        self.update()

    def set_labels(self, labels):
        self._labels = list(labels)
        self.update()

    def clear(self):
        self.set_values([])

    def _current_labels(self):
        if self._labels:
            return self._labels
        period = self.property("period")
        if period == "days7":
            return last_days_labels(7)
        if period == "months6":
            return last_months_labels(6)
        return [""] * len(self._values)

    def paintEvent(self, event):
        colors = theme.colors
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        labels = self._current_labels()
        count = max(len(labels), len(self._values))
        if count == 0:
            painter.end()
            return

        label_height = 24
        gap = 10
        slot = self.width() / count
        bar_width = max(slot - gap, 4)
        chart_height = self.height() - label_height

        font = painter.font()
        font.setPixelSize(11)
        painter.setFont(font)

        if not self._values:
            painter.setPen(QColor(colors["faint"]))
            painter.drawText(QRectF(0, 0, self.width(), chart_height), Qt.AlignmentFlag.AlignCenter, "Sem dados")
        else:
            peak = self._max_value or max(self._values) or 1
            painter.setPen(Qt.PenStyle.NoPen)
            painter.setBrush(QColor(theme.color(self.property("tone") or "blue")))
            for i, value in enumerate(self._values):
                height = max(chart_height * min(value / peak, 1), 3)
                x = i * slot + gap / 2
                painter.drawRoundedRect(QRectF(x, chart_height - height, bar_width, height), 4, 4)

        painter.setPen(QColor(colors["faint"]))
        for i, label in enumerate(labels):
            painter.drawText(QRectF(i * slot, chart_height + 4, slot, label_height - 4),
                             Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop, label)
        painter.end()
