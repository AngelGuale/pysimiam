#!/usr/bin/python
# QtSimiam
# Author: Tim Fuchs
# Description: This is the top-level application for QtSimiam.
import sys
sys.path.insert(0, './scripts')
sys.path.insert(0, './gui')
from PyQt4 import QtGui

from qt_mainwindow import SimulationWidget

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    simWidget = SimulationWidget()
    simWidget.show()
    simWidget.load_world("week1.xml")
    app.exec_()
