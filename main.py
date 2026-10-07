import sys
import os

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QMainWindow, QTabWidget, QWidget

from qt_core import *
from gui.windows.main_window.ui_main_window import *

# MAIN WINDOW
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Projeto gasômetro")

        # Ajustando Main Window
        self.ui = Ui_MainWindow()
        self.ui.setup_ui(self)

        # Botão toggle
        self.ui.toggle_button.clicked.connect(self.toggle_button)

        # Botão home 
        self.ui.btn_1.clicked.connect(self.show_home_page)

        # Botão config
        self.ui.btn_2.clicked.connect(self.show_config_page)

        # Mostrando a Main Window
        self.showMaximized()

    def reset_selection(self):
        for btn in self.ui.left_menu.findChildren(QPushButton):
            try:
                btn.set_active(False)
            except:
                pass



    def show_home_page(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_1)
        self.ui.btn_1.set_active(True)

    def show_config_page(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_2)
        self.ui.btn_2.set_active(True)

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
