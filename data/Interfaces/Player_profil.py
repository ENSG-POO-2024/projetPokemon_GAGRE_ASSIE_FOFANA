from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Player_profil(object):
    def setupUi(self, Player_profil):
        Player_profil.setObjectName("Player_profil")
        self.setFixedSize(809, 691)
        self.player_information = QtWidgets.QLabel(Player_profil)
        self.player_information.setGeometry(QtCore.QRect(180, 12, 450, 61))
        self.player_information.setStyleSheet("color: rgb(255, 255, 255);font: 81 20pt \"Rockwell Extra Bold\";")
        self.player_information.setAlignment(QtCore.Qt.AlignCenter)
        self.player_information.setObjectName("player_information")
        self.name = QtWidgets.QLabel(Player_profil)
        self.name.setGeometry(QtCore.QRect(40, 100, 200, 41))
        self.name.setStyleSheet("color: rgb(255, 255, 255); font: 75 16pt \"Berlin Sans FB Demi\";")
        self.name.setObjectName("name")
        self.age = QtWidgets.QLabel(Player_profil)
        self.age.setGeometry(QtCore.QRect(40, 160, 171, 41))
        self.age.setStyleSheet("color: rgb(255, 255, 255); font: 75 16pt \"Berlin Sans FB Demi\";")
        self.age.setObjectName("age")
        self.pokemons_combat = QtWidgets.QLabel(Player_profil)
        self.pokemons_combat.setGeometry(QtCore.QRect(210, 270, 361, 41))
        self.pokemons_combat.setStyleSheet("color: rgb(255, 255, 255);border-color: rgb(85, 255, 255);font: 81 14pt \"Rockwell Extra Bold\";")
        self.pokemons_combat.setAlignment(QtCore.Qt.AlignCenter)
        self.pokemons_combat.setObjectName("pokemons_combat")
        self.pseudo = QtWidgets.QLabel(Player_profil)
        self.pseudo.setGeometry(QtCore.QRect(280, 100, 501, 41))
        self.pseudo.setStyleSheet("color: rgba(255, 255, 255, 255);font: 75 16pt \"Berlin Sans FB Demi\";")
        self.pseudo.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.pseudo.setObjectName("pseudo")
        self.age_input = QtWidgets.QLabel(Player_profil)
        self.age_input.setGeometry(QtCore.QRect(280, 160, 391, 41))
        self.age_input.setStyleSheet("color: rgba(255, 255, 255, 255); font: 75 16pt \"Berlin Sans FB Demi\";")
        self.age_input.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.age_input.setObjectName("age_input")
        self.line = QtWidgets.QFrame(Player_profil)
        self.line.setGeometry(QtCore.QRect(10, 250, 781, 5))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setStyleSheet("color: rgb(255, 255, 255);")
        self.line.setLineWidth(5)  # Définit l'épaisseur de la ligne à 5 pixels
        self.choix_pokemons = QtWidgets.QPushButton(Player_profil)
        self.choix_pokemons.setGeometry(QtCore.QRect(140, 490, 521, 81))
        self.choix_pokemons.setStyleSheet("background-color: rgb(85, 170, 0); font: 24pt \"Rockwell Condensed\";color: rgb(255, 255, 255);")
        self.choix_pokemons.setObjectName("choix_pokemons")
        self.change_pokemon = QtWidgets.QPushButton(Player_profil)
        self.change_pokemon.setGeometry(QtCore.QRect(250, 600, 300, 40))
        self.change_pokemon.setStyleSheet("background-color: rgb(85, 170, 0); font: 14pt \"Sitka\";color: rgb(255, 255, 255);")
        self.change_pokemon.setObjectName("choix_pokemons")
        self.close_window = QtWidgets.QPushButton(Player_profil)
        self.close_window.setGeometry(QtCore.QRect(690, 638, 93, 28))
        self.close_window.setStyleSheet("background-color: rgb(255, 255, 255); font: 10pt \"MS Shell Dlg 2\";color: rgb(0, 0, 0);border-radius: 5px;")
        self.close_window.setObjectName("Fermer")
        self.background = QtWidgets.QLabel(Player_profil)
        self.background.setGeometry(QtCore.QRect(10, 10, 781, 661))
        self.background.setPixmap(QtGui.QPixmap("../Images/background/background_2.png").scaled(781, 661))
        self.background.setObjectName("background")
        self.profil_photo = QtWidgets.QLabel(Player_profil)
        self.profil_photo.setGeometry(QtCore.QRect(540, 80, 200, 140))
        self.profil_photo.setStyleSheet("border: 2px solid rgb(0, 180, 0); border-radius: 10px;")
        self.profil_photo.setObjectName("profil_photo")
        self.pokemon_1 = QtWidgets.QLabel(Player_profil)
        self.pokemon_1.setGeometry(QtCore.QRect(125, 340, 170, 130))
        self.pokemon_1.setStyleSheet("border: 2px solid rgba(255, 255, 255,100); border-radius: 5px;")
        self.pokemon_1.setObjectName("pokemon_1")
        self.pokemon_2 = QtWidgets.QLabel(Player_profil)
        self.pokemon_2.setGeometry(QtCore.QRect(315, 340, 170, 130))
        self.pokemon_2.setStyleSheet("color: rgba(255, 255, 255, 160);font: 75 14pt \"Neue Haas Grotesk Text Pro Blac\";")
        self.pokemon_2.setStyleSheet("border: 2px solid rgba(255, 255, 255,100); border-radius: 5px;")
        self.pokemon_2.setObjectName("pokemon_2")
        self.pokemon_3 = QtWidgets.QLabel(Player_profil)
        self.pokemon_3.setGeometry(QtCore.QRect(505, 340, 170, 130))
        self.pokemon_3.setStyleSheet("color: rgba(255, 255, 255, 160);font: 75 14pt \"Neue Haas Grotesk Text Pro Blac\";")
        self.pokemon_3.setStyleSheet("border: 2px solid rgba(255, 255, 255,100); border-radius: 5px;")
        self.pokemon_3.setObjectName("pokemon_3")
        self.background.raise_()
        self.player_information.raise_()
        self.name.raise_()
        self.age.raise_()
        self.pokemons_combat.raise_()
        self.pseudo.raise_()
        self.age_input.raise_()
        self.line.raise_()
        self.choix_pokemons.raise_()
        self.profil_photo.raise_()
        self.pokemon_1.raise_()
        self.pokemon_2.raise_()
        self.pokemon_3.raise_()
        self.change_pokemon.raise_()
        self.close_window.raise_()
        self.retranslateUi(Player_profil)
        QtCore.QMetaObject.connectSlotsByName(Player_profil)

    def retranslateUi(self, Player_profil):
       _translate = QtCore.QCoreApplication.translate
       Player_profil.setWindowTitle(_translate("Player_profil", "  POKEMON"))
       Player_profil.setWindowIcon(QtGui.QIcon("../Images/Pokemon_logo.png"))
       self.player_information.setText(_translate("Player_profil", "PLAYER INFORMATION"))
       self.name.setText(_translate("Player_profil", "Player pseudo   :"))
       self.age.setText(_translate("Player_profil", "Age    :"))
       self.pokemons_combat.setText(_translate("Player_profil", "POKEMONS DE COMBAT"))
       self.pseudo.setText(_translate("Player_profil    ", ""))
       self.age_input.setText(_translate("Player_profil", ""))
       self.choix_pokemons.setText(_translate("Player_profil", "Choisir vos pokemons de combats"))
       self.change_pokemon.setText(_translate("Player_profil", "Changer de combattants"))
       self.pokemon_1.setText(_translate("Player_profil", "1er choix"))
       self.pokemon_2.setText(_translate("Player_profil", "2ème choix"))
       self.pokemon_3.setText(_translate("Player_profil", "3ème choix"))
       self.close_window.setText(_translate("Player_profil", "Fermer"))
