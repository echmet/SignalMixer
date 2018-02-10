from PyQt5.QtCore import pyqtSlot, QSize
from PyQt5.QtWidgets import QWidget, QVBoxLayout
import ui.signalitem


class AddedSignalsWidget(QWidget):
    @pyqtSlot()
    def _onContentHeightChanged(self):
        print('content size changed')
        self.resize(self.minimumSizeHint())

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setLayout(QVBoxLayout(self))
        self.layout().addStretch()

        self.setMinimumWidth(ui.signalitem.SignalItem.getMinimumWidth())

    def addItem(self, widget):
        self.layout().insertWidget(self.layout().count() - 1, widget)
        self.resize(self.minimumSizeHint())

        widget.heightChanged.connect(self._onContentHeightChanged)

    def removeItem(self, widget):
        self.layout().removeWidget(widget)
        self.resize(self.minimumSizeHint())

    def minimumSizeHint(self):
        print('Getting size hint for AddedSignalsWidget')

        w = QWidget.sizeHint(self).width()
        h = 0
        for idx in range(0, self.layout().count()):
            wg = self.layout().itemAt(idx).widget()
            if wg is None:
                continue
            h += wg.sizeHint().height()
            w = wg.sizeHint().width()

        print('MSH {} {}'.format(w, h))
        return QSize(w, h)

    def sizeHint(self):
        return self.minimumSizeHint()
