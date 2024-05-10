import sys
import random
import openpyxl
import json
import math
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QPixmap, QPainter, QColor, QFont
from PyQt6.QtCore import Qt


def distance(point1, point2):
    """
    Calcule la distance entre deux points.
    """
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


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
        coord_surete = [(13, 5.25), (13, 9), (4, 7.25),
                        (6, 2), (25, 0.75), (35, 0.75)]
        coord_choice = coord_surete[random.randint(0, len(coord_surete) - 1)]
        self.joueur = Joueur(coord_choice[0] / 2, 2 * coord_choice[1])

        # Création des Pokemons
        self.lespokemons = LesPokemons()
        self.pokemons_libres = self.lespokemons.extract_pokemons_libres(3)

        # Ajout des labels pour afficher les noms des Pokémons
        self.labels = {}
        for pokemon_name, info in self.lespokemons.pokemons.items():
            label = QLabel(pokemon_name, self)
            label.setStyleSheet("color: black")  # Changer la couleur du texte
            font = QFont()
            font.setPointSize(16)  # Changer 16 par la taille de police souhaitée
            label.setFont(font)
            label.setGeometry(
                round(info["x"] * 19.5),
                round(info["y"] * 78),
                100, 20
            )  # Position et taille du label
            self.labels[pokemon_name] = label

    def paintEvent(self, event):
        """
        Elle la carte, le joueur et les pokemons.
        """
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.drawPixmap(self.rect(), self.background_image)

        # Dessin du joueur
        painter.setPen(Joueur.COLOR)
        painter.setBrush(Joueur.COLOR)
        x = round(self.joueur.row * (self.width() - 2 * Carte.MARGIN) // Carte.GRID_SIZE + Carte.MARGIN)
        y = round(self.joueur.col * (self.height() - 2 * Carte.MARGIN) // Carte.GRID_SIZE + Carte.MARGIN)
        painter.drawEllipse(x, y, self.joueur.cell_size, self.joueur.cell_size)

        # Dessin des pokemons libres
        rayon = 10
        for pokemon_name, info in self.pokemons_libres.items():
            X = round(info['x'] * 19.5 + Carte.MARGIN)
            Y = round(info['y'] * 78 + Carte.MARGIN)
            painter.setPen(LesPokemons.COLORL)
            painter.setBrush(LesPokemons.COLORL)
            painter.drawEllipse(X, Y, rayon, rayon)

        # Dessin des pokemons sauvages
        for pokemon_name, info in self.lespokemons.pokemons.items():
            if not self.pokemons_libres.get(pokemon_name) and info['visible']:
                X = round(info['x'] * 19.5 + Carte.MARGIN)
                Y = round(info['y'] * 78 + Carte.MARGIN)
                painter.setPen(LesPokemons.COLORS)
                painter.setBrush(LesPokemons.COLORS)
                painter.drawEllipse(X, Y, rayon, rayon)

    def distance_joueur_pokemons(self):
        """
        Calcule la distance entre le joueur et tous les Pokémon.
        Retourne un dictionnaire avec les distances pour chaque Pokémon.
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
        if event.key() == Qt.Key.Key_Up:
            self.joueur.deplacer("haut")
        elif event.key() == Qt.Key.Key_Down:
            self.joueur.deplacer("bas")
        elif event.key() == Qt.Key.Key_Left:
            self.joueur.deplacer("gauche")
        elif event.key() == Qt.Key.Key_Right:
            self.joueur.deplacer("droite")
        self.lespokemons.show_nearest((2 * self.joueur.row, self.joueur.col / 2))
        self.repaint()


class Joueur:
    COLOR = QColor(255, 0, 0)  # Couleur rouge pour le joueur

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.cell_size = 20

    def deplacer(self, direction, step=0.5):
        """
        Déplace le joueur sur la carte en vérifiant les limites.
        """
        if direction == "haut" and self.col > 0:
            self.col -= step
        elif direction == "bas" and self.col < Carte.GRID_SIZE - 1:
            self.col += step
        elif direction == "gauche" and self.row > 0:
            self.row -= step
        elif direction == "droite" and self.row < Carte.GRID_SIZE - 1:
            self.row += step


class LesPokemons:
    COLORS = QColor(0, 0, 0)  # Couleur noire pour les Pokémons sauvages
    COLORL = QColor(255, 255, 255)  # Couleur blanche pour les Pokémons libres

    def __init__(self):
        self.pokemons = {}
        wb = openpyxl.load_workbook("essai.xlsx")
        sheet = wb.active
        for row in range(1, sheet.max_row + 1):
            cell1 = sheet.cell(row, 1)
            cell2 = sheet.cell(row, 2)
            pokemon_name = cell1.value
            x, y = json.loads(f"{cell2.value}")
            self.pokemons[pokemon_name] = {
                'x': x,
                'y': y,
                'visible': False
            }

    def extract_pokemons_libres(self, num_elements):
        if num_elements > len(self.pokemons):
            num_elements = min(num_elements, len(self.pokemons))
        selected_keys = random.sample(list(self.pokemons.keys()), num_elements)
        extracted_elements = {key: self.pokemons[key] for key in selected_keys}
        return extracted_elements

    def show_nearest(self, joueur_position):
        nearest_pokemon = None
        nearest_distance = 1  # float("Inf")
        for pokemon_name, info in self.pokemons.items():
            dist = distance(joueur_position, (info['x'], info['y']))
            if dist < nearest_distance:
                nearest_distance = dist
                nearest_pokemon = pokemon_name

        if nearest_pokemon:
            for pokemon_name, info in self.pokemons.items():
                if pokemon_name == nearest_pokemon:
                    info['visible'] = True
                else:
                    info['visible'] = False


def main():
    app = QApplication(sys.argv)
    window = Carte()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
