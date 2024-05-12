import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor, QPixmap
from PyQt6.QtCore import Qt
import random as rd

class GameWindow(object):
    def setupUi(self):
        # Paramètres de la fenêtre principale
        self.carte_size_x = 1033 # Dimension x
        self.carte_size_y = 580 # Dimension y
        self.setGeometry(100, 100, self.carte_size_x, self.carte_size_y)
        self.setWindowTitle("Test")
        self.setFixedSize(self.carte_size_x,self.carte_size_y) # Fixation de la taille de l'écran
        # Calcul de du facteur d'échelle
        x_max, y_max = 40,10
        self.echelle_x, self.echelle_y = self.carte_size_x/x_max, self.carte_size_y/y_max

        # Coordonnées de suretés (Ce sont les coordonnées brutes)
        coord_surete = [[33, 2], [23, 1], [28, 7],[17, 6], [38, 8], [25, 4]]

        # Positions du joueur
        player_position = rd.sample(coord_surete, k=1)[0]
        # J'applique le facteur d'échelle aux coordonnées brutes pour que ça soit représentatif
        self.player_x = int(player_position[0]*self.echelle_x)
        self.player_y = int(player_position[1]*self.echelle_y)

        pokemon_name = ["Abra","Aerodactyl","Alakazam","Arbok","Arcanine"] # Echantillon de 5 pokemons saisie à la main
        pokemons_coord = [[5, 8], [20, 3], [10, 5], [35, 9], [15, 2]]  # Coordonnées brutes inventées
        self.pokemons = {}
        # Je stocke les pokemons et leurs coordonnées
        for i in range(len(pokemons_coord)):
            self.pokemons[pokemon_name[i]] = pokemons_coord[i]


