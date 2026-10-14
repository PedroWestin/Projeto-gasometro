from qt_core import *

from gui.themes.themes import theme
from gui.widgets.py_icon import tinted_pixmap


class Ui_LoginWindow(object):
    def setup_ui(self, page):
        page.setObjectName("login_page")

        # Layout da pagina
        self.main_layout = QHBoxLayout(page)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # Painel da marca (esquerda)
        self.brand_panel = QFrame()
        self.brand_panel.setObjectName("login_brand")
        self.brand_layout = QVBoxLayout(self.brand_panel)
        self.brand_layout.setContentsMargins(72, 56, 72, 56)
        self.brand_layout.setSpacing(0)

        self.brand_logo_row = QHBoxLayout()
        self.brand_logo_row.setSpacing(12)
        self.brand_logo_icon = QLabel()
        self.brand_logo_icon.setPixmap(tinted_pixmap("icon_logo.svg", theme.colors["accent"], 32))
        self.brand_logo_icon.setFixedSize(32, 32)
        self.brand_logo_text = QLabel("GASÔMETRO")
        self.brand_logo_text.setObjectName("logo_text")
        self.brand_logo_row.addWidget(self.brand_logo_icon)
        self.brand_logo_row.addWidget(self.brand_logo_text)
        self.brand_logo_row.addStretch()

        self.brand_title = QLabel("ACOMPANHE SEUS BOTIJÕES DE GÁS")
        self.brand_title.setObjectName("login_brand_title")
        self.brand_title.setWordWrap(True)
        self.brand_text = QLabel("Nível, consumo e pontos de troca em um só lugar.")
        self.brand_text.setObjectName("login_brand_text")
        self.brand_text.setWordWrap(True)

        self.brand_layout.addLayout(self.brand_logo_row)
        self.brand_layout.addStretch()
        self.brand_layout.addWidget(self.brand_title)
        self.brand_layout.addSpacing(12)
        self.brand_layout.addWidget(self.brand_text)
        self.brand_layout.addStretch()

        # Painel do formulário (direita)
        self.form_panel = QFrame()
        self.form_panel_layout = QVBoxLayout(self.form_panel)
        self.form_panel_layout.setContentsMargins(32, 32, 32, 32)

        self.login_card = QFrame()
        self.login_card.setProperty("role", "card")
        self.login_card.setFixedWidth(400)
        self.card_layout = QVBoxLayout(self.login_card)
        self.card_layout.setContentsMargins(32, 32, 32, 32)
        self.card_layout.setSpacing(6)

        self.lbl_title = QLabel("ENTRAR")
        self.lbl_title.setProperty("role", "page_title")
        self.lbl_subtitle = QLabel("Acesse sua conta para continuar")
        self.lbl_subtitle.setProperty("role", "page_subtitle")

        self.lbl_user = QLabel("Usuário")
        self.lbl_user.setProperty("role", "muted")
        self.input_user = QLineEdit()
        self.input_user.setProperty("variant", "field")
        self.input_user.setPlaceholderText("Seu usuário")

        self.lbl_password = QLabel("Senha")
        self.lbl_password.setProperty("role", "muted")
        self.input_password = QLineEdit()
        self.input_password.setProperty("variant", "field")
        self.input_password.setPlaceholderText("Sua senha")
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)

        # mensagem de erro (vazia enquanto não houver erro)
        self.lbl_error = QLabel("")
        self.lbl_error.setProperty("role", "error")
        self.lbl_error.setMinimumHeight(20)

        self.btn_login = QPushButton("Entrar")
        self.btn_login.setProperty("variant", "primary")
        self.btn_login.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_login.setMinimumHeight(42)

        self.card_layout.addWidget(self.lbl_title)
        self.card_layout.addWidget(self.lbl_subtitle)
        self.card_layout.addSpacing(18)
        self.card_layout.addWidget(self.lbl_user)
        self.card_layout.addWidget(self.input_user)
        self.card_layout.addSpacing(8)
        self.card_layout.addWidget(self.lbl_password)
        self.card_layout.addWidget(self.input_password)
        self.card_layout.addSpacing(4)
        self.card_layout.addWidget(self.lbl_error)
        self.card_layout.addSpacing(4)
        self.card_layout.addWidget(self.btn_login)

        self.form_panel_layout.addStretch()
        self.form_panel_layout.addWidget(self.login_card, 0, Qt.AlignmentFlag.AlignHCenter)
        self.form_panel_layout.addStretch()

        # Adicionando os paineis
        self.main_layout.addWidget(self.brand_panel, 1)
        self.main_layout.addWidget(self.form_panel, 1)

    def show_error(self, message):
        self.lbl_error.setText(message)

    def reset(self):
        # limpa os campos (chamado ao entrar e ao sair)
        self.input_user.clear()
        self.input_password.clear()
        self.lbl_error.clear()
