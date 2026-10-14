from qt_core import *


class PyTableWidget(QTableWidget):
    # tabela sem grade/seleção que cresce com o número de linhas
    # (a rolagem fica por conta da página, não da tabela)
    ROW_HEIGHT = 52
    HEADER_HEIGHT = 44

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setFrameShape(QFrame.Shape.NoFrame)
        self.setShowGrid(False)
        self.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        self.verticalHeader().setVisible(False)
        self.verticalHeader().setDefaultSectionSize(self.ROW_HEIGHT)
        self.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Fixed)

        header = self.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        header.setHighlightSections(False)
        header.setFixedHeight(self.HEADER_HEIGHT)
        header.setDefaultAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        model = self.model()
        model.rowsInserted.connect(self._fit_height)
        model.rowsRemoved.connect(self._fit_height)
        model.modelReset.connect(self._fit_height)
        self._fit_height()

    def _fit_height(self, *args):
        # -1: a borda do card faz o papel da linha da última linha
        self.setFixedHeight(self.HEADER_HEIGHT + self.rowCount() * self.ROW_HEIGHT - 1)
