from qt_core import *
from gui.pages.ui_pages import Ui_application_pages
from datetime import datetime
from gui.widgets.py_push_button import PyPushButton
from gui.widgets.py_icon import PyIconLabel, tinted_pixmap
from gui.widgets.py_icon_button import PyIconButton
from gui.windows.login_window.ui_login_window import Ui_LoginWindow
from gui.themes.themes import theme

WEEKDAYS = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira",
            "Sexta-feira", "Sábado", "Domingo"]
MONTHS = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho",
          "agosto", "setembro", "outubro", "novembro", "dezembro"]


def format_date_pt(date):
    return f"{WEEKDAYS[date.weekday()]}, {date.day} de {MONTHS[date.month - 1]} de {date.year}"


class Ui_MainWindow(object):
    def setup_ui(self, window):
        if not window.objectName():
            window.setObjectName('MainWindow')

        # Ajustando tamanho
        # window.resize(1366, 720) # minha resolução
        window.setMinimumSize(1100, 600)

        # Criando Widget crentral
        self.central_frame = QFrame()
        self.central_frame.setObjectName("central_frame")

        # Layout da pagina
        self.main_layout = QHBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # Criando a barra lateral
        self.left_menu = QFrame()
        self.left_menu.setObjectName("left_menu")
        self.left_menu.setMaximumWidth(60) # 50 pixels
        self.left_menu.setMinimumWidth(240) # começa aberto, como na referência

        # Layout barra lateral
        self.left_menu_layout = QVBoxLayout(self.left_menu)
        self.left_menu_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_layout.setSpacing(0)

        # Logotipo no topo da barra lateral
        self.left_menu_header = QFrame()
        self.left_menu_header.setFixedHeight(64)
        self.left_menu_header_layout = QHBoxLayout(self.left_menu_header)
        self.left_menu_header_layout.setContentsMargins(16, 0, 0, 0)
        self.left_menu_header_layout.setSpacing(10)

        self.logo_icon = QLabel()
        self.logo_icon.setPixmap(tinted_pixmap("icon_logo.svg", theme.colors["accent"], 28))
        self.logo_icon.setFixedSize(28, 28)
        self.logo_text = QLabel("GASÔMETRO")
        self.logo_text.setObjectName("logo_text")

        self.left_menu_header_layout.addWidget(self.logo_icon)
        self.left_menu_header_layout.addWidget(self.logo_text)
        self.left_menu_header_layout.addStretch()

        # Frame superior barra lateral
        self.left_menu_top_frame = QFrame()
        self.left_menu_top_frame.setMinimumHeight(50)
        # self.left_menu_top_frame.setStyleSheet("background-color: red")

        # Layout botões
        self.left_menu_top_layout = QVBoxLayout(self.left_menu_top_frame)
        self.left_menu_top_layout.setContentsMargins(0, 8, 0, 8)
        self.left_menu_top_layout.setSpacing(0)

        # Botões frame superior barra lateral 
        self.toggle_button = PyPushButton(
            text = "Ocultar menu",
            icon_path = "icon_menu.svg"
            )
        # sai da conta e volta para a tela de login
        self.btn_logout = PyPushButton(
            text = "Sair",
            icon_path = "icon_back.svg"
            )
        
        self.btn_1 = PyPushButton(
            text = "Visão geral",
            is_active = True,
            icon_path = "icon_overview.svg" 
            )
        self.btn_3 = PyPushButton(
            text = "Meus botijões",
            icon_path = "icon_bottle.svg"
            )
        self.btn_4 = PyPushButton(
            text = "Pontos de troca",
            icon_path = "icon_pin.svg"
            )
        self.btn_5 = PyPushButton(
            text = "Histórico",
            icon_path = "icon_clock.svg"
            )
        self.btn_2 = PyPushButton(
            text = "Configurações",
            icon_path = "icon_sliders.svg"
            )

        # Adicionando os botões ao layout
        self.left_menu_top_layout.addWidget(self.toggle_button)
        self.left_menu_top_layout.addWidget(self.btn_logout)
        self.left_menu_top_layout.addSpacing(6)
        self.left_menu_top_layout.addWidget(self.create_separator())
        self.left_menu_top_layout.addSpacing(6)
        self.left_menu_top_layout.addWidget(self.btn_1)
        self.left_menu_top_layout.addWidget(self.btn_3)
        self.left_menu_top_layout.addWidget(self.btn_4)
        self.left_menu_top_layout.addWidget(self.btn_5)
        self.left_menu_top_layout.addWidget(self.btn_2)

        # Espaçamento barra lateral
        self.left_menu_spacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, 
                                            QSizePolicy.Policy.Expanding,)

        # Frame inferior barra lateral
        self.time = datetime.now()
        self.left_menu_bottom_label = QLabel(f"{self.time.strftime("%d/%m/%Y")}")
        self.left_menu_bottom_label.setObjectName("left_menu_date")
        self.left_menu_bottom_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.left_menu_bottom_label.setMinimumHeight(30)
        self.left_menu_bottom_label.setMaximumHeight(30)

        # Adicionando ao layout
        self.left_menu_layout.addWidget(self.left_menu_header)
        self.left_menu_layout.addWidget(self.create_separator())
        self.left_menu_layout.addWidget(self.left_menu_top_frame)
        self.left_menu_layout.addItem(self.left_menu_spacer)
        self.left_menu_layout.addWidget(self.create_separator())
        self.left_menu_layout.addWidget(self.left_menu_bottom_label)

        # Conteúdo principal
        self.content = QFrame()
        self.content.setObjectName("content")

        # Layout do conteúdo 
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setSpacing(0)

        # Barra superior
        self.top_bar = QFrame()
        self.top_bar.setObjectName("top_bar")
        self.top_bar.setMaximumHeight(64)
        self.top_bar.setMinimumHeight(64)
        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(28, 0, 28, 0)
        self.top_bar_layout.setSpacing(12)

        # barra de pesquisa (ainda sem função: será ligada aos dados)
        self.search_box = QFrame()
        self.search_box.setObjectName("search_box")
        self.search_box.setFixedHeight(38)
        self.search_box.setMinimumWidth(240)
        self.search_box.setMaximumWidth(380)
        self.search_box_layout = QHBoxLayout(self.search_box)
        self.search_box_layout.setContentsMargins(14, 0, 14, 0)
        self.search_box_layout.setSpacing(8)
        self.search_icon = PyIconLabel("icon_search.svg", 18, "muted")
        self.search_input = QLineEdit()
        self.search_input.setObjectName("search_input")
        self.search_input.setPlaceholderText("Buscar botijão...")
        self.search_box_layout.addWidget(self.search_icon)
        self.search_box_layout.addWidget(self.search_input)

        # Espaçamento barra superior
        self.top_spacer = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, 
                                      QSizePolicy.Policy.Minimum)

        # notificações
        self.btn_notifications = PyIconButton("icon_bell.svg")

        # usuário (avatar + nome + função)
        self.avatar = QLabel("")
        self.avatar.setObjectName("avatar")
        self.avatar.setFixedSize(36, 36)
        self.avatar.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.user_layout = QVBoxLayout()
        self.user_layout.setContentsMargins(0, 0, 0, 0)
        self.user_layout.setSpacing(0)

        # label direito barra superior (nome do usuário)
        self.top_label_right = QLabel("")
        self.top_label_right.setObjectName("user_name")
        self.top_label_role = QLabel("")
        self.top_label_role.setObjectName("user_role")
        self.user_layout.addStretch()
        self.user_layout.addWidget(self.top_label_right)
        self.user_layout.addWidget(self.top_label_role)
        self.user_layout.addStretch()

        # adicionando os itens para a barra
        self.top_bar_layout.addWidget(self.search_box)
        self.top_bar_layout.addItem(self.top_spacer)
        self.top_bar_layout.addWidget(self.btn_notifications)
        self.top_bar_layout.addSpacing(6)
        self.top_bar_layout.addWidget(self.avatar)
        self.top_bar_layout.addLayout(self.user_layout)

        # Página central
        self.pages = QStackedWidget()
        self.pages.setObjectName("pages")
        self.ui_pages = Ui_application_pages()
        self.ui_pages.setupUi(self.pages)
        self.ui_pages.lbl_home_date.setText(format_date_pt(self.time))

        # Adicionando conteúdo ao layout
        self.content_layout.addWidget(self.top_bar)
        self.content_layout.addWidget(self.pages)

        # Adicionando barra lateral e coteúdo
        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.content)

        # Tela de login (aparece antes do aplicativo)
        self.login_page = QFrame()
        self.ui_login = Ui_LoginWindow()
        self.ui_login.setup_ui(self.login_page)

        self.root_stack = QStackedWidget()
        self.root_stack.setObjectName("root_stack")
        self.root_stack.addWidget(self.login_page)
        self.root_stack.addWidget(self.central_frame)

        # Ajustando Central widget
        window.setCentralWidget(self.root_stack)

    # linha fina que separa os grupos da barra lateral
    def create_separator(self):
        separator = QFrame()
        separator.setProperty("role", "menu_separator")
        separator.setFixedHeight(1)
        return separator

    # mostra nome, função e iniciais do usuário logado na barra superior
    def set_user_info(self, name, role):
        self.top_label_right.setText(name)
        self.top_label_role.setText(role)
        words = name.split()
        if len(words) >= 2:
            initials = words[0][0] + words[-1][0]
        else:
            initials = name[:2]
        self.avatar.setText(initials.upper())

    # menu recolhido: esconde o texto do logotipo e dos botões
    def set_menu_compact(self, compact):
        self.logo_text.setVisible(not compact)
        for btn in self.left_menu.findChildren(PyPushButton):
            btn.set_collapsed(compact)
