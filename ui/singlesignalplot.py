from PyQt5.QtWidgets import QWidget, QVBoxLayout, QToolBar
from PyQt5.QtGui import QPen, QBrush, QPalette
from PyQt5.QtCore import Qt
import guiqwt.curve
import guiqwt.plot


class SingleSignalPlot(QWidget):
    @staticmethod
    def _makeAxisDesc(title, unit):
        s = '{} [{}]'.format(title, unit)
        return s

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
        QWidget.__init__(self, parent)

        self.setLayout(QVBoxLayout(self))
        self._plot = guiqwt.plot.CurvePlot(self)
        self._sourceSignalCurve = guiqwt.curve.CurveItem()
        self._transformedSignalCurve = guiqwt.curve.CurveItem()

        self._sourceSignalCurve.setPen(QPen(Qt.red, 1, Qt.DashLine))
        self._transformedSignalCurve.setPen(QPen(Qt.black, 1))

        self._plot.add_item(self._sourceSignalCurve)
        self._plot.add_item(self._transformedSignalCurve)

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

    def clearDisplay(self):
        self._plot.set_axis_title(guiqwt.plot.BasePlot.X_BOTTOM, '')
        self._plot.set_axis_title(guiqwt.plot.BasePlot.Y_LEFT, '')
        self._sourceSignalCurve.setData([], [])
        self._transformedSignalCurve.setData([], [])

    def setDisplay(self, xAxisTitle, yAxisTitle, xAxisUnit, yAxisUnit, sourceSignal, transformedSignal):
        xDesc = self._makeAxisDesc(xAxisTitle, xAxisUnit)
        yDesc = self._makeAxisDesc(yAxisTitle, yAxisUnit)

        self._plot.set_axis_title(guiqwt.plot.BasePlot.X_BOTTOM, xDesc)
        self._plot.set_axis_title(guiqwt.plot.BasePlot.Y_LEFT, yDesc)

        srcSig = self._makeSignalData(sourceSignal)
        self._sourceSignalCurve.set_data(srcSig[0], srcSig[1])
        xfrSig = self._makeSignalData(transformedSignal)
        self._transformedSignalCurve.set_data(xfrSig[0], xfrSig[1])

        self._plot.do_autoscale()

    def updateTransformedSignal(self, transformedSignal):
        xfrSig = self._makeSignalData(transformedSignal)
        self._transformedSignalCurve.setData(xfrSig[0], xfrSig[1])
 
        self._plot.do_autoscale()
