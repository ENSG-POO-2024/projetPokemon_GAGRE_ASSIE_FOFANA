import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QLabel
from PyQt6.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt


class Carte(QMainWindow):
    MARGIN = 10
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 800
    CordSupX = 100
    CordSupY = 100
    GRID_SIZE = 20

    def __init__(self):
        super().__init__()
        self.setWindowTitle("POKEMON")
        self.setMinimumSize(Carte.SCREEN_WIDTH, Carte.SCREEN_HEIGHT)

        # Charger l'image d'arrière-plan
        self.background_image = QPixmap("Images/BackgroundImage.jpeg")

        # Création du joueur
        rows = random.randint(0, Carte.GRID_SIZE-1)
        cols = random.randint(0, Carte.GRID_SIZE-1)
        self.joueur = Joueur(rows, cols)

    def paintEvent(self, event):
        """
        Elle dessine le joueur.
        """
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.drawPixmap(self.rect(), self.background_image)
        painter.setPen(Joueur.COLOR)
        painter.setBrush(Joueur.COLOR)

        # Calculer les coordonnées du coin supérieur gauche de l'ellipse
        x = self.joueur.row * (self.width() - 2 * Carte.MARGIN) // Carte.GRID_SIZE + Carte.MARGIN
        y = self.joueur.col * (self.height() - 2 * Carte.MARGIN) // Carte.GRID_SIZE + Carte.MARGIN

        # Dessiner l'ellipse centrée sur les coordonnées calculées
        painter.drawEllipse(x, y, self.joueur.cell_size, self.joueur.cell_size)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Up:
            self.joueur.deplacer("haut")
        elif event.key() == Qt.Key_Down:
            self.joueur.deplacer("bas")
        elif event.key() == Qt.Key_Left:
            self.joueur.deplacer("gauche")
        elif event.key() == Qt.Key_Right:
            self.joueur.deplacer("droite")
        self.repaint()  # Redessine la fenêtre après le déplacement du joueur


class Joueur:
    COLOR = QColor(255, 0, 0)  # On choisit une couleur pour le joueur : Rouge

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.cell_size = 20

    def deplacer(self, direction, step=1):
        """
        Elle permet de déplacer le joueur sur la grille ou la carte en vérifiant que le joueur ne sort pas de la zone
        du jeu. direction: la direction dans laquelle le joueur se déplace
        """
        # Logique de déplacement
        if direction == "haut" and self.col > 0:
            self.col -= step
        elif direction == "bas" and self.col < Carte.GRID_SIZE - 1:
            self.col += step
        elif direction == "gauche" and self.row > 0:
            self.row -= step
        elif direction == "droite" and self.row < Carte.GRID_SIZE - 1:
            self.row += step
        elif direction == "haut-gauche" and self.col > 0 and self.row > 0:
            self.col -= step
            self.row -= step
        elif direction == "haut-droite" and self.col > 0 and self.row < Carte.GRID_SIZE - 1:
            self.col -= step
            self.row += step
        elif direction == "bas-gauche" and self.col < Carte.GRID_SIZE - 1 and self.row > 0:
            self.col += step
            self.row -= step
        elif direction == "bas-droite" and self.col < Carte.GRID_SIZE - 1 and self.row < Carte.GRID_SIZE - 1:
            self.col += step
            self.row += step


def main():
    app = QApplication(sys.argv)
    window = Carte()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
