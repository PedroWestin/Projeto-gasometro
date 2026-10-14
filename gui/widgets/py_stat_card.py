from qt_core import *

from gui.themes.themes import repolish, theme
from gui.widgets.py_icon import tinted_pixmap


class _IconBadge(QWidget):
    # quadradinho colorido com ícone (canto do card)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.icon_name = ""
        self.tone = "blue"
        self.setFixedSize(38, 38)
        theme.theme_changed.connect(self.update)

    def configure(self, icon_name, tone):
        self.icon_name = icon_name or ""
        self.tone = tone or "blue"
        self.update()

    def paintEvent(self, event):
        colors = theme.colors
        base = QColor(theme.color(self.tone))
        tint = QColor(base)
        # fundo = cor do tom com pouca opacidade sobre o card
        tint.setAlphaF(0.16 if theme.is_dark else 0.12)

        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(tint)
        painter.drawRoundedRect(self.rect(), 10, 10)
        if self.icon_name:
            painter.drawPixmap(11, 11, tinted_pixmap(self.icon_name, base.name(), 16))
        painter.end()


class PyStatCard(QFrame):
    # card de indicador (KPI). Configurável no pages.ui por propriedades dinâmicas:
    #   title -> texto do título | icon -> arquivo svg | tone -> "blue", "green", "red" ou "accent"
    # os valores são definidos depois com set_value() e set_hint()
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setMinimumHeight(118)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(20, 18, 20, 18)
        layout.setSpacing(12)

        text_layout = QVBoxLayout()
        text_layout.setSpacing(2)
        self.title_label = QLabel()
        self.title_label.setProperty("role", "muted")
        self.title_label.setWordWrap(True)
        self.value_label = QLabel("—")
        self.value_label.setProperty("role", "stat_value")
        self.value_label.setMinimumHeight(40)
        self.hint_label = QLabel()
        self.hint_label.setProperty("role", "stat_hint")
        self.hint_label.setWordWrap(True)
        self.hint_label.setMinimumHeight(18)
        text_layout.addWidget(self.title_label)
        text_layout.addWidget(self.value_label)
        text_layout.addWidget(self.hint_label)

        self.badge = _IconBadge()
        layout.addLayout(text_layout, 1)
        layout.addWidget(self.badge, 0, Qt.AlignmentFlag.AlignTop)

        self.setProperty("role", "card")

    def event(self, e):
        if e.type() == QEvent.Type.DynamicPropertyChange and hasattr(self, "badge"):
            self.title_label.setText(self.property("title") or "")
            self.badge.configure(self.property("icon"), self.property("tone"))
        return super().event(e)

    def set_value(self, text):
        self.value_label.setText(text)

    # tone: "green", "orange" ou "red"
    def set_hint(self, text, tone="green"):
        self.hint_label.setText(text)
        self.hint_label.setProperty("tone", tone)
        repolish(self.hint_label)
