from qt_core import *


class PyPontoCard(QFrame):
    # card de um ponto de troca. Vazio por padrão: preencher com set_data()
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(22, 18, 22, 18)
        layout.setSpacing(2)

        self.distance_label = QLabel()
        self.distance_label.setProperty("role", "distance")
        self.name_label = QLabel()
        self.name_label.setProperty("role", "card_title")
        self.address_label = QLabel()
        self.address_label.setProperty("role", "muted")

        self.divider = QFrame()
        self.divider.setProperty("role", "divider")

        bottom = QHBoxLayout()
        self.hours_label = QLabel()
        self.hours_label.setProperty("role", "muted")
        self.price_label = QLabel()
        self.price_label.setProperty("role", "value")
        self.price_label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        bottom.addWidget(self.hours_label, 1)
        bottom.addWidget(self.price_label)

        layout.addWidget(self.distance_label)
        layout.addWidget(self.name_label)
        layout.addWidget(self.address_label)
        layout.addSpacing(12)
        layout.addWidget(self.divider)
        layout.addSpacing(8)
        layout.addLayout(bottom)

        for label in (self.distance_label, self.name_label, self.address_label,
                      self.hours_label, self.price_label):
            label.setMinimumHeight(20)
        for label in (self.name_label, self.address_label):
            label.setWordWrap(True)

        self.setProperty("role", "card")

    def set_data(self, distance, name, address, hours, price):
        self.distance_label.setText(distance)
        self.name_label.setText(name)
        self.address_label.setText(address)
        self.hours_label.setText(hours)
        self.price_label.setText(price)

    def clear(self):
        self.set_data("", "", "", "", "")
