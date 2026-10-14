import sys
import os

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QMainWindow, QTabWidget, QWidget

from qt_core import *
from gui.windows.main_window.ui_main_window import *
from gui.themes.themes import theme
from core.auth import authenticate

# MAIN WINDOW
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Projeto gasômetro")

        # usuário logado (None enquanto estiver na tela de login)
        self.user = None

        # Ajustando Main Window
        self.ui = Ui_MainWindow()
        self.ui.setup_ui(self)

        # Botão toggle
        self.ui.toggle_button.clicked.connect(self.toggle_button)

        # Botão home 
        self.ui.btn_1.clicked.connect(self.show_home_page)

        # Botão config
        self.ui.btn_2.clicked.connect(self.show_config_page)

        # Botão meus botijões
        self.ui.btn_3.clicked.connect(self.show_botijoes_page)

        # Botão pontos de troca
        self.ui.btn_4.clicked.connect(self.show_pontos_page)

        # Botão histórico
        self.ui.btn_5.clicked.connect(self.show_historico_page)

        # Botão sair
        self.ui.btn_logout.clicked.connect(self.logout)

        # Login
        self.ui.ui_login.btn_login.clicked.connect(self.login)
        self.ui.ui_login.input_user.returnPressed.connect(self.ui.ui_login.input_password.setFocus)
        self.ui.ui_login.input_password.returnPressed.connect(self.login)

        # Tema claro/escuro (chave na página de configurações)
        self.ui.ui_pages.toggle_dark_theme.set_checked_silently(theme.is_dark)
        self.ui.ui_pages.toggle_dark_theme.toggled.connect(self.change_theme)

        # Mostrando a Main Window
        self.showMaximized()
        self.ui.ui_login.input_user.setFocus()

    def reset_selection(self):
        for btn in self.ui.left_menu.findChildren(QPushButton):
            try:
                btn.set_active(False)
            except:
                pass

    # Login simples: confere usuário e senha e libera o aplicativo
    def login(self):
        login_ui = self.ui.ui_login
        username = login_ui.input_user.text()
        password = login_ui.input_password.text()

        if not username.strip() or not password:
            login_ui.show_error("Informe o usuário e a senha.")
            return

        user = authenticate(username, password)
        if user is None:
            login_ui.show_error("Usuário ou senha inválidos.")
            login_ui.input_password.clear()
            login_ui.input_password.setFocus()
            return

        self.user = user
        self.ui.set_user_info(user.name, user.role)
        login_ui.reset()
        self.ui.root_stack.setCurrentWidget(self.ui.central_frame)
        self.show_home_page()

    # Sai da conta e volta para a tela de login
    def logout(self):
        self.user = None
        self.ui.root_stack.setCurrentWidget(self.ui.login_page)
        self.ui.ui_login.input_user.setFocus()

    # Troca entre tema claro e escuro (a escolha fica salva)
    def change_theme(self, dark):
        theme.set_theme("dark" if dark else "light")

    def show_home_page(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_1)
        self.ui.btn_1.set_active(True)

    def show_config_page(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_2)
        self.ui.btn_2.set_active(True)

    def show_botijoes_page(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_3)
        self.ui.btn_3.set_active(True)

    def show_pontos_page(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_4)
        self.ui.btn_4.set_active(True)

    def show_historico_page(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_5)
        self.ui.btn_5.set_active(True)

    # Animação da barra lateral
    def toggle_button(self):
        # Buscando o tamanho do menu
        menu_width = self.ui.left_menu.width()

        # Checando o tamanho
        width = 60
        if menu_width == width:
            width = 240

        # Animação
        self.animation = QPropertyAnimation(self.ui.left_menu, b"minimumWidth")
        self.animation.setStartValue(menu_width)
        self.animation.setEndValue(width)
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.Type.InOutCirc)
        self.animation.start()

        # o texto aparece ao abrir e só some depois que o menu fecha
        if width == 240:
            self.ui.set_menu_compact(False)
        else:
            self.animation.finished.connect(lambda: self.ui.set_menu_compact(True))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    theme.apply()
    window = MainWindow()
    sys.exit(app.exec())
