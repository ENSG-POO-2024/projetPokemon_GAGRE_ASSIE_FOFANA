import sys
import random
import openpyxl
import json
import math
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPixmap, QPainter
from PyQt6.QtCore import Qt


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
        # Taille minimale de la fenêtre
        self.setMinimumSize(Carte.SCREEN_WIDTH, Carte.SCREEN_HEIGHT)

        # Charger l'image d'arrière-plan
        self.background_image = QPixmap("../Images/background/background.jpeg")

        # Création du joueur

        # Définition des coordonnées sûres où le joueur peut apparaître initialement
        coord_surete = [(13, 5.25), (13, 9), (4, 7.25),
                        (6, 2), (25, 0.75), (35, 0.75)]
        # Choix aléatoire d'une paire de coordonnées parmi celles définies dans coord_surete
        coord_choice = coord_surete[random.randint(0, len(coord_surete) - 1)]
        # Les coordonnées sont ajustées avant d'être passées pour positionner le joueur correctement sur la carte
        self.joueur = Joueur(coord_choice[0] / 2, 2 * coord_choice[1])

        # Création des Pokemons
        # Instanciation des de la classe LesPokemons
        self.lespokemons = LesPokemons()
        # Extraction des pokemons libres
        # L'argument 10 spécifie le nombre de pokemons libres à extraire
        self.pokemons_libres = self.lespokemons.extract_pokemons_libres(10)

        # Chargement des images des Pokémons sous forme de dictionnaire.
        # Indice recupération : le nom du Pokemon qui correspond au nom de son image.
        self.pokemon_images = {}
        for pokemon_name in self.lespokemons.pokemons:
            image_path = f"../Images/Pokemon_images/{pokemon_name}.PNG"
            self.pokemon_images[pokemon_name] = QPixmap(image_path)

    def paintEvent(self, event):
        """
           Redessine la carte, le joueur et les Pokémon.

           Args:
                event (QPaintEvent): L'événement de redessin.

           Returns:
                  None
    """
        # Crée un objet QPainter pour dessiner sur la fenêtre
        painter = QPainter(self)
        # Active l'antialiasing pour des dessins plus lisses
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        # Dessine l'image d'arrière-plan sur toute la fenêtre
        painter.drawPixmap(self.rect(), self.background_image)

        # Dessin du joueur
        x = round(self.joueur.row * (self.width() - 2 * Carte.MARGIN) // Carte.GRID_SIZE + Carte.MARGIN)
        y = round(self.joueur.col * (self.height() - 2 * Carte.MARGIN) // Carte.GRID_SIZE + Carte.MARGIN)
        painter.drawPixmap(x, y, self.joueur.sizeJ, self.joueur.sizeJ, self.joueur.image)

        # le facteur d'echelle pour convertir les coordoonnées du fichier en coordonnées pixelisées.
        # Coordonnée maximun dans le fichier : x = 40 et y = 10.
        echelleX = (self.width() - 2 * Carte.MARGIN) / 40
        echelleY = (self.height() - 2 * Carte.MARGIN) / 10

        # Dessin des pokemons libres
        for pokemon_name, coord in self.pokemons_libres.items():
            X = round(coord['x'] * echelleX)
            Y = round(coord['y'] * echelleY)
            painter.drawPixmap(X, Y, self.lespokemons.sizeP, self.lespokemons.sizeP, self.pokemon_images[pokemon_name])

        # Dessin des pokemons sauvages
        for pokemon_name, coord in self.lespokemons.pokemons.items():
            if not self.pokemons_libres.get(pokemon_name) and coord['visible']:
                X = round(coord['x'] * echelleX)
                Y = round(coord['y'] * echelleY)
                painter.drawPixmap(X, Y, self.lespokemons.sizeP, self.lespokemons.sizeP,
                                   self.pokemon_images[pokemon_name])

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


class Joueur:

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


class LesPokemons:

    def __init__(self):
        super().__init__()
        self.sizeP = 20
        self.pokemons = {}
        # Chargement du classeur Excel contenant les coordonnées des Pokémons
        wb = openpyxl.load_workbook("../Donnees_crees/pokemon_coordinates_P.xlsx")
        # Sélection de la feuille active dans le classeur Excel
        sheet = wb.active
        # Sélectionner un échantillon aléatoire de 30 éléments parmi tous les éléments du fichier Excel
        selected_rows = random.sample(range(1, sheet.max_row + 1), 30)
        # Parcours des lignes sélectionnées pour extraire les données des coordonnées des Pokémons
        for row in selected_rows:
            cell1 = sheet.cell(row, 1)  # Nom du Pokémon
            cell2 = sheet.cell(row, 2)  # Coordonnées du Pokémon
            pokemon_name = cell1.value
            # désérialisation des coordonnées : reconvertir le flux d'octets d'un fichier binaire en un objet Python
            x, y = json.loads(cell2.value)
            # Ajout des coordonnées du Pokémon à la liste des Pokémons avec visibilité initialement définie sur False.
            self.pokemons[pokemon_name] = {
                'x': x,
                'y': y,
                'visible': False
            }

    def extract_pokemons_libres(self, num_elements):
        """
            Extrait un nombre donné d'éléments de la liste des pokemons.

            Args:
                num_elements (int): Le nombre d'éléments à extraire.

            Returns:
                dict: Un dictionnaire contenant les éléments extraits.
            """
        # Si le nombre d'éléments demandé est supérieur à la taille de la liste des pokemons,
        # on ajuste le nombre d'éléments à extraire pour qu'il corresponde à la taille de la liste.
        if num_elements > len(self.pokemons):
            num_elements = min(num_elements, len(self.pokemons))
        # Sélectionne au hasard un ensemble de clés (noms de pokemons) de la liste des pokemons
        # en nombre égal à num_elements.
        selected_keys = random.sample(list(self.pokemons.keys()), num_elements)
        # Crée un nouveau dictionnaire contenant uniquement les éléments correspondant aux clés sélectionnées.
        extracted_elements = {key: self.pokemons[key] for key in selected_keys}
        return extracted_elements

    def show_nearest(self, joueur_position):
        """
            Met à jour la visibilité du Pokémon le plus proche du joueur.

            Args:
                joueur_position (tuple): Les coordonnées du joueur.

            Returns:
                None
            """
        # Initialisation des variables pour le Pokémon le plus proche
        nearest_pokemon = None
        # On donne le seuil de comparaion
        nearest_distance = 1
        for pokemon_name, info in self.pokemons.items():
            dist = distance(joueur_position, (info['x'], info['y']))
            # Mise à jour du Pokémon le plus proche si la nouvelle distance est plus petite
            if dist < nearest_distance:
                nearest_distance = dist
                nearest_pokemon = pokemon_name
        # Mise à jour de la visibilité des pokemons
        if nearest_pokemon:
            for pokemon_name, info in self.pokemons.items():
                # Le Pokémon le plus proche est rendu visible, les autres invisibles
                if pokemon_name == nearest_pokemon:
                    info['visible'] = True
                else:
                    info['visible'] = False


# Programme Principal
def main():
    app = QApplication(sys.argv)
    window = Carte()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
