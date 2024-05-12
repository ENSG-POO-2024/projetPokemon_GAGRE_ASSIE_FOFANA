import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.QtGui import QPainter, QColor, QPixmap
from PyQt6.QtCore import Qt
import random as rd
import math as m

class GameWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Paramètres de la fenêtre principale
        self.carte_size_x = 1033 # Dimension x
        self.carte_size_y = 630 # Dimension y
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

    @staticmethod
    def distance(A,B):
        dist = m.sqrt((A[0]-B[0])**2 + (A[1]-B[1])**2)
        return dist



    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Bon j'ai mis le fond vert juste pour voir les images correcetement qu'en blanc
        painter.fillRect(event.rect(), QColor(255, 255, 255))

        # J'affiche le joueur sur la carte. Bon je l'ai redimensionner
        pixmap = QPixmap("../Images/Pion.png").scaled(40,50)  # scaled(taille_x,taille_y) redimensionne l'image
        painter.drawPixmap(self.player_x, self.player_y, pixmap)  #


        # Afficher les pokemons sur la carte
        for name,coords in self.pokemons.items():
            # J'affiche les pokemons en appliquant le facteur d'échelle aux coordonnées brutes pour que ça soit représentatif
            x,y = int(coords[0]*self.echelle_x), int(coords[1]*self.echelle_y)
            pixmap = QPixmap("../Images/Pokemon_images/"+name+".png").scaled(40,50)
            painter.drawPixmap(x, y, pixmap)
            # J'ajoute leur position précise pour voir leur emplacement précis puisque l'image est trop grande
            self.circle_radius = 60
            pen = painter.pen()
            pen.setColor(QColor(255, 0, 0))  # Rouge
            painter.setPen(pen)
            painter.drawEllipse(x - self.circle_radius, y - self.circle_radius, 2 * self.circle_radius, 2 * self.circle_radius)


    def keyPressEvent(self, event):
        self.step = 5 # Pas de déplacement du joueur
        self.margin = 5 # Marge de gauche et du haut
        self.margin_right = -35 # Marge de droite. J'ai moi même ajouté cela parce que l'image du joueur est plus grosse,que sa position réelle.
        self.margin_down = -55 # Marge de du bas. Explication : Pareil
        if event.key() == Qt.Key.Key_Up:
            if self.player_y > self.margin:
                self.player_y -= self.step
        elif event.key() == Qt.Key.Key_Down:
            if self.player_y < self.height() - self.margin + self.margin_down:
                self.player_y += self.step
        elif event.key() == Qt.Key.Key_Left:
            if self.player_x > self.margin:
                self.player_x -= self.step
        elif event.key() == Qt.Key.Key_Right:
            if self.player_x < self.width() - self.margin + self.margin_right:
                self.player_x += self.step
        elif event.key() == Qt.Key.Key_Up and event.key() == Qt.Key.Key_Left:
            if self.player_y > self.margin and self.player_x > self.margin:
                self.player_y -= self.step
                self.player_x -= self.step
        elif event.key() == Qt.Key.Key_Up and event.key() == Qt.Key.Key_Right:
            if self.player_y > self.margin and self.player_x < self.width() - self.margin + self.margin_right:
                self.player_y -= self.step
                self.player_x += self.step
        elif event.key() == Qt.Key.Key_Down and event.key() == Qt.Key.Key_Left:
            if self.player_y < self.height() - self.margin + self.margin_down and self.player_x > self.margin:
                self.player_y += self.step
                self.player_x -= self.step
        elif event.key() == Qt.Key.Key_Down and event.key() == Qt.Key.Key_Right:
            if self.player_y < self.height() - self.margin + self.margin_down and self.player_x < self.width() - self.margin + self.margin_right:
                self.player_y += self.step
                self.player_x += self.step
        self.shownearest()
        self.update()

    def shownearest(self):
        seuil = self.circle_radius
        for name, coords in self.pokemons.items():
            x, y = int(coords[0] * self.echelle_x), int(coords[1] * self.echelle_y)
            dist = GameWindow.distance([x,y], [self.player_x, self.player_y])
            if dist <= seuil :
                confirm_box = QMessageBox()
                confirm_box.setIcon(QMessageBox.Icon.Critical)
                confirm_box.setWindowTitle("Alerte !")
                confirm_box.setText(f"Vous êtes dans la zone de combat de {name} \nLe mode combat est lancé !")
                confirm_box.setStyleSheet("QMessageBox {background-color: #ffcccc;}"
                                          "QMessageBox QLabel {color: #800000; font-weight: bold;}"
                                          "QMessageBox QPushButton {background-color: #ff6666; color: #fff; padding: 5px 15px; border-radius: 5px; border: 1px solid #ff6666;}"
                                          "QMessageBox QPushButton:hover {background-color: #ff4747;}")

                confirm_box.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GameWindow()
    window.show()
    sys.exit(app.exec())
