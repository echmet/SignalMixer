from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QToolBar
from PyQt5.QtGui import QPalette
import guiqwt.curve
import guiqwt.plot

class MixedSignalsPlot(QWidget):
    @staticmethod
    def _makeSignalData(src):
        _srcDataX = []
        _srcDataY = []
        for pt in src:
            _srcDataX.append(pt.x)
            _srcDataY.append(pt.y)

        return (_srcDataX, _srcDataY)

    def _registerPlotTools(self):
        self._plotMgr.add_tool(guiqwt.tools.RectZoomTool)
        self._plotMgr.add_tool(guiqwt.tools.SelectTool)
        self._plotMgr.add_tool(guiqwt.tools.AxisScaleTool)
        self._plotMgr.add_tool(guiqwt.tools.DisplayCoordsTool)
        self._plotMgr.add_tool(guiqwt.tools.BasePlotMenuTool, "axes")
        self._plotMgr.add_tool(guiqwt.tools.BasePlotMenuTool, "grid")

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setLayout(QVBoxLayout())
        self._plot = guiqwt.plot.CurvePlot(self)

        self._displayedSignals = {}

        self.layout().addWidget(self._plot)

        self._plot.setAutoFillBackground(True)
        p = self._plot.palette()
        p.setColor(QPalette.Window, Qt.white)
        p.setColor(QPalette.WindowText, Qt.black)
        p.setColor(QPalette.Text, Qt.black)
        self._plot.setPalette(p)

        self._toolBar = QToolBar(self)
        self.layout().addWidget(self._toolBar)

        self._plotMgr = guiqwt.plot.PlotManager(self)
        self._plotMgr.add_plot(self._plot)
        self._plotMgr.add_toolbar(self._toolBar, id(self._toolBar))

        self._registerPlotTools()

    def addSignal(self, identifier, transformedSignal):
        if identifier in self._displayedSignals:
            self.updateSignal(identifier, transformedSignal)
            return

        xfrSig = self._makeSignalData(transformedSignal)

        curve = guiqwt.curve.CurveItem()
        curve.set_data(xfrSig[0], xfrSig[1])
        self._plot.add_item(curve)

        self._displayedSignals[identifier] = curve

    def removeSignal(self, identifier):
        if identifier in self._displayedSignals:
            curve = self._displayedSignals[identifier]
            self._plot.del_item(curve)
            del self._displayedSignals[identifier]

    def updateSignal(self, identifier, transformedSignal):
        if identifier in self._displayedSignals:
            curve = self._displayedSignals[identifier]
            xfrSig = self._makeSignalData(transformedSignal)
            curve.set_data(xfrSig[0], xfrSig[1])
