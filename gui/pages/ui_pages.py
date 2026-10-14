# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pages.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

from gui.widgets.py_bar_chart import PyBarChart
from gui.widgets.py_botijao_card import PyBotijaoCard
from gui.widgets.py_donut_chart import PyDonutChart
from gui.widgets.py_ponto_card import PyPontoCard
from gui.widgets.py_stat_card import PyStatCard
from gui.widgets.py_table_widget import PyTableWidget
from gui.widgets.py_toggle import PyToggle

class Ui_application_pages(object):
    def setupUi(self, application_pages):
        if not application_pages.objectName():
            application_pages.setObjectName(u"application_pages")
        application_pages.resize(513, 395)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_layout_home = QVBoxLayout(self.page_1)
        self.page_layout_home.setSpacing(0)
        self.page_layout_home.setObjectName(u"page_layout_home")
        self.page_layout_home.setContentsMargins(0, 0, 0, 0)
        self.scroll_home = QScrollArea(self.page_1)
        self.scroll_home.setObjectName(u"scroll_home")
        self.scroll_home.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll_home.setWidgetResizable(True)
        self.scroll_contents_home = QWidget()
        self.scroll_contents_home.setObjectName(u"scroll_contents_home")
        self.scroll_contents_home.setGeometry(QRect(0, 0, 900, 700))
        self.content_layout_home = QVBoxLayout(self.scroll_contents_home)
        self.content_layout_home.setSpacing(18)
        self.content_layout_home.setObjectName(u"content_layout_home")
        self.content_layout_home.setContentsMargins(28, 24, 28, 28)
        self.header_texts_home = QVBoxLayout()
        self.header_texts_home.setSpacing(0)
        self.header_texts_home.setObjectName(u"header_texts_home")
        self.lbl_title_home = QLabel(self.scroll_contents_home)
        self.lbl_title_home.setObjectName(u"lbl_title_home")

        self.header_texts_home.addWidget(self.lbl_title_home)

        self.lbl_home_date = QLabel(self.scroll_contents_home)
        self.lbl_home_date.setObjectName(u"lbl_home_date")
        self.lbl_home_date.setMinimumSize(QSize(0, 20))

        self.header_texts_home.addWidget(self.lbl_home_date)


        self.content_layout_home.addLayout(self.header_texts_home)

        self.stats_row = QHBoxLayout()
        self.stats_row.setSpacing(16)
        self.stats_row.setObjectName(u"stats_row")
        self.card_total = PyStatCard(self.scroll_contents_home)
        self.card_total.setObjectName(u"card_total")

        self.stats_row.addWidget(self.card_total)

        self.card_nivel = PyStatCard(self.scroll_contents_home)
        self.card_nivel.setObjectName(u"card_nivel")

        self.stats_row.addWidget(self.card_nivel)

        self.card_alertas_ativos = PyStatCard(self.scroll_contents_home)
        self.card_alertas_ativos.setObjectName(u"card_alertas_ativos")

        self.stats_row.addWidget(self.card_alertas_ativos)

        self.card_economia = PyStatCard(self.scroll_contents_home)
        self.card_economia.setObjectName(u"card_economia")

        self.stats_row.addWidget(self.card_economia)


        self.content_layout_home.addLayout(self.stats_row)

        self.charts_row = QHBoxLayout()
        self.charts_row.setSpacing(16)
        self.charts_row.setObjectName(u"charts_row")
        self.card_status = QFrame(self.scroll_contents_home)
        self.card_status.setObjectName(u"card_status")
        self.card_status_layout = QVBoxLayout(self.card_status)
        self.card_status_layout.setSpacing(14)
        self.card_status_layout.setObjectName(u"card_status_layout")
        self.card_status_layout.setContentsMargins(22, 20, 22, 22)
        self.lbl_status_title = QLabel(self.card_status)
        self.lbl_status_title.setObjectName(u"lbl_status_title")

        self.card_status_layout.addWidget(self.lbl_status_title)

        self.status_row = QHBoxLayout()
        self.status_row.setSpacing(32)
        self.status_row.setObjectName(u"status_row")
        self.donut_status = PyDonutChart(self.card_status)
        self.donut_status.setObjectName(u"donut_status")
        self.donut_status.setMinimumSize(QSize(150, 150))
        self.donut_status.setMaximumSize(QSize(150, 150))

        self.status_row.addWidget(self.donut_status, 0, Qt.AlignmentFlag.AlignVCenter)

        self.legend_box = QWidget(self.card_status)
        self.legend_box.setObjectName(u"legend_box")
        self.legend_layout = QVBoxLayout(self.legend_box)
        self.legend_layout.setSpacing(10)
        self.legend_layout.setObjectName(u"legend_layout")
        self.legend_layout.setContentsMargins(0, 0, 0, 0)
        self.legend_row_cheio = QHBoxLayout()
        self.legend_row_cheio.setSpacing(8)
        self.legend_row_cheio.setObjectName(u"legend_row_cheio")
        self.legend_dot_cheio = QLabel(self.legend_box)
        self.legend_dot_cheio.setObjectName(u"legend_dot_cheio")
        self.legend_dot_cheio.setMinimumSize(QSize(10, 10))
        self.legend_dot_cheio.setMaximumSize(QSize(10, 10))

        self.legend_row_cheio.addWidget(self.legend_dot_cheio, 0, Qt.AlignmentFlag.AlignVCenter)

        self.legend_text_cheio = QLabel(self.legend_box)
        self.legend_text_cheio.setObjectName(u"legend_text_cheio")

        self.legend_row_cheio.addWidget(self.legend_text_cheio)

        self.lbl_count_cheio = QLabel(self.legend_box)
        self.lbl_count_cheio.setObjectName(u"lbl_count_cheio")

        self.legend_row_cheio.addWidget(self.lbl_count_cheio)

        self.legend_spacer_cheio = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.legend_row_cheio.addItem(self.legend_spacer_cheio)


        self.legend_layout.addLayout(self.legend_row_cheio)

        self.legend_row_baixo = QHBoxLayout()
        self.legend_row_baixo.setSpacing(8)
        self.legend_row_baixo.setObjectName(u"legend_row_baixo")
        self.legend_dot_baixo = QLabel(self.legend_box)
        self.legend_dot_baixo.setObjectName(u"legend_dot_baixo")
        self.legend_dot_baixo.setMinimumSize(QSize(10, 10))
        self.legend_dot_baixo.setMaximumSize(QSize(10, 10))

        self.legend_row_baixo.addWidget(self.legend_dot_baixo, 0, Qt.AlignmentFlag.AlignVCenter)

        self.legend_text_baixo = QLabel(self.legend_box)
        self.legend_text_baixo.setObjectName(u"legend_text_baixo")

        self.legend_row_baixo.addWidget(self.legend_text_baixo)

        self.lbl_count_baixo = QLabel(self.legend_box)
        self.lbl_count_baixo.setObjectName(u"lbl_count_baixo")

        self.legend_row_baixo.addWidget(self.lbl_count_baixo)

        self.legend_spacer_baixo = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.legend_row_baixo.addItem(self.legend_spacer_baixo)


        self.legend_layout.addLayout(self.legend_row_baixo)

        self.legend_row_critico = QHBoxLayout()
        self.legend_row_critico.setSpacing(8)
        self.legend_row_critico.setObjectName(u"legend_row_critico")
        self.legend_dot_critico = QLabel(self.legend_box)
        self.legend_dot_critico.setObjectName(u"legend_dot_critico")
        self.legend_dot_critico.setMinimumSize(QSize(10, 10))
        self.legend_dot_critico.setMaximumSize(QSize(10, 10))

        self.legend_row_critico.addWidget(self.legend_dot_critico, 0, Qt.AlignmentFlag.AlignVCenter)

        self.legend_text_critico = QLabel(self.legend_box)
        self.legend_text_critico.setObjectName(u"legend_text_critico")

        self.legend_row_critico.addWidget(self.legend_text_critico)

        self.lbl_count_critico = QLabel(self.legend_box)
        self.lbl_count_critico.setObjectName(u"lbl_count_critico")

        self.legend_row_critico.addWidget(self.lbl_count_critico)

        self.legend_spacer_critico = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.legend_row_critico.addItem(self.legend_spacer_critico)


        self.legend_layout.addLayout(self.legend_row_critico)


        self.status_row.addWidget(self.legend_box, 0, Qt.AlignmentFlag.AlignVCenter)

        self.status_spacer = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.status_row.addItem(self.status_spacer)


        self.card_status_layout.addLayout(self.status_row)


        self.charts_row.addWidget(self.card_status)

        self.card_consumo = QFrame(self.scroll_contents_home)
        self.card_consumo.setObjectName(u"card_consumo")
        self.card_consumo_layout = QVBoxLayout(self.card_consumo)
        self.card_consumo_layout.setSpacing(14)
        self.card_consumo_layout.setObjectName(u"card_consumo_layout")
        self.card_consumo_layout.setContentsMargins(22, 20, 22, 18)
        self.lbl_consumo_title = QLabel(self.card_consumo)
        self.lbl_consumo_title.setObjectName(u"lbl_consumo_title")

        self.card_consumo_layout.addWidget(self.lbl_consumo_title)

        self.chart_consumo = PyBarChart(self.card_consumo)
        self.chart_consumo.setObjectName(u"chart_consumo")
        self.chart_consumo.setMinimumSize(QSize(0, 170))

        self.card_consumo_layout.addWidget(self.chart_consumo)


        self.charts_row.addWidget(self.card_consumo)

        self.charts_row.setStretch(0, 1)
        self.charts_row.setStretch(1, 1)

        self.content_layout_home.addLayout(self.charts_row)

        self.card_table_home = QFrame(self.scroll_contents_home)
        self.card_table_home.setObjectName(u"card_table_home")
        self.card_table_home_layout = QVBoxLayout(self.card_table_home)
        self.card_table_home_layout.setSpacing(0)
        self.card_table_home_layout.setObjectName(u"card_table_home_layout")
        self.card_table_home_layout.setContentsMargins(0, 0, 0, 0)
        self.table_home = PyTableWidget(self.card_table_home)
        if (self.table_home.columnCount() < 6):
            self.table_home.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_home.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_home.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_home.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_home.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_home.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_home.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        if (self.table_home.rowCount() < 4):
            self.table_home.setRowCount(4)
        self.table_home.setObjectName(u"table_home")
        self.table_home.horizontalHeader().setStretchLastSection(True)

        self.card_table_home_layout.addWidget(self.table_home)


        self.content_layout_home.addWidget(self.card_table_home)

        self.bottom_row = QHBoxLayout()
        self.bottom_row.setSpacing(16)
        self.bottom_row.setObjectName(u"bottom_row")
        self.card_alertas = QFrame(self.scroll_contents_home)
        self.card_alertas.setObjectName(u"card_alertas")
        self.card_alertas_layout = QVBoxLayout(self.card_alertas)
        self.card_alertas_layout.setSpacing(14)
        self.card_alertas_layout.setObjectName(u"card_alertas_layout")
        self.card_alertas_layout.setContentsMargins(22, 20, 22, 22)
        self.lbl_alertas_title = QLabel(self.card_alertas)
        self.lbl_alertas_title.setObjectName(u"lbl_alertas_title")

        self.card_alertas_layout.addWidget(self.lbl_alertas_title)

        self.alerts_container = QWidget(self.card_alertas)
        self.alerts_container.setObjectName(u"alerts_container")
        self.alerts_container.setMinimumSize(QSize(0, 96))
        self.alerts_layout = QVBoxLayout(self.alerts_container)
        self.alerts_layout.setSpacing(10)
        self.alerts_layout.setObjectName(u"alerts_layout")
        self.alerts_layout.setContentsMargins(0, 0, 0, 0)

        self.card_alertas_layout.addWidget(self.alerts_container)

        self.alertas_spacer = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.card_alertas_layout.addItem(self.alertas_spacer)


        self.bottom_row.addWidget(self.card_alertas)

        self.card_financeiro = QFrame(self.scroll_contents_home)
        self.card_financeiro.setObjectName(u"card_financeiro")
        self.card_financeiro_layout = QVBoxLayout(self.card_financeiro)
        self.card_financeiro_layout.setSpacing(14)
        self.card_financeiro_layout.setObjectName(u"card_financeiro_layout")
        self.card_financeiro_layout.setContentsMargins(22, 20, 22, 22)
        self.lbl_financeiro_title = QLabel(self.card_financeiro)
        self.lbl_financeiro_title.setObjectName(u"lbl_financeiro_title")

        self.card_financeiro_layout.addWidget(self.lbl_financeiro_title)

        self.panel_financeiro = QFrame(self.card_financeiro)
        self.panel_financeiro.setObjectName(u"panel_financeiro")
        self.panel_financeiro.setMinimumSize(QSize(0, 96))
        self.panel_financeiro_layout = QVBoxLayout(self.panel_financeiro)
        self.panel_financeiro_layout.setSpacing(4)
        self.panel_financeiro_layout.setObjectName(u"panel_financeiro_layout")
        self.panel_financeiro_layout.setContentsMargins(22, 18, 22, 18)
        self.lbl_fin_total_caption = QLabel(self.panel_financeiro)
        self.lbl_fin_total_caption.setObjectName(u"lbl_fin_total_caption")

        self.panel_financeiro_layout.addWidget(self.lbl_fin_total_caption)

        self.lbl_fin_total = QLabel(self.panel_financeiro)
        self.lbl_fin_total.setObjectName(u"lbl_fin_total")

        self.panel_financeiro_layout.addWidget(self.lbl_fin_total)

        self.fin_row = QHBoxLayout()
        self.fin_row.setSpacing(40)
        self.fin_row.setObjectName(u"fin_row")
        self.fin_pair_economia = QVBoxLayout()
        self.fin_pair_economia.setSpacing(0)
        self.fin_pair_economia.setObjectName(u"fin_pair_economia")
        self.lbl_fin_economia_caption = QLabel(self.panel_financeiro)
        self.lbl_fin_economia_caption.setObjectName(u"lbl_fin_economia_caption")

        self.fin_pair_economia.addWidget(self.lbl_fin_economia_caption)

        self.lbl_fin_economia = QLabel(self.panel_financeiro)
        self.lbl_fin_economia.setObjectName(u"lbl_fin_economia")

        self.fin_pair_economia.addWidget(self.lbl_fin_economia)


        self.fin_row.addLayout(self.fin_pair_economia)

        self.fin_pair_trocas = QVBoxLayout()
        self.fin_pair_trocas.setSpacing(0)
        self.fin_pair_trocas.setObjectName(u"fin_pair_trocas")
        self.lbl_fin_trocas_caption = QLabel(self.panel_financeiro)
        self.lbl_fin_trocas_caption.setObjectName(u"lbl_fin_trocas_caption")

        self.fin_pair_trocas.addWidget(self.lbl_fin_trocas_caption)

        self.lbl_fin_trocas = QLabel(self.panel_financeiro)
        self.lbl_fin_trocas.setObjectName(u"lbl_fin_trocas")

        self.fin_pair_trocas.addWidget(self.lbl_fin_trocas)


        self.fin_row.addLayout(self.fin_pair_trocas)

        self.fin_spacer = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.fin_row.addItem(self.fin_spacer)


        self.panel_financeiro_layout.addLayout(self.fin_row)


        self.card_financeiro_layout.addWidget(self.panel_financeiro)


        self.bottom_row.addWidget(self.card_financeiro)

        self.bottom_row.setStretch(0, 1)
        self.bottom_row.setStretch(1, 1)

        self.content_layout_home.addLayout(self.bottom_row)

        self.spacer_home = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.content_layout_home.addItem(self.spacer_home)

        self.scroll_home.setWidget(self.scroll_contents_home)

        self.page_layout_home.addWidget(self.scroll_home)

        application_pages.addWidget(self.page_1)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_layout_botijoes = QVBoxLayout(self.page_3)
        self.page_layout_botijoes.setSpacing(0)
        self.page_layout_botijoes.setObjectName(u"page_layout_botijoes")
        self.page_layout_botijoes.setContentsMargins(0, 0, 0, 0)
        self.scroll_botijoes = QScrollArea(self.page_3)
        self.scroll_botijoes.setObjectName(u"scroll_botijoes")
        self.scroll_botijoes.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll_botijoes.setWidgetResizable(True)
        self.scroll_contents_botijoes = QWidget()
        self.scroll_contents_botijoes.setObjectName(u"scroll_contents_botijoes")
        self.scroll_contents_botijoes.setGeometry(QRect(0, 0, 900, 700))
        self.content_layout_botijoes = QVBoxLayout(self.scroll_contents_botijoes)
        self.content_layout_botijoes.setSpacing(18)
        self.content_layout_botijoes.setObjectName(u"content_layout_botijoes")
        self.content_layout_botijoes.setContentsMargins(28, 24, 28, 28)
        self.header_row_botijoes = QHBoxLayout()
        self.header_row_botijoes.setObjectName(u"header_row_botijoes")
        self.header_texts_botijoes = QVBoxLayout()
        self.header_texts_botijoes.setSpacing(0)
        self.header_texts_botijoes.setObjectName(u"header_texts_botijoes")
        self.lbl_title_botijoes = QLabel(self.scroll_contents_botijoes)
        self.lbl_title_botijoes.setObjectName(u"lbl_title_botijoes")

        self.header_texts_botijoes.addWidget(self.lbl_title_botijoes)

        self.lbl_botijoes_count = QLabel(self.scroll_contents_botijoes)
        self.lbl_botijoes_count.setObjectName(u"lbl_botijoes_count")
        self.lbl_botijoes_count.setMinimumSize(QSize(0, 20))

        self.header_texts_botijoes.addWidget(self.lbl_botijoes_count)


        self.header_row_botijoes.addLayout(self.header_texts_botijoes)

        self.header_spacer_botijoes = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.header_row_botijoes.addItem(self.header_spacer_botijoes)

        self.btn_conectar_botijao = QPushButton(self.scroll_contents_botijoes)
        self.btn_conectar_botijao.setObjectName(u"btn_conectar_botijao")

        self.header_row_botijoes.addWidget(self.btn_conectar_botijao, 0, Qt.AlignmentFlag.AlignTop)


        self.content_layout_botijoes.addLayout(self.header_row_botijoes)

        self.botijoes_grid = QGridLayout()
        self.botijoes_grid.setObjectName(u"botijoes_grid")
        self.botijoes_grid.setHorizontalSpacing(16)
        self.botijoes_grid.setVerticalSpacing(16)
        self.card_botijao_1 = PyBotijaoCard(self.scroll_contents_botijoes)
        self.card_botijao_1.setObjectName(u"card_botijao_1")

        self.botijoes_grid.addWidget(self.card_botijao_1, 0, 0, 1, 1)

        self.card_botijao_2 = PyBotijaoCard(self.scroll_contents_botijoes)
        self.card_botijao_2.setObjectName(u"card_botijao_2")

        self.botijoes_grid.addWidget(self.card_botijao_2, 0, 1, 1, 1)

        self.card_botijao_3 = PyBotijaoCard(self.scroll_contents_botijoes)
        self.card_botijao_3.setObjectName(u"card_botijao_3")

        self.botijoes_grid.addWidget(self.card_botijao_3, 1, 0, 1, 1)

        self.card_botijao_4 = PyBotijaoCard(self.scroll_contents_botijoes)
        self.card_botijao_4.setObjectName(u"card_botijao_4")

        self.botijoes_grid.addWidget(self.card_botijao_4, 1, 1, 1, 1)

        self.botijoes_grid.setColumnStretch(0, 1)
        self.botijoes_grid.setColumnStretch(1, 1)

        self.content_layout_botijoes.addLayout(self.botijoes_grid)

        self.spacer_botijoes = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.content_layout_botijoes.addItem(self.spacer_botijoes)

        self.scroll_botijoes.setWidget(self.scroll_contents_botijoes)

        self.page_layout_botijoes.addWidget(self.scroll_botijoes)

        application_pages.addWidget(self.page_3)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_layout_config = QVBoxLayout(self.page_2)
        self.page_layout_config.setSpacing(0)
        self.page_layout_config.setObjectName(u"page_layout_config")
        self.page_layout_config.setContentsMargins(0, 0, 0, 0)
        self.scroll_config = QScrollArea(self.page_2)
        self.scroll_config.setObjectName(u"scroll_config")
        self.scroll_config.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll_config.setWidgetResizable(True)
        self.scroll_contents_config = QWidget()
        self.scroll_contents_config.setObjectName(u"scroll_contents_config")
        self.scroll_contents_config.setGeometry(QRect(0, 0, 900, 700))
        self.content_layout_config = QVBoxLayout(self.scroll_contents_config)
        self.content_layout_config.setSpacing(18)
        self.content_layout_config.setObjectName(u"content_layout_config")
        self.content_layout_config.setContentsMargins(28, 24, 28, 28)
        self.header_texts_config = QVBoxLayout()
        self.header_texts_config.setSpacing(0)
        self.header_texts_config.setObjectName(u"header_texts_config")
        self.lbl_title_config = QLabel(self.scroll_contents_config)
        self.lbl_title_config.setObjectName(u"lbl_title_config")

        self.header_texts_config.addWidget(self.lbl_title_config)

        self.lbl_config_subtitle = QLabel(self.scroll_contents_config)
        self.lbl_config_subtitle.setObjectName(u"lbl_config_subtitle")
        self.lbl_config_subtitle.setMinimumSize(QSize(0, 20))

        self.header_texts_config.addWidget(self.lbl_config_subtitle)


        self.content_layout_config.addLayout(self.header_texts_config)

        self.card_aparencia = QFrame(self.scroll_contents_config)
        self.card_aparencia.setObjectName(u"card_aparencia")
        self.card_aparencia_layout = QVBoxLayout(self.card_aparencia)
        self.card_aparencia_layout.setSpacing(14)
        self.card_aparencia_layout.setObjectName(u"card_aparencia_layout")
        self.card_aparencia_layout.setContentsMargins(22, 20, 22, 20)
        self.lbl_aparencia_title = QLabel(self.card_aparencia)
        self.lbl_aparencia_title.setObjectName(u"lbl_aparencia_title")

        self.card_aparencia_layout.addWidget(self.lbl_aparencia_title)

        self.divider_aparencia = QFrame(self.card_aparencia)
        self.divider_aparencia.setObjectName(u"divider_aparencia")

        self.card_aparencia_layout.addWidget(self.divider_aparencia)

        self.theme_row = QHBoxLayout()
        self.theme_row.setSpacing(24)
        self.theme_row.setObjectName(u"theme_row")
        self.theme_texts = QVBoxLayout()
        self.theme_texts.setSpacing(2)
        self.theme_texts.setObjectName(u"theme_texts")
        self.lbl_theme_title = QLabel(self.card_aparencia)
        self.lbl_theme_title.setObjectName(u"lbl_theme_title")

        self.theme_texts.addWidget(self.lbl_theme_title)

        self.lbl_theme_desc = QLabel(self.card_aparencia)
        self.lbl_theme_desc.setObjectName(u"lbl_theme_desc")
        self.lbl_theme_desc.setWordWrap(True)

        self.theme_texts.addWidget(self.lbl_theme_desc)


        self.theme_row.addLayout(self.theme_texts)

        self.toggle_dark_theme = PyToggle(self.card_aparencia)
        self.toggle_dark_theme.setObjectName(u"toggle_dark_theme")

        self.theme_row.addWidget(self.toggle_dark_theme, 0, Qt.AlignmentFlag.AlignVCenter)

        self.theme_row.setStretch(0, 1)

        self.card_aparencia_layout.addLayout(self.theme_row)


        self.content_layout_config.addWidget(self.card_aparencia)

        self.spacer_config = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.content_layout_config.addItem(self.spacer_config)

        self.scroll_config.setWidget(self.scroll_contents_config)

        self.page_layout_config.addWidget(self.scroll_config)

        application_pages.addWidget(self.page_2)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_layout_pontos = QVBoxLayout(self.page_4)
        self.page_layout_pontos.setSpacing(0)
        self.page_layout_pontos.setObjectName(u"page_layout_pontos")
        self.page_layout_pontos.setContentsMargins(0, 0, 0, 0)
        self.scroll_pontos = QScrollArea(self.page_4)
        self.scroll_pontos.setObjectName(u"scroll_pontos")
        self.scroll_pontos.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll_pontos.setWidgetResizable(True)
        self.scroll_contents_pontos = QWidget()
        self.scroll_contents_pontos.setObjectName(u"scroll_contents_pontos")
        self.scroll_contents_pontos.setGeometry(QRect(0, 0, 900, 700))
        self.content_layout_pontos = QVBoxLayout(self.scroll_contents_pontos)
        self.content_layout_pontos.setSpacing(16)
        self.content_layout_pontos.setObjectName(u"content_layout_pontos")
        self.content_layout_pontos.setContentsMargins(28, 24, 28, 28)
        self.header_texts_pontos = QVBoxLayout()
        self.header_texts_pontos.setSpacing(0)
        self.header_texts_pontos.setObjectName(u"header_texts_pontos")
        self.lbl_title_pontos = QLabel(self.scroll_contents_pontos)
        self.lbl_title_pontos.setObjectName(u"lbl_title_pontos")

        self.header_texts_pontos.addWidget(self.lbl_title_pontos)

        self.lbl_pontos_local = QLabel(self.scroll_contents_pontos)
        self.lbl_pontos_local.setObjectName(u"lbl_pontos_local")
        self.lbl_pontos_local.setMinimumSize(QSize(0, 20))

        self.header_texts_pontos.addWidget(self.lbl_pontos_local)


        self.content_layout_pontos.addLayout(self.header_texts_pontos)

        self.pontos_grid = QGridLayout()
        self.pontos_grid.setObjectName(u"pontos_grid")
        self.pontos_grid.setHorizontalSpacing(16)
        self.pontos_grid.setVerticalSpacing(16)
        self.card_ponto_1 = PyPontoCard(self.scroll_contents_pontos)
        self.card_ponto_1.setObjectName(u"card_ponto_1")

        self.pontos_grid.addWidget(self.card_ponto_1, 0, 0, 1, 1)

        self.card_ponto_2 = PyPontoCard(self.scroll_contents_pontos)
        self.card_ponto_2.setObjectName(u"card_ponto_2")

        self.pontos_grid.addWidget(self.card_ponto_2, 0, 1, 1, 1)

        self.card_ponto_3 = PyPontoCard(self.scroll_contents_pontos)
        self.card_ponto_3.setObjectName(u"card_ponto_3")

        self.pontos_grid.addWidget(self.card_ponto_3, 0, 2, 1, 1)

        self.card_ponto_4 = PyPontoCard(self.scroll_contents_pontos)
        self.card_ponto_4.setObjectName(u"card_ponto_4")

        self.pontos_grid.addWidget(self.card_ponto_4, 1, 0, 1, 1)

        self.card_ponto_5 = PyPontoCard(self.scroll_contents_pontos)
        self.card_ponto_5.setObjectName(u"card_ponto_5")

        self.pontos_grid.addWidget(self.card_ponto_5, 1, 1, 1, 1)

        self.card_ponto_6 = PyPontoCard(self.scroll_contents_pontos)
        self.card_ponto_6.setObjectName(u"card_ponto_6")

        self.pontos_grid.addWidget(self.card_ponto_6, 1, 2, 1, 1)

        self.pontos_grid.setColumnStretch(0, 1)
        self.pontos_grid.setColumnStretch(1, 1)
        self.pontos_grid.setColumnStretch(2, 1)

        self.content_layout_pontos.addLayout(self.pontos_grid)

        self.lbl_como_trocar = QLabel(self.scroll_contents_pontos)
        self.lbl_como_trocar.setObjectName(u"lbl_como_trocar")

        self.content_layout_pontos.addWidget(self.lbl_como_trocar)

        self.steps_row = QHBoxLayout()
        self.steps_row.setSpacing(16)
        self.steps_row.setObjectName(u"steps_row")
        self.card_step_1 = QFrame(self.scroll_contents_pontos)
        self.card_step_1.setObjectName(u"card_step_1")
        self.card_step_1_layout = QVBoxLayout(self.card_step_1)
        self.card_step_1_layout.setSpacing(6)
        self.card_step_1_layout.setObjectName(u"card_step_1_layout")
        self.card_step_1_layout.setContentsMargins(22, 20, 22, 20)
        self.lbl_step_1_number = QLabel(self.card_step_1)
        self.lbl_step_1_number.setObjectName(u"lbl_step_1_number")

        self.card_step_1_layout.addWidget(self.lbl_step_1_number)

        self.lbl_step_1_title = QLabel(self.card_step_1)
        self.lbl_step_1_title.setObjectName(u"lbl_step_1_title")

        self.card_step_1_layout.addWidget(self.lbl_step_1_title)

        self.lbl_step_1_text = QLabel(self.card_step_1)
        self.lbl_step_1_text.setObjectName(u"lbl_step_1_text")
        self.lbl_step_1_text.setWordWrap(True)

        self.card_step_1_layout.addWidget(self.lbl_step_1_text)


        self.steps_row.addWidget(self.card_step_1)

        self.card_step_2 = QFrame(self.scroll_contents_pontos)
        self.card_step_2.setObjectName(u"card_step_2")
        self.card_step_2_layout = QVBoxLayout(self.card_step_2)
        self.card_step_2_layout.setSpacing(6)
        self.card_step_2_layout.setObjectName(u"card_step_2_layout")
        self.card_step_2_layout.setContentsMargins(22, 20, 22, 20)
        self.lbl_step_2_number = QLabel(self.card_step_2)
        self.lbl_step_2_number.setObjectName(u"lbl_step_2_number")

        self.card_step_2_layout.addWidget(self.lbl_step_2_number)

        self.lbl_step_2_title = QLabel(self.card_step_2)
        self.lbl_step_2_title.setObjectName(u"lbl_step_2_title")

        self.card_step_2_layout.addWidget(self.lbl_step_2_title)

        self.lbl_step_2_text = QLabel(self.card_step_2)
        self.lbl_step_2_text.setObjectName(u"lbl_step_2_text")
        self.lbl_step_2_text.setWordWrap(True)

        self.card_step_2_layout.addWidget(self.lbl_step_2_text)


        self.steps_row.addWidget(self.card_step_2)

        self.card_step_3 = QFrame(self.scroll_contents_pontos)
        self.card_step_3.setObjectName(u"card_step_3")
        self.card_step_3_layout = QVBoxLayout(self.card_step_3)
        self.card_step_3_layout.setSpacing(6)
        self.card_step_3_layout.setObjectName(u"card_step_3_layout")
        self.card_step_3_layout.setContentsMargins(22, 20, 22, 20)
        self.lbl_step_3_number = QLabel(self.card_step_3)
        self.lbl_step_3_number.setObjectName(u"lbl_step_3_number")

        self.card_step_3_layout.addWidget(self.lbl_step_3_number)

        self.lbl_step_3_title = QLabel(self.card_step_3)
        self.lbl_step_3_title.setObjectName(u"lbl_step_3_title")

        self.card_step_3_layout.addWidget(self.lbl_step_3_title)

        self.lbl_step_3_text = QLabel(self.card_step_3)
        self.lbl_step_3_text.setObjectName(u"lbl_step_3_text")
        self.lbl_step_3_text.setWordWrap(True)

        self.card_step_3_layout.addWidget(self.lbl_step_3_text)


        self.steps_row.addWidget(self.card_step_3)

        self.steps_row.setStretch(0, 1)
        self.steps_row.setStretch(1, 1)
        self.steps_row.setStretch(2, 1)

        self.content_layout_pontos.addLayout(self.steps_row)

        self.spacer_pontos = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.content_layout_pontos.addItem(self.spacer_pontos)

        self.scroll_pontos.setWidget(self.scroll_contents_pontos)

        self.page_layout_pontos.addWidget(self.scroll_pontos)

        application_pages.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.page_layout_historico = QVBoxLayout(self.page_5)
        self.page_layout_historico.setSpacing(0)
        self.page_layout_historico.setObjectName(u"page_layout_historico")
        self.page_layout_historico.setContentsMargins(0, 0, 0, 0)
        self.scroll_historico = QScrollArea(self.page_5)
        self.scroll_historico.setObjectName(u"scroll_historico")
        self.scroll_historico.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll_historico.setWidgetResizable(True)
        self.scroll_contents_historico = QWidget()
        self.scroll_contents_historico.setObjectName(u"scroll_contents_historico")
        self.scroll_contents_historico.setGeometry(QRect(0, 0, 900, 700))
        self.content_layout_historico = QVBoxLayout(self.scroll_contents_historico)
        self.content_layout_historico.setSpacing(18)
        self.content_layout_historico.setObjectName(u"content_layout_historico")
        self.content_layout_historico.setContentsMargins(28, 24, 28, 28)
        self.header_texts_historico = QVBoxLayout()
        self.header_texts_historico.setSpacing(0)
        self.header_texts_historico.setObjectName(u"header_texts_historico")
        self.lbl_title_historico = QLabel(self.scroll_contents_historico)
        self.lbl_title_historico.setObjectName(u"lbl_title_historico")

        self.header_texts_historico.addWidget(self.lbl_title_historico)

        self.lbl_historico_subtitle = QLabel(self.scroll_contents_historico)
        self.lbl_historico_subtitle.setObjectName(u"lbl_historico_subtitle")
        self.lbl_historico_subtitle.setMinimumSize(QSize(0, 20))

        self.header_texts_historico.addWidget(self.lbl_historico_subtitle)


        self.content_layout_historico.addLayout(self.header_texts_historico)

        self.card_historico_chart = QFrame(self.scroll_contents_historico)
        self.card_historico_chart.setObjectName(u"card_historico_chart")
        self.card_historico_chart_layout = QVBoxLayout(self.card_historico_chart)
        self.card_historico_chart_layout.setSpacing(14)
        self.card_historico_chart_layout.setObjectName(u"card_historico_chart_layout")
        self.card_historico_chart_layout.setContentsMargins(22, 20, 22, 18)
        self.lbl_historico_chart_title = QLabel(self.card_historico_chart)
        self.lbl_historico_chart_title.setObjectName(u"lbl_historico_chart_title")

        self.card_historico_chart_layout.addWidget(self.lbl_historico_chart_title)

        self.chart_historico = PyBarChart(self.card_historico_chart)
        self.chart_historico.setObjectName(u"chart_historico")
        self.chart_historico.setMinimumSize(QSize(0, 190))

        self.card_historico_chart_layout.addWidget(self.chart_historico)


        self.content_layout_historico.addWidget(self.card_historico_chart)

        self.card_table_historico = QFrame(self.scroll_contents_historico)
        self.card_table_historico.setObjectName(u"card_table_historico")
        self.card_table_historico_layout = QVBoxLayout(self.card_table_historico)
        self.card_table_historico_layout.setSpacing(0)
        self.card_table_historico_layout.setObjectName(u"card_table_historico_layout")
        self.card_table_historico_layout.setContentsMargins(0, 0, 0, 0)
        self.table_historico = PyTableWidget(self.card_table_historico)
        if (self.table_historico.columnCount() < 4):
            self.table_historico.setColumnCount(4)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_historico.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_historico.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_historico.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table_historico.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        if (self.table_historico.rowCount() < 4):
            self.table_historico.setRowCount(4)
        self.table_historico.setObjectName(u"table_historico")
        self.table_historico.horizontalHeader().setStretchLastSection(True)

        self.card_table_historico_layout.addWidget(self.table_historico)


        self.content_layout_historico.addWidget(self.card_table_historico)

        self.spacer_historico = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.content_layout_historico.addItem(self.spacer_historico)

        self.scroll_historico.setWidget(self.scroll_contents_historico)

        self.page_layout_historico.addWidget(self.scroll_historico)

        application_pages.addWidget(self.page_5)

        self.retranslateUi(application_pages)

        application_pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(application_pages)
    # setupUi

    def retranslateUi(self, application_pages):
        application_pages.setWindowTitle(QCoreApplication.translate("application_pages", u"StackedWidget", None))
        self.lbl_title_home.setText(QCoreApplication.translate("application_pages", u"VIS\u00c3O GERAL", None))
        self.lbl_title_home.setProperty(u"role", QCoreApplication.translate("application_pages", u"page_title", None))
        self.lbl_home_date.setText("")
        self.lbl_home_date.setProperty(u"role", QCoreApplication.translate("application_pages", u"page_subtitle", None))
        self.card_total.setProperty(u"title", QCoreApplication.translate("application_pages", u"Total de botij\u00f5es", None))
        self.card_total.setProperty(u"icon", QCoreApplication.translate("application_pages", u"icon_bottle.svg", None))
        self.card_total.setProperty(u"tone", QCoreApplication.translate("application_pages", u"blue", None))
        self.card_nivel.setProperty(u"title", QCoreApplication.translate("application_pages", u"N\u00edvel m\u00e9dio", None))
        self.card_nivel.setProperty(u"icon", QCoreApplication.translate("application_pages", u"icon_gauge.svg", None))
        self.card_nivel.setProperty(u"tone", QCoreApplication.translate("application_pages", u"green", None))
        self.card_alertas_ativos.setProperty(u"title", QCoreApplication.translate("application_pages", u"Alertas ativos", None))
        self.card_alertas_ativos.setProperty(u"icon", QCoreApplication.translate("application_pages", u"icon_bell.svg", None))
        self.card_alertas_ativos.setProperty(u"tone", QCoreApplication.translate("application_pages", u"red", None))
        self.card_economia.setProperty(u"title", QCoreApplication.translate("application_pages", u"Economia no m\u00eas", None))
        self.card_economia.setProperty(u"icon", QCoreApplication.translate("application_pages", u"icon_chart.svg", None))
        self.card_economia.setProperty(u"tone", QCoreApplication.translate("application_pages", u"accent", None))
        self.card_status.setProperty(u"role", QCoreApplication.translate("application_pages", u"card", None))
        self.lbl_status_title.setText(QCoreApplication.translate("application_pages", u"Status dos botij\u00f5es", None))
        self.lbl_status_title.setProperty(u"role", QCoreApplication.translate("application_pages", u"chart_title", None))
        self.legend_dot_cheio.setText("")
        self.legend_dot_cheio.setProperty(u"role", QCoreApplication.translate("application_pages", u"legend_dot", None))
        self.legend_dot_cheio.setProperty(u"tone", QCoreApplication.translate("application_pages", u"green", None))
        self.legend_text_cheio.setText(QCoreApplication.translate("application_pages", u"Cheio \u2014", None))
        self.legend_text_cheio.setProperty(u"role", QCoreApplication.translate("application_pages", u"muted", None))
        self.lbl_count_cheio.setText("")
        self.lbl_count_cheio.setProperty(u"role", QCoreApplication.translate("application_pages", u"muted", None))
        self.legend_dot_baixo.setText("")
        self.legend_dot_baixo.setProperty(u"role", QCoreApplication.translate("application_pages", u"legend_dot", None))
        self.legend_dot_baixo.setProperty(u"tone", QCoreApplication.translate("application_pages", u"orange", None))
        self.legend_text_baixo.setText(QCoreApplication.translate("application_pages", u"Baixo \u2014", None))
        self.legend_text_baixo.setProperty(u"role", QCoreApplication.translate("application_pages", u"muted", None))
        self.lbl_count_baixo.setText("")
        self.lbl_count_baixo.setProperty(u"role", QCoreApplication.translate("application_pages", u"muted", None))
        self.legend_dot_critico.setText("")
        self.legend_dot_critico.setProperty(u"role", QCoreApplication.translate("application_pages", u"legend_dot", None))
        self.legend_dot_critico.setProperty(u"tone", QCoreApplication.translate("application_pages", u"red", None))
        self.legend_text_critico.setText(QCoreApplication.translate("application_pages", u"Cr\u00edtico \u2014", None))
        self.legend_text_critico.setProperty(u"role", QCoreApplication.translate("application_pages", u"muted", None))
        self.lbl_count_critico.setText("")
        self.lbl_count_critico.setProperty(u"role", QCoreApplication.translate("application_pages", u"muted", None))
        self.card_consumo.setProperty(u"role", QCoreApplication.translate("application_pages", u"card", None))
        self.lbl_consumo_title.setText(QCoreApplication.translate("application_pages", u"Consumo \u2014 \u00faltimos 7 dias (%)", None))
        self.lbl_consumo_title.setProperty(u"role", QCoreApplication.translate("application_pages", u"chart_title", None))
        self.chart_consumo.setProperty(u"tone", QCoreApplication.translate("application_pages", u"blue", None))
        self.chart_consumo.setProperty(u"period", QCoreApplication.translate("application_pages", u"days7", None))
        self.card_table_home.setProperty(u"role", QCoreApplication.translate("application_pages", u"card", None))
        ___qtablewidgetitem = self.table_home.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("application_pages", u"BOTIJ\u00c3O", None))
        ___qtablewidgetitem1 = self.table_home.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("application_pages", u"N\u00cdVEL", None))
        ___qtablewidgetitem2 = self.table_home.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("application_pages", u"AUTONOMIA", None))
        ___qtablewidgetitem3 = self.table_home.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("application_pages", u"STATUS", None))
        ___qtablewidgetitem4 = self.table_home.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("application_pages", u"\u00daLTIMA LEITURA", None))
        ___qtablewidgetitem5 = self.table_home.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("application_pages", u"A\u00c7\u00c3O", None))
        self.card_alertas.setProperty(u"role", QCoreApplication.translate("application_pages", u"card", None))
        self.lbl_alertas_title.setText(QCoreApplication.translate("application_pages", u"Alertas", None))
        self.lbl_alertas_title.setProperty(u"role", QCoreApplication.translate("application_pages", u"chart_title", None))
        self.card_financeiro.setProperty(u"role", QCoreApplication.translate("application_pages", u"card", None))
        self.lbl_financeiro_title.setText(QCoreApplication.translate("application_pages", u"Resumo financeiro do m\u00eas", None))
        self.lbl_financeiro_title.setProperty(u"role", QCoreApplication.translate("application_pages", u"chart_title", None))
        self.panel_financeiro.setProperty(u"role", QCoreApplication.translate("application_pages", u"panel_dark", None))
        self.lbl_fin_total_caption.setText(QCoreApplication.translate("application_pages", u"Gasto no m\u00eas", None))
        self.lbl_fin_total_caption.setProperty(u"role", QCoreApplication.translate("application_pages", u"panel_label", None))
        self.lbl_fin_total.setText(QCoreApplication.translate("application_pages", u"\u2014", None))
        self.lbl_fin_total.setProperty(u"role", QCoreApplication.translate("application_pages", u"panel_value", None))
        self.lbl_fin_economia_caption.setText(QCoreApplication.translate("application_pages", u"Economia", None))
        self.lbl_fin_economia_caption.setProperty(u"role", QCoreApplication.translate("application_pages", u"panel_label", None))
        self.lbl_fin_economia.setText(QCoreApplication.translate("application_pages", u"\u2014", None))
        self.lbl_fin_economia.setProperty(u"role", QCoreApplication.translate("application_pages", u"panel_value", None))
        self.lbl_fin_trocas_caption.setText(QCoreApplication.translate("application_pages", u"Trocas realizadas", None))
        self.lbl_fin_trocas_caption.setProperty(u"role", QCoreApplication.translate("application_pages", u"panel_label", None))
        self.lbl_fin_trocas.setText(QCoreApplication.translate("application_pages", u"\u2014", None))
        self.lbl_fin_trocas.setProperty(u"role", QCoreApplication.translate("application_pages", u"panel_value", None))
        self.lbl_title_botijoes.setText(QCoreApplication.translate("application_pages", u"MEUS BOTIJ\u00d5ES", None))
        self.lbl_title_botijoes.setProperty(u"role", QCoreApplication.translate("application_pages", u"page_title", None))
        self.lbl_botijoes_count.setText("")
        self.lbl_botijoes_count.setProperty(u"role", QCoreApplication.translate("application_pages", u"page_subtitle", None))
        self.btn_conectar_botijao.setText(QCoreApplication.translate("application_pages", u"+ Conectar botij\u00e3o", None))
        self.btn_conectar_botijao.setProperty(u"variant", QCoreApplication.translate("application_pages", u"primary", None))
        self.lbl_title_config.setText(QCoreApplication.translate("application_pages", u"CONFIGURA\u00c7\u00d5ES", None))
        self.lbl_title_config.setProperty(u"role", QCoreApplication.translate("application_pages", u"page_title", None))
        self.lbl_config_subtitle.setText(QCoreApplication.translate("application_pages", u"Prefer\u00eancias do aplicativo", None))
        self.lbl_config_subtitle.setProperty(u"role", QCoreApplication.translate("application_pages", u"page_subtitle", None))
        self.card_aparencia.setProperty(u"role", QCoreApplication.translate("application_pages", u"card", None))
        self.lbl_aparencia_title.setText(QCoreApplication.translate("application_pages", u"Apar\u00eancia", None))
        self.lbl_aparencia_title.setProperty(u"role", QCoreApplication.translate("application_pages", u"chart_title", None))
        self.divider_aparencia.setProperty(u"role", QCoreApplication.translate("application_pages", u"divider", None))
        self.lbl_theme_title.setText(QCoreApplication.translate("application_pages", u"Tema escuro", None))
        self.lbl_theme_title.setProperty(u"role", QCoreApplication.translate("application_pages", u"setting_title", None))
        self.lbl_theme_desc.setText(QCoreApplication.translate("application_pages", u"Alterna entre o tema claro e o escuro. A escolha fica salva neste computador.", None))
        self.lbl_theme_desc.setProperty(u"role", QCoreApplication.translate("application_pages", u"muted", None))
        self.lbl_title_pontos.setText(QCoreApplication.translate("application_pages", u"PONTOS DE TROCA", None))
        self.lbl_title_pontos.setProperty(u"role", QCoreApplication.translate("application_pages", u"page_title", None))
        self.lbl_pontos_local.setText("")
        self.lbl_pontos_local.setProperty(u"role", QCoreApplication.translate("application_pages", u"page_subtitle", None))
        self.lbl_como_trocar.setText(QCoreApplication.translate("application_pages", u"COMO FAZER A TROCA", None))
        self.lbl_como_trocar.setProperty(u"role", QCoreApplication.translate("application_pages", u"section_title", None))
        self.card_step_1.setProperty(u"role", QCoreApplication.translate("application_pages", u"card", None))
        self.lbl_step_1_number.setText(QCoreApplication.translate("application_pages", u"01", None))
        self.lbl_step_1_number.setProperty(u"role", QCoreApplication.translate("application_pages", u"step_number", None))
        self.lbl_step_1_title.setText(QCoreApplication.translate("application_pages", u"Feche e desconecte", None))
        self.lbl_step_1_title.setProperty(u"role", QCoreApplication.translate("application_pages", u"step_title", None))
        self.lbl_step_1_text.setText(QCoreApplication.translate("application_pages", u"Feche o registro do botij\u00e3o vazio e desconecte a mangueira com cuidado.", None))
        self.lbl_step_1_text.setProperty(u"role", QCoreApplication.translate("application_pages", u"muted", None))
        self.card_step_2.setProperty(u"role", QCoreApplication.translate("application_pages", u"card", None))
        self.lbl_step_2_number.setText(QCoreApplication.translate("application_pages", u"02", None))
        self.lbl_step_2_number.setProperty(u"role", QCoreApplication.translate("application_pages", u"step_number", None))
        self.lbl_step_2_title.setText(QCoreApplication.translate("application_pages", u"Leve ou pe\u00e7a retirada", None))
        self.lbl_step_2_title.setProperty(u"role", QCoreApplication.translate("application_pages", u"step_title", None))
        self.lbl_step_2_text.setText(QCoreApplication.translate("application_pages", u"Leve o botij\u00e3o vazio at\u00e9 o ponto escolhido ou pe\u00e7a retirada e entrega.", None))
        self.lbl_step_2_text.setProperty(u"role", QCoreApplication.translate("application_pages", u"muted", None))
        self.card_step_3.setProperty(u"role", QCoreApplication.translate("application_pages", u"card", None))
        self.lbl_step_3_number.setText(QCoreApplication.translate("application_pages", u"03", None))
        self.lbl_step_3_number.setProperty(u"role", QCoreApplication.translate("application_pages", u"step_number", None))
        self.lbl_step_3_title.setText(QCoreApplication.translate("application_pages", u"Confira antes de conectar", None))
        self.lbl_step_3_title.setProperty(u"role", QCoreApplication.translate("application_pages", u"step_title", None))
        self.lbl_step_3_text.setText(QCoreApplication.translate("application_pages", u"Verifique o lacre, a validade e a veda\u00e7\u00e3o do botij\u00e3o novo antes de instalar.", None))
        self.lbl_step_3_text.setProperty(u"role", QCoreApplication.translate("application_pages", u"muted", None))
        self.lbl_title_historico.setText(QCoreApplication.translate("application_pages", u"HIST\u00d3RICO", None))
        self.lbl_title_historico.setProperty(u"role", QCoreApplication.translate("application_pages", u"page_title", None))
        self.lbl_historico_subtitle.setText(QCoreApplication.translate("application_pages", u"Consumo e trocas dos \u00faltimos meses", None))
        self.lbl_historico_subtitle.setProperty(u"role", QCoreApplication.translate("application_pages", u"page_subtitle", None))
        self.card_historico_chart.setProperty(u"role", QCoreApplication.translate("application_pages", u"card", None))
        self.lbl_historico_chart_title.setText(QCoreApplication.translate("application_pages", u"Consumo m\u00e9dio mensal (%)", None))
        self.lbl_historico_chart_title.setProperty(u"role", QCoreApplication.translate("application_pages", u"chart_title", None))
        self.chart_historico.setProperty(u"tone", QCoreApplication.translate("application_pages", u"accent", None))
        self.chart_historico.setProperty(u"period", QCoreApplication.translate("application_pages", u"months6", None))
        self.card_table_historico.setProperty(u"role", QCoreApplication.translate("application_pages", u"card", None))
        ___qtablewidgetitem6 = self.table_historico.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("application_pages", u"DATA", None))
        ___qtablewidgetitem7 = self.table_historico.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("application_pages", u"BOTIJ\u00c3O", None))
        ___qtablewidgetitem8 = self.table_historico.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("application_pages", u"LOCAL DA TROCA", None))
        ___qtablewidgetitem9 = self.table_historico.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("application_pages", u"VALOR", None))
    # retranslateUi

