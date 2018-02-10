from PyQt5.QtWidgets import QWidget, QLineEdit
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QSize
from PyQt5.QtGui import QFont, QFontMetrics
from forms.signalitem import Ui_SignalItem
from ui.cropscalewidget import CropScaleWidget
from cropscalepack import CropScalePack
import ui.collapseexpandbutton


class SignalItem(QWidget, Ui_SignalItem):
    class WidthHinter:
        def __init__(self, font):
            self._txt = '{:x<60}'.format('')
            self._metrics = QFontMetrics(font)

        def width(self):
            return int(self._metrics.width(self._txt) * 1.05)

    def _croppingControlsHeight(self):
        if self._cropScaleWidget.isCollapsed:
            return 0
        return self._cropScaleWidget.height()

    @pyqtSlot(ui.collapseexpandbutton.Transition)
    def _onCollapseExpand(self, trans):
        if trans == ui.collapseexpandbutton.Transition.COLLAPSE:
            self._cropScaleWidget.collapse()
            self.qpb_collapseExpandButton.setState(ui.collapseexpandbutton.State.COLLAPSED)
        elif trans == ui.collapseexpandbutton.Transition.EXPAND:
            self._cropScaleWidget.expand()
            self.qpb_collapseExpandButton.setState(ui.collapseexpandbutton.State.EXPANDED)

        self.heightChanged.emit()

    @pyqtSlot(CropScalePack)
    def _onCropScaleParamsChanged(self, pack):
        self.signalAdjusted.emit(self._identifier, pack)

    @pyqtSlot()
    def _onCustomIDChanged(self):
        self.customIDChanged.emit(self._identifier, self.qle_customID.text())

    @pyqtSlot()
    def _onRemoveClicked(self):
        self.removeSignal.emit(self._identifier)

    @pyqtSlot()
    def _onShowClicked(self):
        self.showSignal.emit(self._identifier)

    def __init__(self, identifier, dataSrc, dataID, customID, xFirst, xLast, yZero, xStep, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self._identifier = identifier
        self._cropScaleWidget = CropScaleWidget(xFirst, xLast, yZero, xStep, self)
        self._widthHinter = SignalItem.WidthHinter(self.font())

        self.qle_dataSource.setText(dataSrc)
        self.qle_dataID.setText(dataID)
        self.qle_customID.setText(customID)

        self.layout().addWidget(self._cropScaleWidget)

        self._cropScaleWidget.collapse()
        self.qpb_collapseExpandButton.setState(ui.collapseexpandbutton.State.COLLAPSED)

        self.qpb_remove.clicked.connect(self._onRemoveClicked)
        self.qpb_show.clicked.connect(self._onShowClicked)
        self._cropScaleWidget.cropScaleParamsChanged.connect(self._onCropScaleParamsChanged)
        self.qpb_collapseExpandButton.collapsedExpanded.connect(self._onCollapseExpand)
        self.qle_customID.editingFinished.connect(self._onCustomIDChanged)

    @staticmethod
    def getMinimumWidth():
        return SignalItem.WidthHinter(QLineEdit().font()).width()

    def minimumHeight(self):
        h = self.qle_dataID.minimumSizeHint().height()
        return 6 * h

    def minimumWidth(self):
        return self._widthHinter.width()

    def minimumSizeHint(self):
        w = self.minimumWidth()
        h = self.minimumHeight() + self._croppingControlsHeight()
        return QSize(w, h)

    def sizeHint(self):
        return self.minimumSizeHint()

    customIDChanged = pyqtSignal(str, str)
    heightChanged = pyqtSignal()
    removeSignal = pyqtSignal(str)
    showSignal = pyqtSignal(str)
    signalAdjusted = pyqtSignal(str, CropScalePack)
