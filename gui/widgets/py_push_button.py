import os

from PySide6.QtGui import QPaintEvent
from qt_core import *

from gui.themes.themes import theme

class PyPushButton(QPushButton):
    # cores = None usa as cores do tema ativo (claro/escuro)
    def __init__(self,
                text= "",
                height = 44,
                minimum_width = 60,
                text_padding = 44, 
                text_color = None,
                icon_path = "",
                icon_color = None,
                btn_color = None,
                btn_hover = None,
                btn_pressed = None,
                is_active = False): 
        super().__init__()


        # texto padrão
        self.setText(text)
        self.setMaximumHeight(height)
        self.setMinimumHeight(height)
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        # parametros customizados
        self.full_text = text
        self.minimum_width = minimum_width
        self.text_padding = text_padding
        self.text_color = text_color
        self.icon_path = icon_path
        self.icon_color = icon_color
        self.btn_color = btn_color
        self.btn_hover = btn_hover
        self.btn_pressed = btn_pressed
        self.is_active = is_active
        
    # aplicando o estilo
        self.set_style(
            text_padding = self.text_padding,
            text_color = self.text_color,
            btn_color = self.btn_color,
            btn_hover = self.btn_hover,
            btn_pressed = self.btn_pressed,
            is_active = self.is_active
        )

        # refaz o estilo quando o tema muda
        theme.theme_changed.connect(self.refresh_style)

    # mudando o estado do botão
    def set_active(self, check_is_active):
        self.is_active = check_is_active
        self.refresh_style()

    def refresh_style(self):
        self.set_style(
            text_padding = self.text_padding,
            text_color = self.text_color,
            btn_color = self.btn_color,
            btn_hover = self.btn_hover,
            btn_pressed = self.btn_pressed,
            is_active = self.is_active
        )
        self.update()

    # com o menu recolhido o texto some e só o ícone fica visível
    def set_collapsed(self, collapsed):
        self.setText("" if collapsed else self.full_text)

    def set_style(
        self, 
        text_padding = 44,
        text_color = None,
        btn_color = None,
        btn_hover = None,
        btn_pressed = None,
        is_active = False
    ):
        colors = theme.colors
        text_color = text_color or colors["sidebar_text"]
        btn_color = btn_color or "transparent"
        btn_hover = btn_hover or colors["sidebar_hover"]
        btn_pressed = btn_pressed or colors["sidebar_pressed"]

        style = f"""
        QPushButton {{
            color: {text_color};
            background-color: {btn_color};
            padding-left: {text_padding}px;
            text-align: left;
            border: none;
            border-radius: 10px;
            margin: 2px 10px;
            outline: none;
        }}
        QPushButton:hover {{
            background-color: {btn_hover};
        }}
        QPushButton:pressed {{
            background-color: {btn_pressed};
        }}
        """

        active_style = f"""
        QPushButton {{
            background-color: {colors["accent"]};
            color: {colors["sidebar_active_text"]};
            font-weight: 700;
        }}
        QPushButton:hover {{
            background-color: {colors["accent_hover"]};
        }}
        """
        if not is_active:
            self.setStyleSheet(style)
        else:
            self.setStyleSheet(style + active_style)

    # gerando o campo para pintar os icones
    def paintEvent(self, event):
        QPushButton.paintEvent(self, event)

        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.RenderHint.Antialiasing)
        qp.setPen(Qt.PenStyle.NoPen)

        rect = QRect(0, 0, self.minimum_width, self.height())

        # o ícone do item ativo acompanha a cor do texto ativo
        if self.is_active:
            color = theme.colors["sidebar_active_text"]
        else:
            color = self.icon_color or theme.colors["sidebar_text"]
        self.draw_icon(qp, self.icon_path, rect, color)

        qp.end()

    # pintando os icones
    def draw_icon(self, qp, image, rect, color):
        # procurar a pasta de icones
        app_path = os.path.abspath(os.getcwd())
        folder = "gui/images/icons"
        path = os.path.join(app_path, folder)
        icon_path = os.path.normpath(os.path.join(path, image))

        # desenhando o icone
        icon = QPixmap(icon_path)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceIn)
        painter.fillRect(icon.rect(), QColor(color))
        painter.end()

        qp.drawPixmap(
            int((rect.width() - icon.width()) / 2),
            int((rect.height() - icon.height()) / 2),
            icon
        )
