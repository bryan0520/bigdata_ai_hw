from PyQt5 import QtWidgets, QtGui, QtCore
import importlib
import ConsoleConfig



class AlertConsoleEvent(QtWidgets.QMainWindow):

    def __init__(self):
        super(AlertConsoleEvent, self).__init__()
        self.ui = importlib.import_module(ConsoleConfig.ui).Ui_MainWindow()
        self.ui.setupUi(self)
