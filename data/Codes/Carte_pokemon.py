import sys
import random as rd
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap, QPainter, QIcon
from PyQt5.QtCore import Qt


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
        self.coord_surete = [(30, 3.5), (19, 4), (27, 7.75),
                        (3, 3.75), (12, 9.5), (38, 0)]
        # Choix aléatoire d'une paire de coordonnées parmi celles définies dans coord_surete
        self.coord_choice = self.coord_surete[rd.randint(0, len(self.coord_surete) - 1)]
        # Les coordonnées sont ajustées avant d'être passées pour positionner le joueur correctement sur la carte

# Programme Principal
def main():
    app = QApplication(sys.argv)
    window = Carte()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
