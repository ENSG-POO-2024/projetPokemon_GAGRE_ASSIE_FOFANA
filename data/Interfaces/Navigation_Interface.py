import sys
import random
import openpyxl
import json
import math
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap, QPainter,QIcon
    
from PyQt5.QtCore import Qt



def distance(point1, point2):
    """
    Calcule la distance entre deux points.

    Args:
        point1 (tuple): Coordonnées du premier point.
        point2 (tuple): Coordonnées du deuxième point.

    Returns:
        float: La distance entre les deux points.
    """
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


class Carte(QMainWindow):
    MARGIN = 10  # Marge autour de la carte
    SCREEN_WIDTH = 1033  # Largeur de la fenêtre de la carte
    SCREEN_HEIGHT = 580  # Hauteur de la fenêtre de la carte
    GRID_SIZE = 20  # Taille d'une grille de la carte

    def __init__(self):
        super().__init__()
        self.setWindowTitle("POKEMON")
        self.setWindowIcon(QIcon("../Images/Pokemon_logo.png"))
        # Taille minimale de la fenêtre
        self.setMinimumSize(Carte.SCREEN_WIDTH, Carte.SCREEN_HEIGHT)

        # Charger l'image d'arrière-plan
        self.background_image = QPixmap("../Images/background/background_player.png")

        # Création du joueur

        # Définition des coordonnées sûres où le joueur peut apparaître initialement
        self.coord_surete = [(13, 5.25), (13, 9), (4, 7.25),
                        (6, 2), (25, 0.75), (35, 0.75)]
        # Choix aléatoire d'une paire de coordonnées parmi celles définies dans coord_surete
        self.coord_choice = self.coord_surete[random.randint(0, len(self.coord_surete) - 1)]
        # Les coordonnées sont ajustées avant d'être passées pour positionner le joueur correctement sur la carte
        self. Personnage = Personnage(self.coord_choice[0] / 2, 2 * self.coord_choice[1])

    def distance_joueur_pokemons(self):
        """
    Calcule la distance entre le joueur et tous les Pokémons(sauges et libres) sur la carte.
    Retourne un dictionnaire avec les distances pour chaque Pokémon.

    Returns:
        dict: Un dictionnaire contenant les distances entre le joueur et chaque Pokémon.
    """
        distances = {}
        joueur_position = (2 * self.joueur.row, self.joueur.col / 2)
        for pokemon_name, info in self.lespokemons.pokemons.items():
            pokemon_position = (info['x'], info['y'])
            dist = distance(joueur_position, pokemon_position)
            print(dist)
            distances[pokemon_name] = dist
        return distances

    def keyPressEvent(self, event):
        """
            Gère les événements de pression de touche.

            Args:
                event: L'événement de pression de touche.

            """
        # Déplace le joueur en fonction de la touche pressée

        if event.key() == Qt.Key.Key_Up:
            self.joueur.deplacer("haut")
        elif event.key() == Qt.Key.Key_Down:
            self.joueur.deplacer("bas")
        elif event.key() == Qt.Key.Key_Left:
            self.joueur.deplacer("gauche")
        elif event.key() == Qt.Key.Key_Right:
            self.joueur.deplacer("droite")
        # Affiche le Pokémon le plus proche du joueur
        self.lespokemons.show_nearest((2 * self.joueur.row, self.joueur.col / 2))
        # Actualise l'affichage de la carte
        self.repaint()


class Personnage:

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.sizeJ = 40
        self.image = QPixmap("../Images/Pion.png")  # Chargement de l'image du joueur

    def deplacer(self, direction, step=0.5):
        """
             Déplace le joueur sur la carte en vérifiant les limites.

             Args:
                direction (str): La direction du déplacement (haut, bas, gauche, droite).
                step (float): Le pas de déplacement.

    """
        if direction == "haut" and self.col > 0:
            self.col -= step
        elif direction == "bas" and self.col < Carte.GRID_SIZE - 1:
            self.col += step
        elif direction == "gauche" and self.row > 0:
            self.row -= step
        elif direction == "droite" and self.row < Carte.GRID_SIZE - 1:
            self.row += step


# Programme Principal
def main():
    app = QApplication(sys.argv)
    window = Carte()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
