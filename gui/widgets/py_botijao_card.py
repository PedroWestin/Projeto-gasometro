from qt_core import *

from gui.widgets.py_gauge import PyGauge


class PyBotijaoCard(QFrame):
    # card de um botijão. Vazio por padrão: preencher com set_data()
    # os botões ficam expostos em btn_details e btn_swap para ligar às ações
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(22, 20, 22, 20)
        layout.setSpacing(4)

        self.name_label = QLabel()
        self.name_label.setProperty("role", "card_title")
        self.code_label = QLabel()
        self.code_label.setProperty("role", "code")
        self.name_label.setMinimumHeight(22)
        self.code_label.setMinimumHeight(16)
        for label in (self.name_label, self.code_label):
            label.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)

        # medidor + informações
        body = QHBoxLayout()
        body.setContentsMargins(0, 14, 0, 14)
        body.setSpacing(24)
        self.gauge = PyGauge()

        info = QGridLayout()
        info.setHorizontalSpacing(16)
        info.setVerticalSpacing(10)
        self.autonomy_caption = QLabel("Autonomia")
        self.autonomy_caption.setProperty("role", "muted")
        self.autonomy_label = QLabel("—")
        self.autonomy_label.setProperty("role", "value")
        self.autonomy_label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.reading_caption = QLabel("Última leitura")
        self.reading_caption.setProperty("role", "muted")
        self.reading_label = QLabel("—")
        self.reading_label.setProperty("role", "value")
        self.reading_label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        info.addWidget(self.autonomy_caption, 0, 0)
        info.addWidget(self.autonomy_label, 0, 1)
        info.addWidget(self.reading_caption, 1, 0)
        info.addWidget(self.reading_label, 1, 1)
        info.setColumnStretch(0, 1)

        body.addWidget(self.gauge, 0, Qt.AlignmentFlag.AlignVCenter)
        body.addLayout(info, 1)

        # ações
        buttons = QHBoxLayout()
        buttons.setSpacing(12)
        self.btn_details = QPushButton("Ver detalhes")
        self.btn_details.setProperty("variant", "dark")
        self.btn_swap = QPushButton("Solicitar troca")
        self.btn_swap.setProperty("variant", "primary")
        for button in (self.btn_details, self.btn_swap):
            button.setCursor(Qt.CursorShape.PointingHandCursor)
            buttons.addWidget(button, 1)

        layout.addWidget(self.name_label)
        layout.addWidget(self.code_label)
        layout.addLayout(body)
        layout.addLayout(buttons)

        self.setProperty("role", "card")

    # level: 0 a 100 | status_text: "CHEIO", "BAIXO"... | tone: "green", "accent" ou "red"
    def set_data(self, name, code, level, status_text, tone, autonomy, last_reading):
        self.name_label.setText(name)
        self.code_label.setText(code)
        self.gauge.set_value(level, status_text, tone)
        self.autonomy_label.setText(autonomy)
        self.reading_label.setText(last_reading)

    def clear(self):
        self.set_data("", "", None, "", "green", "—", "—")
