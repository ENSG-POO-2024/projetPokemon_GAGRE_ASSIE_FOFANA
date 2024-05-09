import sys
sys.path.append('../../Gestion_pokemon')
from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout
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
        # self.play.clicked.connect(self.change_window)

    def update_pseudo(self):
        pseudo = self.player_name.text()
        age = self.player_age.text()
        genre = self.gender_choice.currentText()
        
        self.player_profil = Window_Player_profil()
        
        # self.player_profil.dresseur = Dresseur(pseudo, genre)
        
        # print(self.player_profil.dresseur.nom)
        
        self.player_profil.show()
        self.close()
        
    
        

class Window_Player_profil (QMainWindow,Ui_Player_profil):
    def __init__(self, parent=None):
        super(Window_Player_profil, self).__init__(parent)
        self.setupUi(self)
        
        self.choix_pokemons.clicked.connect(self.afficher_inventaire)
        self.change_pokemon.clicked.connect(self.changement_combattants)
        self.close_window.clicked.connect(self.close)
        
        self.pokemons_combats=[] # Liste pour stocker les pokemons choisis
        # print(self.dresseur.nom)
        # print(self.dresseur.genre)

    def afficher_inventaire(self):
        self.inventaire_window = Window_Inventaire_Pokemon() # Ouvrir la fenêtre de l'inventaire des pokemons
        self.inventaire_window.tableWidget.cellClicked.connect(self.selectionner_pokemon)
        self.inventaire_window.show()

    def selectionner_pokemon(self, row, col):
        pokemon_selectionne = self.inventaire_window.tableWidget.cellWidget(row, col).layout().itemAt(1).widget().text()    # Récupérer le nom du pokemon sélectionné dans le tableau
        if len(self.pokemons_combats) == 3:
            print("La liste de vos pokemons est pleine")
        if pokemon_selectionne not in self.pokemons_combats: # Vérifier si le pokemon sélectionné n'est pas déjà dans la liste des pokemons choisis
            self.pokemons_combats.append(pokemon_selectionne) # Ajouter le pokemon sélectionné dans la liste des pokemons choisis
            # Mettre à jour les labels avec les pokemons choisis
            if len(self.pokemons_combats) == 1:
                self.pokemon_1.setPixmap(QtGui.QPixmap("../Images/Pokemon_images/" + pokemon_selectionne.replace("'","")+".png").scaled(141, 101))
            elif len(self.pokemons_combats) == 2:
                self.pokemon_2.setPixmap(QtGui.QPixmap("../Images/Pokemon_images/" + pokemon_selectionne.replace("'","")+".png").scaled(141, 101))
            elif len(self.pokemons_combats) == 3:
                self.pokemon_3.setPixmap(QtGui.QPixmap("../Images/Pokemon_images/" + pokemon_selectionne.replace("'","")+".png").scaled(141, 101))

    def changement_combattants(self):
        self.pokemons_combats = [] # Vider la liste de pokemon la liste de pokemon
        self.pokemon_1.setPixmap(QtGui.QPixmap(""))
        self.pokemon_1.setText("1er choix")
        self.pokemon_2.setPixmap(QtGui.QPixmap(""))
        self.pokemon_2.setText("2ème choix")
        self.pokemon_3.setPixmap(QtGui.QPixmap(""))
        self.pokemon_3.setText("3ème choix")

class Window_Inventaire_Pokemon (QMainWindow,Ui_Inventaire_Pokemon):
    def __init__(self, parent=None):
        super(Window_Inventaire_Pokemon, self).__init__(parent)
        self.setupUi()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    Accueil = Window_Bienvenue()
    Accueil.show()
    sys.exit(app.exec_())