# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Lancement_combat.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Lancement_combat(object):
    def setupUi(self, Lancement_combat):
        Lancement_combat.setObjectName("Lancement_combat")
        Lancement_combat.resize(1033, 582)
        Lancement_combat.setMinimumSize(QtCore.QSize(1033, 580))
        Lancement_combat.setMaximumSize(QtCore.QSize(1033, 582))
        Lancement_combat.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Ensemble_lancement = QtWidgets.QGroupBox(Lancement_combat)
        self.Ensemble_lancement.setGeometry(QtCore.QRect(0, -10, 1051, 591))
        self.Ensemble_lancement.setTitle("")
        self.Ensemble_lancement.setObjectName("Ensemble_lancement")
        self.PASS = QtWidgets.QCommandLinkButton(self.Ensemble_lancement)
        self.PASS.setGeometry(QtCore.QRect(900, 10, 141, 131))
        self.PASS.setMinimumSize(QtCore.QSize(111, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.PASS.setFont(font)
        self.PASS.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Images/Pass.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PASS.setIcon(icon)
        self.PASS.setIconSize(QtCore.QSize(120, 120))
        self.PASS.setObjectName("PASS")
        self.VS = QtWidgets.QLabel(self.Ensemble_lancement)
        self.VS.setGeometry(QtCore.QRect(-10, 0, 1091, 591))
        self.VS.setText("")
        self.VS.setPixmap(QtGui.QPixmap("../Images/VS.jpg"))
        self.VS.setScaledContents(True)
        self.VS.setObjectName("VS")
        self.Joueur = QtWidgets.QLabel(self.Ensemble_lancement)
        self.Joueur.setGeometry(QtCore.QRect(0, 210, 461, 341))
        self.Joueur.setText("")
        self.Joueur.setScaledContents(True)
        self.Joueur.setObjectName("Joueur")
        self.Nom_Pokemon_3 = QtWidgets.QLabel(self.Ensemble_lancement)
        self.Nom_Pokemon_3.setGeometry(QtCore.QRect(410, 170, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Nom_Pokemon_3.setFont(font)
        self.Nom_Pokemon_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.Nom_Pokemon_3.setText("")
        self.Nom_Pokemon_3.setAlignment(QtCore.Qt.AlignCenter)
        self.Nom_Pokemon_3.setObjectName("Nom_Pokemon_3")
        self.Pokemon_3 = QtWidgets.QLabel(self.Ensemble_lancement)
        self.Pokemon_3.setGeometry(QtCore.QRect(410, 20, 131, 141))
        self.Pokemon_3.setText("")
        self.Pokemon_3.setScaledContents(True)
        self.Pokemon_3.setObjectName("Pokemon_3")
        self.Nom_Pokemon_2 = QtWidgets.QLabel(self.Ensemble_lancement)
        self.Nom_Pokemon_2.setGeometry(QtCore.QRect(200, 170, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Nom_Pokemon_2.setFont(font)
        self.Nom_Pokemon_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.Nom_Pokemon_2.setText("")
        self.Nom_Pokemon_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Nom_Pokemon_2.setObjectName("Nom_Pokemon_2")
        self.Pokemon_1 = QtWidgets.QLabel(self.Ensemble_lancement)
        self.Pokemon_1.setGeometry(QtCore.QRect(10, 10, 131, 151))
        self.Pokemon_1.setText("")
        self.Pokemon_1.setScaledContents(True)
        self.Pokemon_1.setObjectName("Pokemon_1")
        self.Pokemon_2 = QtWidgets.QLabel(self.Ensemble_lancement)
        self.Pokemon_2.setGeometry(QtCore.QRect(200, 10, 151, 161))
        self.Pokemon_2.setText("")
        self.Pokemon_2.setScaledContents(True)
        self.Pokemon_2.setObjectName("Pokemon_2")
        self.Nom_Pokemon_1 = QtWidgets.QLabel(self.Ensemble_lancement)
        self.Nom_Pokemon_1.setGeometry(QtCore.QRect(0, 170, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Nom_Pokemon_1.setFont(font)
        self.Nom_Pokemon_1.setStyleSheet("color: rgb(255, 255, 255);")
        self.Nom_Pokemon_1.setText("")
        self.Nom_Pokemon_1.setAlignment(QtCore.Qt.AlignCenter)
        self.Nom_Pokemon_1.setObjectName("Nom_Pokemon_1")
        self.Nom_adversaire = QtWidgets.QLabel(self.Ensemble_lancement)
        self.Nom_adversaire.setGeometry(QtCore.QRect(600, 460, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.Nom_adversaire.setFont(font)
        self.Nom_adversaire.setText("")
        self.Nom_adversaire.setAlignment(QtCore.Qt.AlignCenter)
        self.Nom_adversaire.setObjectName("Nom_adversaire")
        self.Adversaire = QtWidgets.QLabel(self.Ensemble_lancement)
        self.Adversaire.setGeometry(QtCore.QRect(630, 180, 241, 271))
        self.Adversaire.setText("")
        self.Adversaire.setScaledContents(True)
        self.Adversaire.setObjectName("Adversaire")
        self.Type_1 = QtWidgets.QLabel(self.Ensemble_lancement)
        self.Type_1.setGeometry(QtCore.QRect(890, 310, 71, 81))
        self.Type_1.setText("")
        self.Type_1.setScaledContents(True)
        self.Type_1.setObjectName("Type_1")
        self.Type_2 = QtWidgets.QLabel(self.Ensemble_lancement)
        self.Type_2.setGeometry(QtCore.QRect(890, 210, 71, 81))
        self.Type_2.setText("")
        self.Type_2.setScaledContents(True)
        self.Type_2.setObjectName("Type_2")
        self.Type_3 = QtWidgets.QLabel(self.Ensemble_lancement)
        self.Type_3.setGeometry(QtCore.QRect(150, 20, 51, 61))
        self.Type_3.setText("")
        self.Type_3.setScaledContents(True)
        self.Type_3.setObjectName("Type_3")
        self.Type_4 = QtWidgets.QLabel(self.Ensemble_lancement)
        self.Type_4.setGeometry(QtCore.QRect(150, 90, 51, 61))
        self.Type_4.setText("")
        self.Type_4.setScaledContents(True)
        self.Type_4.setObjectName("Type_4")
        self.Type_5 = QtWidgets.QLabel(self.Ensemble_lancement)
        self.Type_5.setGeometry(QtCore.QRect(350, 90, 51, 61))
        self.Type_5.setText("")
        self.Type_5.setScaledContents(True)
        self.Type_5.setObjectName("Type_5")
        self.Type_6 = QtWidgets.QLabel(self.Ensemble_lancement)
        self.Type_6.setGeometry(QtCore.QRect(350, 20, 51, 61))
        self.Type_6.setText("")
        self.Type_6.setScaledContents(True)
        self.Type_6.setObjectName("Type_6")
        self.Type_7 = QtWidgets.QLabel(self.Ensemble_lancement)
        self.Type_7.setGeometry(QtCore.QRect(550, 20, 51, 61))
        self.Type_7.setText("")
        self.Type_7.setScaledContents(True)
        self.Type_7.setObjectName("Type_7")
        self.Type_8 = QtWidgets.QLabel(self.Ensemble_lancement)
        self.Type_8.setGeometry(QtCore.QRect(550, 90, 51, 61))
        self.Type_8.setText("")
        self.Type_8.setScaledContents(True)
        self.Type_8.setObjectName("Type_8")
        self.VS.raise_()
        self.PASS.raise_()
        self.Joueur.raise_()
        self.Nom_Pokemon_3.raise_()
        self.Pokemon_3.raise_()
        self.Nom_Pokemon_2.raise_()
        self.Pokemon_1.raise_()
        self.Pokemon_2.raise_()
        self.Nom_Pokemon_1.raise_()
        self.Nom_adversaire.raise_()
        self.Adversaire.raise_()
        self.Type_1.raise_()
        self.Type_2.raise_()
        self.Type_3.raise_()
        self.Type_4.raise_()
        self.Type_5.raise_()
        self.Type_6.raise_()
        self.Type_7.raise_()
        self.Type_8.raise_()

        self.retranslateUi(Lancement_combat)
        QtCore.QMetaObject.connectSlotsByName(Lancement_combat)

    def retranslateUi(self, Lancement_combat):
        _translate = QtCore.QCoreApplication.translate
        Lancement_combat.setWindowIcon(QtGui.QIcon("../Images/Pokemon_logo.png"))
        Lancement_combat.setWindowTitle(_translate("Lancement_combat", "  POKEMON"))
