from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Inventaire_Pokemon(object):
    def setupUi(self):
        self.setWindowTitle("   INVENTAIRE DU JOUEUR")
        self.setWindowIcon(QtGui.QIcon("../Images/Pokemon_logo.png"))
        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QtWidgets.QVBoxLayout(self.central_widget)
