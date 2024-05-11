import sys
import os
sys.path.append('../../Gestion_pokemon')
from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QMessageBox
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5 import QtCore, QtGui, QtWidgets

from Player_profil import Ui_Player_profil
from Bienvenue import Ui_Bienvenue
from Inventaire_Pokemon import Ui_Inventaire_Pokemon
from Classes_Pokemons import *

class Window_Bienvenue (QMainWindow,Ui_Bienvenue):
    def __init__(self, parent=None):
        super(Window_Bienvenue, self).__init__(parent)
        self.setupUi(self)
        self.play.clicked.connect(self.update_pseudo)

    def update_pseudo(self):

        name = self.player_name.text()
        age_text = self.player_age.text()
        genre = self.gender_choice.currentText()
        self.joueur= Dresseur(name,genre)
        self.joueur.age=age_text
        self.joueur.choix_pokemons_combattants()
        self.joueur.pokemons_on_map()
        self.player_profil = Window_Player_profil(self)
        self.player_profil.show()
        self.close()




class Window_Player_profil (QMainWindow,Ui_Player_profil):
    def __init__(self,Bienvenue, parent=None):
        super(Window_Player_profil, self).__init__(parent)
        self.setupUi(self)
        self.joueur = Bienvenue.joueur
        self.choix_pokemons.clicked.connect(self.afficher_inventaire)
        self.change_pokemon.clicked.connect(self.changement_combattants)
        self.close_window.clicked.connect(self.close)
        self.pokemons_combats= self.joueur.pokemons_combats # Liste pour stocker les pokemons choisis
        self.pokemon_1.setPixmap(QtGui.QPixmap(Dresseur.dict_pokemons[self.pokemons_combats[0]].Image).scaled(141,101))
        self.pokemon_2.setPixmap(QtGui.QPixmap(Dresseur.dict_pokemons[self.pokemons_combats[1]].Image).scaled(141,101))
        self.pokemon_3.setPixmap(QtGui.QPixmap(Dresseur.dict_pokemons[self.pokemons_combats[2]].Image).scaled(141,101))

        if self.joueur.genre == "Masculin":
            self.profil_photo.setPixmap(QtGui.QPixmap(self.joueur.Image).scaled(200, 140))
        elif self.joueur.genre== "Feminin":
            self.profil_photo.setPixmap(QtGui.QPixmap(self.joueur.Image).scaled(200, 140))
        else:
            self.profil_photo.setPixmap(QtGui.QPixmap(self.joueur.Image).scaled(200, 130))
        self.pseudo.setText(self.joueur.nom)
        self.age_input.setText(self.joueur.age)

    def afficher_inventaire(self):
        self.inventaire_window = Window_Inventaire_Pokemon(self) # Ouvrir la fenêtre de l'inventaire des pokemons
        self.inventaire_window.tableWidget.cellClicked.connect(self.selectionner_pokemon)
        self.inventaire_window.show()

    def selectionner_pokemon(self, row, col):
        pokemon_selectionne = self.inventaire_window.tableWidget.cellWidget(row, col).layout().itemAt(1).widget().text()    # Récupérer le nom du pokemon sélectionné dans le tableau
        if len(self.pokemons_combats) < 3 and pokemon_selectionne not in self.pokemons_combats: # Vérifier si le pokemon sélectionné n'est pas déjà dans la liste des pokemons choisis
            self.pokemons_combats.append(pokemon_selectionne) # Ajouter le pokemon sélectionné dans la liste des pokemons choisis

            # Mettre à jour les labels avec les pokemons choisis
            if len(self.pokemons_combats) == 1:
                self.pokemon_1.setPixmap(QtGui.QPixmap("../Images/Pokemon_images/" + pokemon_selectionne.replace("'","")+".png").scaled(141, 101))
            elif len(self.pokemons_combats) == 2:
                self.pokemon_2.setPixmap(QtGui.QPixmap("../Images/Pokemon_images/" + pokemon_selectionne.replace("'","")+".png").scaled(141, 101))
            elif len(self.pokemons_combats) == 3:
                self.pokemon_3.setPixmap(QtGui.QPixmap("../Images/Pokemon_images/" + pokemon_selectionne.replace("'","")+".png").scaled(141, 101))
            if len(self.pokemons_combats) == 3:
                confirm_box = QMessageBox()
                confirm_box.setIcon(QMessageBox.Question)
                confirm_box.setWindowTitle("Validation de choix")
                confirm_box.setText(f"Voulez-vous valider ces 3 combattants : \n{self.pokemons_combats[0]}, {self.pokemons_combats[1]} et {self.pokemons_combats[2]} ?")
                confirm_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                confirm_box.setStyleSheet("QMessageBox {background-color: #fff;}"
                                       "QMessageBox QLabel {color: #000; font-weight: bold;}"
                                       "QMessageBox QPushButton {background-color: #388e3c; color: #fff; padding: 5px 15px; border-radius: 5px; border: 1px solid #388e3c;}"
                                       "QMessageBox QPushButton:hover {background-color: #43a047;}")
                yes_button = confirm_box.button(QMessageBox.Yes)
                yes_button.setText("Oui")
                no_button = confirm_box.button(QMessageBox.No)
                no_button.setText("Non")
                result = confirm_box.exec_()
                if result == QMessageBox.Yes:
                    self.inventaire_window.close()
                self.pokemons_combats = []

    def changement_combattants(self):
        self.pokemons_combats = [] # Vider la liste de pokemon la liste de pokemon
        self.pokemon_1.setPixmap(QtGui.QPixmap(""))
        self.pokemon_1.setText("1er choix")
        self.pokemon_1.setStyleSheet("color: rgba(255, 255, 255, 160); font: 75 14pt \"Neue Haas Grotesk Text Pro Blac\";border: 2px solid rgba(255, 255, 255,100); border-radius: 5px;")
        self.pokemon_2.setPixmap(QtGui.QPixmap(""))
        self.pokemon_2.setText("2ème choix")
        self.pokemon_2.setStyleSheet("color: rgba(255, 255, 255, 160); font: 75 14pt \"Neue Haas Grotesk Text Pro Blac\";border: 2px solid rgba(255, 255, 255,100); border-radius: 5px;")
        self.pokemon_3.setPixmap(QtGui.QPixmap(""))
        self.pokemon_3.setText("3ème choix")
        self.pokemon_3.setStyleSheet("color: rgba(255, 255, 255, 160); font: 75 14pt \"Neue Haas Grotesk Text Pro Blac\";border: 2px solid rgba(255, 255, 255,100); border-radius: 5px;")


class Window_Inventaire_Pokemon (QMainWindow,Ui_Inventaire_Pokemon):
    def __init__(self,Profil, parent=None):
        super(Window_Inventaire_Pokemon, self).__init__(parent)
        self.setupUi()
        self.joueur = Profil.joueur
        self.pokemons_attrapes =self.joueur.pokemons_attrapes
        self.pokemons_a_trouver =self.joueur.pokemons_a_trouver
        self.tableWidget = QtWidgets.QTableWidget()
        num_rows = len(Profil.joueur.pokemons_attrapes) // 17 + 1
        num_cols = len(Profil.joueur.pokemons_attrapes) if len(Profil.joueur.pokemons_attrapes) < 17 else 17
        self.tableWidget.setRowCount(num_rows)
        self.tableWidget.setColumnCount(num_cols)
        #self.showFullScreen()
        self.setFixedSize(1033, 580)
        window_geometry = self.frameGeometry()
        center_point = QApplication.desktop().availableGeometry().center()
        window_geometry.moveCenter(center_point)
        self.move(window_geometry.topLeft())
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        for i in range(len(self.pokemons_attrapes)):  # Remplir l'inventaire du joueur
            row = i // num_cols
            col = i % num_cols
            widget = QtWidgets.QWidget()  # Créer un widget pour contenir l'image et le nom
            layout = QtWidgets.QVBoxLayout(widget)
            image_label = QtWidgets.QLabel()  # Ajouter l'image
            image_path = Dresseur.dict_pokemons[self.pokemons_attrapes[i]].Image
            pixmap = QtGui.QPixmap(image_path).scaled(50, 50)  # Redimensionner l'image
            image_label.setPixmap(pixmap)
            layout.addWidget(image_label)
            name_label = QtWidgets.QLabel(self.pokemons_attrapes[i])  # Ajouter le nom de l'image
            layout.addWidget(name_label, alignment=QtCore.Qt.AlignHCenter)  # Centrer le nom
            self.tableWidget.setCellWidget(row, col, widget)  # Ajouter le widget à la cellule du tableau
        self.layout.addWidget(self.tableWidget)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(105)  # Augmenter la taille des cellules
        self.tableWidget.verticalHeader().setDefaultSectionSize(100)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Accueil = Window_Bienvenue()
    Accueil.show()
    sys.exit(app.exec_())