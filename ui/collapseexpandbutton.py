import math
from PyQt5.QtCore import QPointF, pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QPalette, QPen, QPainterPath, QPainter
from enum import Enum


class State(Enum):
    COLLAPSED = 1
    EXPANDED = 2


class Transition(Enum):
    COLLAPSE = 1
    EXPAND = 2


class CollapseExpandButton(QPushButton):
    def _buildPainterPaths(self, size):
        marginLR = int(math.floor((size.width() * 0.3) + 0.5))
        marginUD = int(math.floor((size.height() * 0.3) + 0.5))
        middleColl = int(math.floor((size.height() / 2.0) + 0.5))
        middleExpd = int(math.floor((size.width() / 2.0) + 0.5))

        self._collapsedPath = QPainterPath(QPointF(size.width() - marginLR, marginUD))
        self._collapsedPath.lineTo(marginLR, middleColl)
        self._collapsedPath.lineTo(size.width() - marginLR, size.height() - marginUD)

        self._expandedPath = QPainterPath(QPointF(marginLR, marginUD))
        self._expandedPath.lineTo(middleExpd, size.height() - marginUD)
        self._expandedPath.lineTo(size.width() - marginLR, marginUD)

    @pyqtSlot()
    def _onClicked(self):
        if self._currentState == State.COLLAPSED:
            self._currentState = State.EXPANDED
            self.collapsedExpanded.emit(Transition.EXPAND)
        elif self._currentState == State.EXPANDED:
            self._currentState = State.COLLAPSED
            self.collapsedExpanded.emit(Transition.COLLAPSE)

        super().update()

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setText('')
        self._currentState = State.EXPANDED

        pal = self.palette()
        self._pen = QPen(pal.color(QPalette.WindowText))
        self._pen.setWidth(2)

        self._collapsedPath = None
        self._expandedPath = None
        self._buildPainterPaths(self.size())

        self.clicked.connect(self._onClicked)

    collapsedExpanded = pyqtSignal(Transition)

    def paintEvent(self, ev):
        super().paintEvent(ev)

        p = QPainter(self)
        p.setPen(self._pen)
        p.setRenderHint(QPainter.Antialiasing, True)

        if self._currentState == State.COLLAPSED:
            p.fillPath(self._collapsedPath, self._pen.brush())
        elif self._currentState == State.EXPANDED:
            p.fillPath(self._expandedPath, self._pen.brush())

    def resizeEvent(self, ev):
        self._buildPainterPaths(ev.size())

    def setState(self, state):
        self._currentState = state
        self.repaint()

    def state(self):
        return self._currentState
