from PySide6.QtCore import QObject, QSettings, Signal
from PySide6.QtGui import QFontDatabase
from PySide6.QtWidgets import QApplication

# PALETAS
# Tema claro: cores extraídas das imagens de referência.
LIGHT = {
    "bg": "#e9edee",              # fundo da área de conteúdo
    "surface": "#ffffff",         # cards e barra superior
    "border": "#e1e5e8",
    "text": "#1b1f2a",
    "muted": "#5f666d",
    "faint": "#878b8e",
    "input_bg": "#e9edee",
    "track": "#e4e8ea",           # trilho de gauge, rosca e barras
    "scroll": "#c9cfd3",

    "accent": "#ff5a20",
    "accent_hover": "#ff7440",
    "accent_pressed": "#e84e17",
    "on_accent": "#ffffff",

    "btn_dark": "#1b1f28",
    "btn_dark_hover": "#2c3240",
    "on_btn_dark": "#ffffff",

    "blue": "#1e6fda",
    "green": "#2e9f43",
    "red": "#e53945",

    "panel": "#1b1f28",           # painel escuro (resumo financeiro)
    "panel_muted": "#9aa3b5",

    "sidebar": "#1b1f28",
    "sidebar_text": "#c8ccd4",
    "sidebar_muted": "#6f7787",
    "sidebar_hover": "#2a303c",
    "sidebar_pressed": "#12151b",
    "sidebar_line": "#2a2f3a",
    "sidebar_active_text": "#1b1f28",
    "brand": "#1b1f28",           # painel de marca da tela de login
}

DARK = {
    "bg": "#10131a",
    "surface": "#1a1f2a",
    "border": "#2a3140",
    "text": "#e8ebf0",
    "muted": "#9aa3b5",
    "faint": "#6f788a",
    "input_bg": "#232a37",
    "track": "#2b3342",
    "scroll": "#3a4356",

    "accent": "#ff5a20",
    "accent_hover": "#ff7440",
    "accent_pressed": "#e84e17",
    "on_accent": "#ffffff",

    "btn_dark": "#2c3445",
    "btn_dark_hover": "#3a455b",
    "on_btn_dark": "#ffffff",

    "blue": "#3b82e8",
    "green": "#3dbb58",
    "red": "#f0525e",

    "panel": "#262d3b",
    "panel_muted": "#9aa3b5",

    "sidebar": "#0c0f14",
    "sidebar_text": "#aab3c5",
    "sidebar_muted": "#6f788a",
    "sidebar_hover": "#1a1f2a",
    "sidebar_pressed": "#07090c",
    "sidebar_line": "#1f2530",
    "sidebar_active_text": "#10131a",
    "brand": "#0c0f14",
}

THEMES = {"light": LIGHT, "dark": DARK}

# FONTES
# Usa a primeira fonte instalada de cada lista (a de referência vem primeiro).
UI_FONTS = ["Inter", "Segoe UI", "SF Pro Text", "Helvetica Neue", "Roboto", "Arial"]
TITLE_FONTS = ["Bebas Neue", "Anton", "Oswald", "Arial Narrow", "Segoe UI"]
MONO_FONTS = ["JetBrains Mono", "Cascadia Mono", "Consolas", "Menlo", "DejaVu Sans Mono", "Courier New"]

# tamanho/peso dos títulos conforme a fonte encontrada (fontes condensadas são menores)
TITLE_METRICS = {
    "Bebas Neue": (30, 22, 32, 400),
    "Anton": (26, 19, 28, 400),
    "Oswald": (26, 19, 28, 600),
}
TITLE_METRICS_DEFAULT = (22, 17, 24, 700)  # (página, seção, valor KPI, peso)


def _pick_font(candidates, fallback):
    installed = set(QFontDatabase.families())
    for family in candidates:
        if family in installed:
            return family
    return fallback


def repolish(widget):
    # reaplica o estilo depois de mudar uma propriedade dinâmica em tempo de execução
    widget.style().unpolish(widget)
    widget.style().polish(widget)
    widget.update()


def build_stylesheet(c, fonts):
    ui, title, mono = fonts["ui"], fonts["title"], fonts["mono"]
    page_px, section_px, stat_px, title_weight = TITLE_METRICS.get(title, TITLE_METRICS_DEFAULT)

    return f"""
    QWidget {{
        color: {c['text']};
        font-family: "{ui}";
        font-size: 13px;
    }}
    QMainWindow, #root_stack, #central_frame {{ background-color: {c['bg']}; }}
    QToolTip {{
        background-color: {c['surface']};
        color: {c['text']};
        border: 1px solid {c['border']};
        padding: 4px 8px;
    }}

    /* ---------- barra lateral ---------- */
    #left_menu {{ background-color: {c['sidebar']}; }}
    #logo_text {{
        color: #ffffff;
        font-family: "{title}";
        font-size: {section_px + 2}px;
        font-weight: {title_weight};
    }}
    QFrame[role="menu_separator"] {{
        background-color: {c['sidebar_line']};
        border: none;
        min-height: 1px;
        max-height: 1px;
    }}
    #left_menu_date {{
        color: {c['sidebar_muted']};
        font-family: "{mono}";
        font-size: 10px;
    }}

    /* ---------- barra superior ---------- */
    #content {{ background-color: {c['bg']}; }}
    #top_bar {{
        background-color: {c['surface']};
        border-bottom: 1px solid {c['border']};
    }}
    #search_box {{ background-color: {c['input_bg']}; border-radius: 10px; }}
    #search_input {{
        background: transparent;
        border: none;
        color: {c['text']};
        selection-background-color: {c['accent']};
    }}
    #user_name {{ font-weight: 700; }}
    #user_role {{ color: {c['muted']}; font-size: 11px; }}
    #avatar {{
        background-color: {c['blue']};
        color: #ffffff;
        border-radius: 18px;
        font-size: 12px;
        font-weight: 700;
    }}

    /* ---------- páginas ---------- */
    #pages {{ background: transparent; }}
    QScrollArea {{ background: transparent; border: none; }}
    QScrollArea > QWidget > QWidget {{ background: transparent; }}
    QScrollBar:vertical {{ background: transparent; width: 12px; margin: 4px 2px; }}
    QScrollBar:horizontal {{ background: transparent; height: 12px; margin: 2px 4px; }}
    QScrollBar::handle:vertical {{ background: {c['scroll']}; border-radius: 4px; min-height: 30px; }}
    QScrollBar::handle:horizontal {{ background: {c['scroll']}; border-radius: 4px; min-width: 30px; }}
    QScrollBar::handle:vertical:hover, QScrollBar::handle:horizontal:hover {{ background: {c['faint']}; }}
    QScrollBar::add-line, QScrollBar::sub-line {{ width: 0; height: 0; }}
    QScrollBar::add-page, QScrollBar::sub-page {{ background: transparent; }}

    QFrame[role="card"] {{
        background-color: {c['surface']};
        border: 1px solid {c['border']};
        border-radius: 14px;
    }}
    QFrame[role="divider"] {{
        background-color: {c['border']};
        border: none;
        min-height: 1px;
        max-height: 1px;
    }}
    QFrame[role="panel_dark"] {{
        background-color: {c['panel']};
        border: none;
        border-radius: 12px;
    }}

    QLabel[role="page_title"] {{
        font-family: "{title}";
        font-size: {page_px}px;
        font-weight: {title_weight};
    }}
    QLabel[role="page_subtitle"] {{ color: {c['muted']}; }}
    QLabel[role="section_title"] {{
        font-family: "{title}";
        font-size: {section_px}px;
        font-weight: {title_weight};
    }}
    QLabel[role="card_title"] {{ font-size: 15px; font-weight: 700; }}
    QLabel[role="chart_title"] {{ font-size: 14px; font-weight: 700; }}
    QLabel[role="muted"] {{ color: {c['muted']}; }}
    QLabel[role="code"] {{ color: {c['faint']}; font-family: "{mono}"; font-size: 11px; }}
    QLabel[role="value"] {{ font-family: "{mono}"; font-weight: 700; }}
    QLabel[role="distance"] {{
        color: {c['blue']};
        font-family: "{mono}";
        font-size: 11px;
        font-weight: 700;
    }}
    QLabel[role="stat_value"] {{
        font-family: "{title}";
        font-size: {stat_px}px;
        font-weight: {title_weight};
    }}
    QLabel[role="stat_hint"] {{ font-size: 12px; font-weight: 700; }}
    QLabel[role="stat_hint"][tone="green"] {{ color: {c['green']}; }}
    QLabel[role="stat_hint"][tone="orange"] {{ color: {c['accent']}; }}
    QLabel[role="stat_hint"][tone="red"] {{ color: {c['red']}; }}
    QLabel[role="legend_dot"] {{ border-radius: 2px; }}
    QLabel[role="legend_dot"][tone="green"] {{ background-color: {c['green']}; }}
    QLabel[role="legend_dot"][tone="orange"] {{ background-color: {c['accent']}; }}
    QLabel[role="legend_dot"][tone="red"] {{ background-color: {c['red']}; }}
    QLabel[role="step_number"] {{
        color: {c['accent']};
        font-family: "{mono}";
        font-size: 12px;
        font-weight: 700;
    }}
    QLabel[role="step_title"] {{ font-size: 16px; font-weight: 700; }}
    QLabel[role="setting_title"] {{ font-size: 14px; font-weight: 700; }}
    QLabel[role="panel_label"] {{ color: {c['panel_muted']}; font-size: 12px; }}
    QLabel[role="panel_value"] {{
        color: #ffffff;
        font-family: "{title}";
        font-size: {stat_px - 4}px;
        font-weight: {title_weight};
    }}
    QLabel[role="error"] {{ color: {c['red']}; font-size: 12px; }}

    /* ---------- botões ---------- */
    QPushButton[variant="primary"] {{
        background-color: {c['accent']};
        color: {c['on_accent']};
        border: none;
        border-radius: 8px;
        padding: 0 18px;
        min-height: 36px;
        font-weight: 700;
    }}
    QPushButton[variant="primary"]:hover {{ background-color: {c['accent_hover']}; }}
    QPushButton[variant="primary"]:pressed {{ background-color: {c['accent_pressed']}; }}
    QPushButton[variant="dark"] {{
        background-color: {c['btn_dark']};
        color: {c['on_btn_dark']};
        border: none;
        border-radius: 8px;
        padding: 0 18px;
        min-height: 36px;
        font-weight: 700;
    }}
    QPushButton[variant="dark"]:hover {{ background-color: {c['btn_dark_hover']}; }}
    QPushButton[variant="dark"]:pressed {{ background-color: {c['btn_dark']}; }}

    /* ---------- campos de texto ---------- */
    QLineEdit[variant="field"] {{
        background-color: {c['input_bg']};
        color: {c['text']};
        border: 1px solid transparent;
        border-radius: 10px;
        padding: 0 14px;
        min-height: 42px;
        selection-background-color: {c['accent']};
    }}
    QLineEdit[variant="field"]:focus {{
        background-color: {c['surface']};
        border: 1px solid {c['accent']};
    }}

    /* ---------- tabelas ---------- */
    QTableWidget {{
        background: transparent;
        border: none;
        outline: none;
        color: {c['text']};
    }}
    QTableWidget::item {{ padding: 0 16px; border-bottom: 1px solid {c['border']}; }}
    QHeaderView {{ background: transparent; border: none; }}
    QHeaderView::section {{
        background: transparent;
        color: {c['muted']};
        border: none;
        border-bottom: 1px solid {c['border']};
        padding: 0 16px;
        font-size: 11px;
        font-weight: 700;
        text-align: left;
    }}
    QTableCornerButton::section {{ background: transparent; border: none; }}

    /* ---------- tela de login ---------- */
    #login_page {{ background-color: {c['bg']}; }}
    #login_brand {{ background-color: {c['brand']}; }}
    #login_brand_title {{
        color: #ffffff;
        font-family: "{title}";
        font-size: {page_px + 14}px;
        font-weight: {title_weight};
    }}
    #login_brand_text {{ color: #aab3c5; font-size: 15px; }}
    """


class ThemeManager(QObject):
    # emitido sempre que o tema muda (os widgets desenhados à mão se repintam)
    theme_changed = Signal(str)

    def __init__(self):
        super().__init__()
        self._settings = QSettings("ProjetoGasometro", "Gasometro")
        saved = self._settings.value("theme", "light")
        self._name = saved if saved in THEMES else "light"
        self._fonts = None

    @property
    def name(self):
        return self._name

    @property
    def is_dark(self):
        return self._name == "dark"

    @property
    def colors(self):
        return THEMES[self._name]

    def color(self, key):
        # aceita a chave da paleta ("accent") ou uma cor direta ("#ff0000")
        return self.colors.get(key, key)

    @property
    def fonts(self):
        # só pode ser resolvido depois que o QApplication existe
        if self._fonts is None:
            self._fonts = {
                "ui": _pick_font(UI_FONTS, "sans-serif"),
                "title": _pick_font(TITLE_FONTS, "sans-serif"),
                "mono": _pick_font(MONO_FONTS, "monospace"),
            }
        return self._fonts

    def apply(self):
        app = QApplication.instance()
        if app is not None:
            app.setStyleSheet(build_stylesheet(self.colors, self.fonts))

    def set_theme(self, name):
        if name not in THEMES or name == self._name:
            return
        self._name = name
        self._settings.setValue("theme", name)
        self.apply()
        self.theme_changed.emit(name)


# instância única usada pela aplicação inteira
theme = ThemeManager()
