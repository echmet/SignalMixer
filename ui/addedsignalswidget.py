from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtCore import QSize


class AddedSignalsWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setLayout(QVBoxLayout(self))
        self.layout().addStretch()

    def addItem(self, widget):
        self.layout().insertWidget(self.layout().count() - 1, widget)

    def removeItem(self, widget):
        self.layout().removeWidget(widget)
