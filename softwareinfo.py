from PyQt5.QtGui import QPixmap
import sigmixres


class SoftwareInfo:
    VERSION_MAJ = 0
    VERSION_MIN = 1
    VERSION_REV = 'a'

    @staticmethod
    def echmetLogo():
        return QPixmap(':/images/res/ECHMET_logo_velke.png')

    @staticmethod
    def versionString():
        return '{:0}.{:1}{:2}'.format(SoftwareInfo.VERSION_MAJ, SoftwareInfo.VERSION_MIN, SoftwareInfo.VERSION_REV)
