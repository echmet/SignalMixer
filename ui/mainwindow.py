from PyQt5.QtWidgets import QWidget, QMenu, QSizePolicy, QMessageBox, QVBoxLayout, QDialog, QFileDialog, QMenuBar, QAction
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from signaltracemodel import SignalTraceModelError
from forms.mainform import Ui_MainForm
from ui.signalitem import SignalItem
from ui.addedsignalswidget import AddedSignalsWidget
from ui.singlesignalplot import SingleSignalPlot
from ui.mixedsignalsplot import MixedSignalsPlot
from ui.aboutdialog import AboutDialog
from signaltrace import SignalTrace, SignalTraceError
from cropscalepack import CropScalePack
import signalmixerfactory
import ui.selectmixerdialog
import abstractcocktailwriter
import csvcocktailwriter
import os.path
import softwareinfo


class MainWindow(QWidget, Ui_MainForm):
    def _initSignalsTab(self):
        self.qtabw_signalsViews.widget(0).setLayout(QVBoxLayout())
        self.qtabw_signalsViews.widget(1).setLayout(QVBoxLayout())

        self.qtabw_signalsViews.widget(0).layout().addWidget(self._singleSignalPlot)
        self.qtabw_signalsViews.widget(1).layout().addWidget(self._mixedSignalsPlot)

    @pyqtSlot()
    def _onActionAboutTriggered(self):
        AboutDialog().exec_()

    @pyqtSlot(bool)
    def _onActionLoad(self, checked):
        data = self.sender().data()
        self.loadSignal.emit(data[0], data[1], self._lastLoadedPath)

    @pyqtSlot(str, str)
    def _onCustomIDChanged(self, identifier, customID):
        self._signalModel.setCustomSignalID(identifier, customID)

    @pyqtSlot()
    def _onExportMixedSignals(self):
        dlg = ui.selectmixerdialog.SelectMixerDialog(self._mixerFactory.availableMixers(), self)
        ret = dlg.exec_()
        if ret != QDialog.Accepted:
            return

        try:
            mixer = self._mixerFactory.getMixer(dlg.selectedMixer)
            (header, cocktail) = mixer.mix(self._signalModel.allSignals())

            fileDlg = QFileDialog(self)
            fileDlg.setAcceptMode(QFileDialog.AcceptSave)
            fileDlg.setNameFilters(['CSV file (*.csv)'])
            if fileDlg.exec_() != QDialog.Accepted:
                return

            selFiles = fileDlg.selectedFiles()
            if len(selFiles) < 1:
                return

            outputPath = selFiles[0]

            writer = csvcocktailwriter.CSVCocktailWriter()
            writer.write(header, cocktail, outputPath)
            self._lastOutputPath = os.path.realpath(os.path.dirname(outputPath))
        except SignalTraceModelError:
            pass
        except signalmixerfactory.NoSuchMixerError as ex:
            mbox = QMessageBox(QMessageBox.Critical, 'Unable to mix signals', str(ex))
            mbox.exec_()
        except abstractcocktailwriter.CocktailWriterError as ex:
            mbox = QMessageBox(QMessageBox.Warning, 'Unable to write mixed signals', str(ex))
            mbox.exec_()

    @pyqtSlot()
    def _onQuitClicked(self):
        self.close()

    @pyqtSlot(str)
    def _onRemoveSignal(self, identifier):
        sender = self.sender()
        self._signalModel.removeSignal(identifier)
        self._addedSigsWidget.removeItem(sender)
        sender.deleteLater()

        if identifier == self._currentlyDisplayedIdentifier:
            self._singleSignalPlot.clearDisplay()

        self._mixedSignalsPlot.removeSignal(identifier)

    @pyqtSlot(str)
    def _onShowSignal(self, identifier):
        try:
            sig = self._signalModel.getSignal(identifier)
            self._singleSignalPlot.setDisplay(sig.xUnit, sig.yUnit, sig.xTitle, sig.yTitle, sig.sourceSignal(), sig.transformedSignal())
            self._currentlyDisplayedIdentifier = identifier
        except SignalTraceModelError as ex:
            mbox = QMessageBox(QMessageBox.Critical, 'Signal model error', 'Cannot display signal: {}'.format(str(ex)))
            mbox.exec_()

    def _setupLoadingActions(self, sffs):
        for sff in sffs:
            text = 'Load {} file'.format(sff.shortDescription)
            if len(sff.loadingOptions) < 2:
                action = self._loadMenu.addAction(text)
                action.setData((sff.tag, 0))
                action.triggered.connect(self._onActionLoad)
            else:
                submenu = self._loadMenu.addMenu(text)
                for opt in sff.loadingOptions:
                    action = submenu.addAction('From {}'.format(opt.name))
                    action.setData((sff.tag, opt.index))
                    action.triggered.connect(self._onActionLoad)

    def __init__(self, supportedFileFormats, signalModel, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self._loadMenu = QMenu(self)
        self._setupLoadingActions(supportedFileFormats)
        self._signalModel = signalModel
        self._currentlyDisplayedIdentifier = ''
        self._lastLoadedPath = ''
        self.setWindowTitle('SignalMixer {}'.format(softwareinfo.SoftwareInfo.versionString()))

        actionAbout = QAction('About', self)
        menuBar = QMenuBar(self)
        menuBar.addAction(actionAbout)

        self.layout().insertWidget(0, menuBar)

        self._addedSigsWidget = AddedSignalsWidget(self)
        self.qscrArea_addedSignals.setWidget(self._addedSigsWidget)

        self._singleSignalPlot = SingleSignalPlot(self)
        self._mixedSignalsPlot = MixedSignalsPlot(self)
        self._singleSignalPlot.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.qpb_addSignal.setMenu(self._loadMenu)
        self._initSignalsTab()

        self._mixerFactory = signalmixerfactory.SignalMixerFactory()

        signalModel.signalLoaded.connect(self.onSignalLoaded)
        self.qpb_exportMixedSignals.clicked.connect(self._onExportMixedSignals)
        self.qpb_quit.clicked.connect(self._onQuitClicked)
        actionAbout.triggered.connect(self._onActionAboutTriggered)

    loadSignal = pyqtSignal(str, int, str)

    @pyqtSlot(str, CropScalePack)
    def onSignalAdjusted(self, identifier, pack):
        try:
            self._signalModel.adjustSignal(identifier, pack)

            sig = self._signalModel.getSignal(identifier)
            if self._currentlyDisplayedIdentifier == identifier:
                self._singleSignalPlot.updateTransformedSignal(sig.transformedSignal())
            else:
                self._singleSignalPlot.setDisplay(sig.xTitle, sig.yTitle, sig.xUnit, sig.yUnit, sig.sourceSignal(), sig.transformedSignal())
                self._currentlyDisplayedIdentifier = identifier

            self._mixedSignalsPlot.updateSignal(identifier, sig.transformedSignal())
        except SignalTraceError as ex:
            mbox = QMessageBox(QMessageBox.Warning, 'Signal error', str(ex))
            mbox.exec_()
        except SignalTraceModelError as ex:
            mbox = QMessageBox(QMessageBox.Critical, 'Signal model error', str(ex))
            mbox.exec_()

    @pyqtSlot(SignalTrace, str)
    def onSignalLoaded(self, sig, identifier):
        if len(identifier) == 0:
            mbox = QMessageBox(QMessageBox.Information, 'Cannot load signal', 'Signal is already loaded')
            mbox.exec_()
            return

        self._lastLoadedPath = os.path.realpath(os.path.dirname(sig.srcFile))

        xFirst = sig.sourceSignal()[0].x
        xLast = sig.sourceSignal()[-1].x
        yZero = sig.sourceSignal()[0].y
        xStep = sig.averageXStep()

        sigItem = SignalItem(identifier, sig.srcFile, sig.dataID, sig.customID, xFirst, xLast, yZero, xStep, self)
        self._addedSigsWidget.addItem(sigItem)

        self._singleSignalPlot.setDisplay(sig.xTitle, sig.yTitle, sig.xUnit, sig.yUnit, sig.sourceSignal(), sig.transformedSignal())
        self._mixedSignalsPlot.addSignal(identifier, sig.transformedSignal())

        self._currentlyDisplayedIdentifier = identifier

        sigItem.removeSignal.connect(self._onRemoveSignal)
        sigItem.showSignal.connect(self._onShowSignal)
        sigItem.signalAdjusted.connect(self.onSignalAdjusted)
        sigItem.customIDChanged.connect(self._onCustomIDChanged)
