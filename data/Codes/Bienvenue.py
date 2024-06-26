from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication

class Ui_Bienvenue(object):
    def setupUi(self, Bienvenue):
        Bienvenue.setObjectName("Bienvenue")
        self.setFixedSize(1033, 580)
        # -----------------------------------------
        # Centrer la fenêtre sur l'écran
        window_geometry = self.frameGeometry()
        center_point = QApplication.desktop().availableGeometry().center()
        window_geometry.moveCenter(center_point)
        self.move(window_geometry.topLeft())
        #-----------------------------------------
        self.background = QtWidgets.QLabel(Bienvenue)
        self.background.setGeometry(QtCore.QRect(10, 10, 1011, 561))
        self.background.setPixmap(QtGui.QPixmap("../Images/background/bienvenue_5.png"))
        self.background.setObjectName("background")
        self.welcome_message = QtWidgets.QLabel(Bienvenue)
        self.welcome_message.setGeometry(QtCore.QRect(60, 40, 941, 41))
        self.welcome_message.setStyleSheet("font: 81 20pt \"Rockwell Nova Extra Bold\";color: rgb(255, 255, 255);")
        self.welcome_message.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome_message.setObjectName("welcome_message")
        self.player_name = QtWidgets.QLineEdit(Bienvenue)
        self.player_name.setGeometry(QtCore.QRect(240, 130, 271, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.player_name.setFont(font)
        self.player_name.setStyleSheet("background-color: rgba(0, 0, 0, 0);border-bottom: 2px solid rgba(200, 200, 200, 180);color: rgba(255, 255, 255,180);border-top: 0;border-left: 0;border-right: 0;padding-bottom: 7px;")
        self.player_name.setObjectName("player_name")
        self.player_name.setMaxLength(12)   # Fixer le nombre de caractères à 12
        self.player_age = QtWidgets.QLineEdit(Bienvenue)
        self.player_age.setGeometry(QtCore.QRect(570, 130, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.player_age.setFont(font)
        self.player_age.setStyleSheet("background-color: rgba(0, 0, 0, 0);border-bottom: 2px solid rgba(200, 200, 200, 180);color: rgba(255, 255, 255,180);border-top: 0;border-left: 0;border-right: 0;padding-bottom: 7px;")
        self.player_age.setObjectName("player_age")
        self.player_age.setMaxLength(2)    # Fixer le nombre de caractères à 2
        self.player_genre = QtWidgets.QLabel(Bienvenue)
        self.player_genre.setGeometry(QtCore.QRect(330, 280, 111, 31))
        self.player_genre.setStyleSheet("color: rgba(255, 255, 255,180);font: 15pt \"MS Shell Dlg 2\";")
        self.player_genre.setObjectName("player_genre")
        self.gender_choice = QtWidgets.QComboBox(Bienvenue)
        self.gender_choice.setGeometry(QtCore.QRect(430, 280, 231, 31))
        self.gender_choice.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(100, 100, 100, 255));border: 1px solid #FFFFFF;border-radius: 5px;padding: 1px 18px 1px 3px;min-width: 6em;font-size: 12px;font: 13pt 'MS Shell Dlg 2';color: rgba(255, 255, 255,200);")
        self.gender_choice.addItems(["", "Masculin", "Feminin"])
        self.gender_choice.setObjectName("gender_choice")
        self.cancel = QtWidgets.QPushButton(Bienvenue)
        self.cancel.setGeometry(QtCore.QRect(310, 500, 201, 41))
        self.cancel.setStyleSheet("background-color: #CC0000;border: 1px solid #FFFFFF;border-radius: 5px; color: white;font: bold 14pt \'Arial\';box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.4);")
        self.cancel.setObjectName("play")
        self.cancel.clicked.connect(Bienvenue.close)
        self.play = QtWidgets.QPushButton(Bienvenue)
        self.play.setGeometry(QtCore.QRect(600, 500, 201, 41))
        self.play.setStyleSheet("background-color: #00CC00;border: 1px solid #FFFFFF;border-radius: 5px; color: white;\nfont: bold 14pt \'Arial\';box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.4);")
        self.play.setObjectName("play")
        self.editors = QtWidgets.QLabel(Bienvenue)
        self.editors.setGeometry(QtCore.QRect(20, 580, 251, 31))
        self.editors.setStyleSheet("color: rgba(255, 255, 255,50);font: 8pt \"Segoe UI Historic\";")
        self.editors.setObjectName("editors")
        self.retranslateUi(Bienvenue)
        QtCore.QMetaObject.connectSlotsByName(Bienvenue)

    def retranslateUi(self, Bienvenue):
       _translate = QtCore.QCoreApplication.translate
       Bienvenue.setWindowTitle(_translate("Bienvenue", "  POKEMON"))
       Bienvenue.setWindowIcon(QtGui.QIcon("../Images/Pokemon_logo.png"))
       self.welcome_message.setText(_translate("Bienvenue", ""))
       self.player_name.setPlaceholderText(_translate("Bienvenue", "Votre pseudo"))
       self.player_age.setPlaceholderText(_translate("Bienvenue", "Votre age"))
       self.player_genre.setText(_translate("Bienvenue", "Genre "))
       self.play.setText(_translate("Bienvenue", "JOUER"))
       self.cancel.setText(_translate("Bienvenue", "SORTIR"))
       self.editors.setText(_translate("Bienvenue", "By @yohan @marcel @ibrahima"))
       

