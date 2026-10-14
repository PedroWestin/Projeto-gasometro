from qt_core import *

from gui.themes.themes import theme


class PyToggle(QCheckBox):
    # chave liga/desliga animada (usa o sinal toggled(bool) do QCheckBox)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(48, 26)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self._position = 0.0

        self._animation = QPropertyAnimation(self, b"position", self)
        self._animation.setDuration(180)
        self._animation.setEasingCurve(QEasingCurve.Type.InOutCubic)
        self.toggled.connect(self._animate)
        theme.theme_changed.connect(self.update)

    def _get_position(self):
        return self._position

    def _set_position(self, value):
        self._position = value
        self.update()

    position = Property(float, _get_position, _set_position)

    def _animate(self, checked):
        self._animation.stop()
        self._animation.setEndValue(1.0 if checked else 0.0)
        self._animation.start()

    # muda o estado sem emitir toggled (usado ao carregar o tema salvo)
    def set_checked_silently(self, checked):
        self.blockSignals(True)
        self.setChecked(checked)
        self.blockSignals(False)
        self._animation.stop()
        self._position = 1.0 if checked else 0.0
        self.update()

    def hitButton(self, pos):
        return self.contentsRect().contains(pos)

    def paintEvent(self, event):
        colors = theme.colors
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setPen(Qt.PenStyle.NoPen)

        track = QColor(colors["track"])
        on = QColor(colors["accent"])
        # mistura a cor do trilho conforme a posição do botão
        mix = self._position
        blended = QColor(
            int(track.red() + (on.red() - track.red()) * mix),
            int(track.green() + (on.green() - track.green()) * mix),
            int(track.blue() + (on.blue() - track.blue()) * mix),
        )
        painter.setBrush(blended)
        painter.drawRoundedRect(self.rect(), self.height() / 2, self.height() / 2)

        margin = 3
        diameter = self.height() - margin * 2
        x = margin + (self.width() - diameter - margin * 2) * self._position
        painter.setBrush(QColor("#ffffff"))
        painter.drawEllipse(QRectF(x, margin, diameter, diameter))
        painter.end()
