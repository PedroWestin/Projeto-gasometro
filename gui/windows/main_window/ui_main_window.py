from qt_core import *
from gui.pages.ui_pages import Ui_application_pages
from datetime import datetime
from gui.widgets.py_push_button import PyPushButton

class Ui_MainWindow(object):
    def setup_ui(self, window):
        if not window.objectName():
            window.setObjectName('MainWindow')

        # Ajustando tamanho
        # window.resize(1366, 720) # minha resolução
        window.setMinimumSize(960, 540)

        # Criando Widget crentral
        self.central_frame = QFrame()

        # Layout da pagina
        self.main_layout = QHBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # Criando a barra lateral
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet("background-color: #44475a")
        self.left_menu.setMaximumWidth(60) # 50 pixels
        self.left_menu.setMinimumWidth(60)

        # Layout barra lateral
        self.left_menu_layout = QVBoxLayout(self.left_menu)
        self.left_menu_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_layout.setSpacing(0)

        # Frame superior barra lateral
        self.left_menu_top_frame = QFrame()
        self.left_menu_top_frame.setMinimumHeight(50)
        # self.left_menu_top_frame.setStyleSheet("background-color: red")

        # Layout botões
        self.left_menu_top_layout = QVBoxLayout(self.left_menu_top_frame)
        self.left_menu_top_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_top_layout.setSpacing(0)

        # Botões frame superior barra lateral 
        self.toggle_button = PyPushButton(
            text = "Ocultar menu",
            icon_path = "icon_menu.svg"
            )
        
        self.btn_1 = PyPushButton(
            text = "Página inicial",
            is_active = True,
            icon_path = "icon_home.svg" 
            )
        self.btn_2 = PyPushButton(
            text = "Configurações",
            icon_path = "icon_settings.svg"
            )

        # Adicionando os botões ao layout
        self.left_menu_top_layout.addWidget(self.toggle_button)
        self.left_menu_top_layout.addWidget(self.btn_1)
        self.left_menu_top_layout.addWidget(self.btn_2)

        # Espaçamento barra lateral
        self.left_menu_spacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, 
                                            QSizePolicy.Policy.Expanding,)

        # Frame inferior barra lateral
        self.time = datetime.now()
        self.left_menu_bottom_label = QLabel(f"{self.time.strftime("%d/%m/%Y")}")
        self.left_menu_bottom_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.left_menu_bottom_label.setMinimumHeight(30)
        self.left_menu_bottom_label.setMaximumHeight(30)

        # Adicionando ao layout
        self.left_menu_layout.addWidget(self.left_menu_top_frame)
        self.left_menu_layout.addItem(self.left_menu_spacer)
        self.left_menu_layout.addWidget(self.left_menu_bottom_label)

        # Conteúdo principal
        self.content = QFrame()
        self.content.setStyleSheet("background-color: #282a36")

        # Layout do conteúdo 
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setSpacing(0)

        # Barra superior
        self.top_bar = QFrame()
        self.top_bar.setMaximumHeight(30)
        self.top_bar.setMinimumHeight(30)
        self.top_bar.setStyleSheet("background-color: #21232d; color: #6272a4")
        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(10, 0, 10, 0)

        # label esquerdo barra superior
        self.top_label_left = QLabel("Barra de pesquisa | Projeto Gasômetro")

        # Espaçamento barra superior
        self.top_spacer = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, 
                                      QSizePolicy.Policy.Minimum)

        # label direito barra superior
        self.top_label_right = QLabel("User")
        self.top_label_right.setStyleSheet("font: 700 9pt 'Segoe UI'")

        # adicionando os labels para a barra
        self.top_bar_layout.addWidget(self.top_label_left)
        self.top_bar_layout.addItem(self.top_spacer)
        self.top_bar_layout.addWidget(self.top_label_right)

        # Página central
        self.pages = QStackedWidget()
        self.pages.setStyleSheet("font-size: 12pt; color: white")
        self.ui_pages = Ui_application_pages()
        self.ui_pages.setupUi(self.pages)

        # Rodapé
        self.bottom_bar = QFrame()
        self.bottom_bar.setMaximumHeight(30)
        self.bottom_bar.setMinimumHeight(30)
        self.bottom_bar.setStyleSheet("background-color: #21232d; color: #6272a4")        

        # Adicionando conteúdo ao layout
        self.content_layout.addWidget(self.top_bar)
        self.content_layout.addWidget(self.pages)
        self.content_layout.addWidget(self.bottom_bar)

        # Adicionando barra lateral e coteúdo
        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.content)

        # Ajustando Central widget
        window.setCentralWidget(self.central_frame)