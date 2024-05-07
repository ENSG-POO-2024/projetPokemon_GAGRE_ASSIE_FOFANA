# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Zone_de_bataille.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(764, 440)
        self.Ensemble_bataille = QtWidgets.QGroupBox(Dialog)
        self.Ensemble_bataille.setGeometry(QtCore.QRect(-40, -30, 841, 471))
        self.Ensemble_bataille.setTitle("")
        self.Ensemble_bataille.setObjectName("Ensemble_bataille")
        self.Arene = QtWidgets.QLabel(self.Ensemble_bataille)
        self.Arene.setGeometry(QtCore.QRect(40, 20, 821, 451))
        self.Arene.setText("")
        self.Arene.setPixmap(QtGui.QPixmap("../Images_interface/Arene.png"))
        self.Arene.setScaledContents(True)
        self.Arene.setObjectName("Arene")
        self.Arriere = QtWidgets.QLabel(self.Ensemble_bataille)
        self.Arriere.setGeometry(QtCore.QRect(30, -50, 851, 531))
        self.Arriere.setStyleSheet("background-color: rgb(229, 229, 229);")
        self.Arriere.setText("")
        self.Arriere.setObjectName("Arriere")
        self.Hopital_1 = QtWidgets.QLabel(self.Ensemble_bataille)
        self.Hopital_1.setGeometry(QtCore.QRect(150, 360, 91, 101))
        self.Hopital_1.setText("")
        self.Hopital_1.setPixmap(QtGui.QPixmap("../Images_interface/Hopital.webp"))
        self.Hopital_1.setScaledContents(True)
        self.Hopital_1.setObjectName("Hopital_1")
        self.Hopital_2 = QtWidgets.QLabel(self.Ensemble_bataille)
        self.Hopital_2.setGeometry(QtCore.QRect(360, 360, 91, 101))
        self.Hopital_2.setText("")
        self.Hopital_2.setPixmap(QtGui.QPixmap("../Images_interface/Hopital.webp"))
        self.Hopital_2.setScaledContents(True)
        self.Hopital_2.setObjectName("Hopital_2")
        self.Hopital_3 = QtWidgets.QLabel(self.Ensemble_bataille)
        self.Hopital_3.setGeometry(QtCore.QRect(570, 360, 91, 101))
        self.Hopital_3.setText("")
        self.Hopital_3.setPixmap(QtGui.QPixmap("../Images_interface/Hopital.webp"))
        self.Hopital_3.setScaledContents(True)
        self.Hopital_3.setObjectName("Hopital_3")
        self.Pokemon_KO_1 = QtWidgets.QLabel(self.Ensemble_bataille)
        self.Pokemon_KO_1.setGeometry(QtCore.QRect(250, 350, 101, 101))
        self.Pokemon_KO_1.setText("")
        self.Pokemon_KO_1.setScaledContents(True)
        self.Pokemon_KO_1.setObjectName("Pokemon_KO_1")
        self.Pokemon_KO_2 = QtWidgets.QLabel(self.Ensemble_bataille)
        self.Pokemon_KO_2.setGeometry(QtCore.QRect(460, 350, 101, 101))
        self.Pokemon_KO_2.setText("")
        self.Pokemon_KO_2.setScaledContents(True)
        self.Pokemon_KO_2.setObjectName("Pokemon_KO_2")
        self.Pokemon_KO_3 = QtWidgets.QLabel(self.Ensemble_bataille)
        self.Pokemon_KO_3.setGeometry(QtCore.QRect(670, 350, 101, 101))
        self.Pokemon_KO_3.setText("")
        self.Pokemon_KO_3.setScaledContents(True)
        self.Pokemon_KO_3.setObjectName("Pokemon_KO_3")
        self.Pokemon_1 = QtWidgets.QLabel(self.Ensemble_bataille)
        self.Pokemon_1.setGeometry(QtCore.QRect(60, 40, 101, 101))
        self.Pokemon_1.setText("")
        self.Pokemon_1.setScaledContents(True)
        self.Pokemon_1.setObjectName("Pokemon_1")
        self.Pokemon_2 = QtWidgets.QLabel(self.Ensemble_bataille)
        self.Pokemon_2.setGeometry(QtCore.QRect(160, 40, 101, 101))
        self.Pokemon_2.setText("")
        self.Pokemon_2.setScaledContents(True)
        self.Pokemon_2.setObjectName("Pokemon_2")
        self.Pokemon_3 = QtWidgets.QLabel(self.Ensemble_bataille)
        self.Pokemon_3.setGeometry(QtCore.QRect(270, 40, 101, 101))
        self.Pokemon_3.setText("")
        self.Pokemon_3.setScaledContents(True)
        self.Pokemon_3.setObjectName("Pokemon_3")
        self.Pokemon_attaquant = QtWidgets.QLabel(self.Ensemble_bataille)
        self.Pokemon_attaquant.setGeometry(QtCore.QRect(240, 230, 111, 101))
        self.Pokemon_attaquant.setText("")
        self.Pokemon_attaquant.setScaledContents(True)
        self.Pokemon_attaquant.setObjectName("Pokemon_attaquant")
        self.Adversaire = QtWidgets.QLabel(self.Ensemble_bataille)
        self.Adversaire.setGeometry(QtCore.QRect(570, 230, 101, 101))
        self.Adversaire.setText("")
        self.Adversaire.setScaledContents(True)
        self.Adversaire.setObjectName("Adversaire")
        self.Joueur = QtWidgets.QLabel(self.Ensemble_bataille)
        self.Joueur.setGeometry(QtCore.QRect(46, 180, 141, 171))
        self.Joueur.setText("")
        self.Joueur.setScaledContents(True)
        self.Joueur.setObjectName("Joueur")
        self.Echange = QtWidgets.QPushButton(self.Ensemble_bataille)
        self.Echange.setGeometry(QtCore.QRect(400, 30, 81, 61))
        self.Echange.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Images_interface/Echange.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Echange.setIcon(icon)
        self.Echange.setIconSize(QtCore.QSize(80, 80))
        self.Echange.setObjectName("Echange")
        self.Neutre = QtWidgets.QPushButton(self.Ensemble_bataille)
        self.Neutre.setGeometry(QtCore.QRect(510, 50, 91, 81))
        self.Neutre.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Images_interface/Neutre.webp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Neutre.setIcon(icon1)
        self.Neutre.setIconSize(QtCore.QSize(70, 70))
        self.Neutre.setObjectName("Neutre")
        self.Fuir = QtWidgets.QPushButton(self.Ensemble_bataille)
        self.Fuir.setGeometry(QtCore.QRect(400, 100, 81, 61))
        self.Fuir.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../Images_interface/Exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Fuir.setIcon(icon2)
        self.Fuir.setIconSize(QtCore.QSize(80, 80))
        self.Fuir.setObjectName("Fuir")
        self.Type1 = QtWidgets.QPushButton(self.Ensemble_bataille)
        self.Type1.setGeometry(QtCore.QRect(700, 50, 61, 81))
        self.Type1.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../Images_interface/Types/Bug.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Type1.setIcon(icon3)
        self.Type1.setIconSize(QtCore.QSize(100, 75))
        self.Type1.setObjectName("Type1")
        self.Type2 = QtWidgets.QPushButton(self.Ensemble_bataille)
        self.Type2.setGeometry(QtCore.QRect(620, 50, 61, 81))
        self.Type2.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../Images_interface/Types/Fire.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Type2.setIcon(icon4)
        self.Type2.setIconSize(QtCore.QSize(100, 75))
        self.Type2.setObjectName("Type2")
        self.PV_adversaire = QtWidgets.QLabel(self.Ensemble_bataille)
        self.PV_adversaire.setGeometry(QtCore.QRect(570, 200, 101, 31))
        self.PV_adversaire.setText("")
        self.PV_adversaire.setAlignment(QtCore.Qt.AlignCenter)
        self.PV_adversaire.setObjectName("PV_adversaire")
        self.PV_attaquant = QtWidgets.QLabel(self.Ensemble_bataille)
        self.PV_attaquant.setGeometry(QtCore.QRect(240, 200, 101, 31))
        self.PV_attaquant.setText("")
        self.PV_attaquant.setAlignment(QtCore.Qt.AlignCenter)
        self.PV_attaquant.setObjectName("PV_attaquant")
        self.Arriere.raise_()
        self.Arene.raise_()
        self.Hopital_1.raise_()
        self.Hopital_2.raise_()
        self.Hopital_3.raise_()
        self.Pokemon_KO_1.raise_()
        self.Pokemon_KO_2.raise_()
        self.Pokemon_KO_3.raise_()
        self.Pokemon_1.raise_()
        self.Pokemon_2.raise_()
        self.Pokemon_3.raise_()
        self.Pokemon_attaquant.raise_()
        self.Adversaire.raise_()
        self.Joueur.raise_()
        self.Echange.raise_()
        self.Neutre.raise_()
        self.Fuir.raise_()
        self.Type1.raise_()
        self.Type2.raise_()
        self.PV_adversaire.raise_()
        self.PV_attaquant.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
