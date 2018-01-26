from collections import namedtuple
from ui.xunitinputdialog import XUnitInputDialog


UnitIdentifier = namedtuple('UnitIdentifier', ['names', 'ratio'])

IDENTIFIERS = [
    UnitIdentifier(names=['ms', 'msec', 'millisecond', 'milliseconds'], ratio=0.001),
    UnitIdentifier(names=['s', 'sec', 'second', 'seconds'], ratio=1.0),
    UnitIdentifier(names=['min', 'minute', 'minutes'], ratio=60.0),
    UnitIdentifier(names=['h', 'hr', 'hour', 'hours'], ratio=3600.0)
]


def _getRatioFromUser(xUnit):
    dlg = XUnitInputDialog(xUnit)
    dlg.exec_()
    return dlg.multiplier()

def guessRatio(xUnit):
    _xUnit = xUnit.lower()
    for ident in IDENTIFIERS:
        for name in ident.names:
            if name == _xUnit:
                return ident.ratio

    return _getRatioFromUser(xUnit)
