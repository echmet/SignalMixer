from PyQt5.QtCore import pyqtSlot, QSize
from PyQt5.QtWidgets import QWidget, QVBoxLayout
import ui.signalitem


class AddedSignalsWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setLayout(QVBoxLayout(self))
        self.layout().addStretch()

        self.setMinimumWidth(ui.signalitem.SignalItem.getMinimumWidth())

    def addItem(self, widget):
        self.layout().insertWidget(self.layout().count() - 1, widget)

    def removeItem(self, widget):
        self.layout().removeWidget(widget)

    def minimumSizeHint(self):
        w = ui.signalitem.SignalItem.getMinimumWidth()
        h = QWidget.minimumSizeHint(self).height()

        return QSize(w, h)

    def sizeHint(self):
        return self.minimumSizeHint()
