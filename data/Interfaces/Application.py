# -*- coding: utf-8 -*-
"""
Created on Tue May  7 20:13:38 2024

@author: Hp Probook i7
"""



import sys
import random as rd
sys.path.append('../../Gestion_pokemon/')
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QMainWindow, QApplication, QMessageBox, QAction,
                             QDialog, QVBoxLayout, QPushButton, QLabel)

from Capture_pokemon import Ui_Capture_pokemon
from Combat_perdu import Ui_Combat_perdu
from Lancement_combat import Ui_Lancement_combat
from Zone_de_bataille import Ui_Zone_de_bataille
from Victoire_combat import Ui_Victoire_combat
from Selection_pokemon import Ui_Selection_pokemon
from Player_profil import Ui_Player_profil
from Bienvenue import Ui_Bienvenue
from Inventaire_Pokemon import Ui_Inventaire_Pokemon
from Classes_Pokemons import *
from Navigation_Interface import Carte, Personnage
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

####################################################################################################################

################################               Bienvenue                    ################################

####################################################################################################################

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
        self.pokemons_combats= self.joueur.pokemons_combats # Liste pour stocker les pokemons choisis
        self.close_window.clicked.connect(self.change_window)
        
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
                else :
                    self.pokemons_combats = []
                    
                self.joueur.pokemons_combats=self.pokemons_combats
                print(self.pokemons_combats)



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
    
    def change_window(self):
        self.next_window =  Window_Carte (self)
        self.next_window.show()
        self.close()
    
    def close_window(self):
        self.close()

class Window_Inventaire_Pokemon (QMainWindow,Ui_Inventaire_Pokemon):
    def __init__(self,Profil, parent=None):
        super(Window_Inventaire_Pokemon, self).__init__(parent)
        self.setupUi()
        self.profil =Profil
        self.joueur = Profil.joueur
        self.pokemons_attrapes =self.joueur.pokemons_attrapes
        self.pokemons_a_trouver =self.joueur.pokemons_a_trouver
        self.tableWidget = QtWidgets.QTableWidget()
        num_rows = len(Profil.joueur.pokemons_attrapes) // 17 + 1
        num_cols = len(Profil.joueur.pokemons_attrapes) if len(Profil.joueur.pokemons_attrapes) < 17 else 17
        self.tableWidget.setRowCount(num_rows)
        self.tableWidget.setColumnCount(num_cols)
        self.resize(1033, 580)
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
        self.sortir_button = QtWidgets.QPushButton("Cliquez ici pour sortir")
        self.sortir_button.setStyleSheet("background-color: rgb(255,110,100); color: rgb(0,0,0); font: 75 10pt \"Arial\"")
        self.layout.addWidget(self.sortir_button)
        self.sortir_button.clicked.connect(self.close)
        
        
##############################################################

             ########## Music ###########

##############################################################
class music():
    
    def play_music(self):
        if self.music_url:
            self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(self.music_url)))
            self.media_player.play()

    def stop_music(self):
        self.media_player.stop()
        
        
##############################################################

             ########## Carte ###########     

##############################################################
        

class Window_Carte (Carte):
    def __init__(self, Profil ): 
        super( ).__init__()
        
        self.joueur = Profil.joueur
        self.pokemons_libres =self.joueur.pokemons_libres
        self.pokemons_sauvages= self.joueur.pokemons_sauvages
        self.pokemons_hors_map=  self.joueur.pokemons_hors_map
        self.pokemon_adversaire= None
        self.create_menu()
        if len(self.joueur.pokemons_a_trouver) == 0:
            self.fin_de_jeu()
###############################################################################################

###############################  Message de fin de Jeu  ###############################

###############################################################################################
    def fin_de_jeu(self):
        
        self.fin = QDialog(self)
        self.fin.setWindowTitle("  ")
        self.fin.setFixedSize(700,300)
        self.fin.setWindowTitle("  POKEMON")
        self.fin.setWindowIcon(QtGui.QIcon("../Images/Pokemon_logo.png"))
        dialog_layout = QVBoxLayout(self.fin)
        fin_label = QLabel()
        fin_label.setPixmap(QtGui.QPixmap("../Images/Fin_Jeu.jpg").scaled(781, 661))
        fin_label.setScaledContents(True)
        dialog_layout.addWidget(fin_label)
        self.sortir = QPushButton("Acceuil")
        self.sortir.clicked.connect(self.reinitialisation)
        dialog_layout.addWidget(self.sortir, alignment= QtCore.Qt.AlignmentFlag.AlignCenter)
        self.fin.exec()
            
    def reinitialisation(self):
        print("Ici")
        self.relancer=Window_Bienvenue()
        self.relancer.show()
        self.fin.close()
        self.close()
        
        
###############################################################################################
    def recherche_pokemon(self, Personnage_position):
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
        
        pokemons = self.pokemons_sauvages+self.pokemons_libres
        for pokemon_nom in pokemons:
            pokemon = Dresseur.get_pokemon(pokemon_nom)
            position= pokemon.Coordonnees
            dist = Window_Carte.distance(Personnage_position, (position[0], position[1]))
            # Mise à jour du Pokémon le plus proche si la nouvelle distance est plus petite
            if dist < nearest_distance:
                nearest_distance = dist
                nearest_pokemon = pokemon
       
        if nearest_pokemon != None:
            self.pokemon_adversaire = nearest_pokemon
            nearest_pokemon = None
            confirm_box = QMessageBox()
            confirm_box.setIcon(QMessageBox.Icon.Question)
            confirm_box.setWindowTitle("Alerte !")
            confirm_box.setText(f"Vous êtes dans la zone de combat de {self.pokemon_adversaire.nom}\nVoulez-cous le combattre ou fuir ?")
            confirm_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            confirm_box.setStyleSheet("QMessageBox {background-color: #ffcccc;}"
                                      "QMessageBox QLabel {color: #800000; font-weight: bold;}"
                                      "QMessageBox QPushButton {background-color: #ff6666; color: #fff; padding: 5px 15px; border-radius: 5px; border: 1px solid #ff6666;}"
                                      "QMessageBox QPushButton:hover {background-color: #ff4747;}")
            # Modifier le texte des boutons
            confirm_box.button(QMessageBox.StandardButton.Yes).setText("Combattre")
            confirm_box.button(QMessageBox.StandardButton.No).setText("Fuir")
            reponse = confirm_box.exec()
            if reponse == QMessageBox.StandardButton.Yes:
                self.change_window()
            else:
                self.pokemon_adversaire=None
                player_position = rd.sample(self.coord_surete, k=1)[0]
                self.Personnage.row, self.Personnage.row = int(player_position[0] /2), 2* int(player_position[1] )
                self.update()
            
    
            
    def display_developpers(self):
        dialog = QDialog(self)
        dialog.setFixedSize(300, 150)
        dialog.setWindowTitle("  POKEMON")
        dialog.setWindowIcon(QtGui.QIcon("../Images/Pokemon_logo.png"))
        dialog_layout = QVBoxLayout(dialog)
        developers_label = QLabel()
        developers_label.setText("Yohan GAGRE\nIbrahima FOFANA\nMarcel ASSIE")
        developers_label.setStyleSheet("background-color: rgba(0, 255, 0, 100); color: black; font-size: 16px; font-weight: bold; border-radius: 10px; padding: 10px;")
        developers_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        dialog_layout.addWidget(developers_label)
        sortir = QPushButton("Fermer")
        sortir.clicked.connect(dialog.close)
        dialog_layout.addWidget(sortir, alignment= QtCore.Qt.AlignmentFlag.AlignCenter)
        dialog.exec()

                    
    def distance(point1, point2):
        """
        Calcule la distance entre deux points.

        Args:
            point1 (tuple): Coordonnées du premier point.
            point2 (tuple): Coordonnées du deuxième point.

        Returns:
            float: La distance entre les deux points.
        """
        return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)**0.5
               
    def paintEvent(self, event):
        """
           Redessine la carte, le joueur et les Pokémon.

           Args:
                event (QPaintEvent): L'événement de redessin.

           Returns:
                  None
    """
        # Crée un objet QPainter pour dessiner sur la fenêtre
        painter =QtGui.QPainter(self)
        # Active l'antialiasing pour des dessins plus lisses
        painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)
        # Dessine l'image d'arrière-plan sur toute la fenêtre
        painter.drawPixmap(self.rect(), self.background_image)

        # Dessin du joueur
        x = round(self.Personnage.row * (self.width() - 2 * Carte.MARGIN) // Carte.GRID_SIZE + Carte.MARGIN)
        y = round(self.Personnage.col * (self.height() - 2 * Carte.MARGIN) // Carte.GRID_SIZE + Carte.MARGIN)
        painter.drawPixmap(x, y, self.Personnage.sizeJ, self.Personnage.sizeJ, self.Personnage.image)

        # le facteur d'echelle pour convertir les coordoonnées du fichier en coordonnées pixelisées.
        # Coordonnée maximun dans le fichier : x = 40 et y = 10.
        self.echelleX = (self.width() - 2 * Carte.MARGIN) / 40
        self.echelleY = (self.height() - 2 * Carte.MARGIN) / 10

        # Dessin des pokemons libres
        for pokemon_libre in self.pokemons_libres:
            pokemon = Dresseur.get_pokemon(pokemon_libre)
            position = pokemon.Coordonnees
            X = round(position[0] * self.echelleX)
            Y = round(position[1] * self.echelleY)
            painter.drawPixmap(X, Y, 30, 30, QtGui.QPixmap(pokemon.Image))

        # Dessin des pokemons sauvages
        if self.pokemon_adversaire != None and self.pokemon_adversaire.nom in self.pokemons_sauvages:
            coord = self.pokemon_adversaire.Coordonnees
            X = round(coord[0] * self.echelleX)
            Y = round(coord[1] * self.echelleY)
            painter.drawPixmap(X, Y, 30, 30, QtGui.QPixmap(self.pokemon_adversaire.Image))
        
        
    def create_menu(self):
        # Création d'une action pour quitter
        profil_view = QtWidgets.QAction("Voir profil", self)
        profil_view.triggered.connect(self.return_profil)

        developpers = QtWidgets.QAction("Voir les developpeurs", self)
        developpers.triggered.connect(self.display_developpers)

        # Création d'un menu
        menu = self.menuBar()
        menu.setStyleSheet("background-color: transparent;")
        fichier_menu = menu.addMenu(QtGui.QIcon("../Images/menu.png"),"Menu")
        fichier_menu.addAction(profil_view)
        fichier_menu.addAction(developpers)
        
    def keyPressEvent(self, event):
        """
            Gère les événements de pression de touche.

            Args:
                event: L'événement de pression de touche.

            """
        # Déplace le joueur en fonction de la touche pressée

        if event.key() == QtCore.Qt.Key.Key_Up:
            self.Personnage.deplacer("haut")
        elif event.key() == QtCore.Qt.Key.Key_Down:
            self.Personnage.deplacer("bas")
        elif event.key() == QtCore.Qt.Key.Key_Left:
            self.Personnage.deplacer("gauche")
        elif event.key() == QtCore.Qt.Key.Key_Right:
            self.Personnage.deplacer("droite")
        # Affiche le Pokémon le plus proche du joueur
        self.recherche_pokemon((2 * self.Personnage.row, self.Personnage.col / 2))
        # Actualise l'affichage de la carte
        self.repaint()
        
    def change_window(self):
        self.next_window = Window_Lancement_combat (self)
        self.next_window.show()
        self.close()
        
    def return_profil(self):
        self.back_window = Window_Player_profil(self)
        self.back_window.show()
        
##############################################################

             ########## Lancement ###########     

##############################################################

class Window_Lancement_combat (QMainWindow,Ui_Lancement_combat):
    def __init__(self,Carte, parent=None): #Joueur, pokemon_adversaire, liste_pokemons_combattants
        super(Window_Lancement_combat, self).__init__(parent)
        self.setupUi(self)
        self.joueur= Carte.joueur
        self.pokemon_adversaire= Carte.pokemon_adversaire
        self.Combattants=self.joueur.pokemons_combats
        self.Zone_d_attente()
        self.acteur_combat()
        self.PASS.clicked.connect(self.change_window)
        
    def Zone_d_attente(self) :
        self.pokemons_zone_attente = [Dresseur.dict_pokemons[self.Combattants[0]],
                                      Dresseur.dict_pokemons[self.Combattants[1]],
                                      Dresseur.dict_pokemons[self.Combattants[2]]]

    def close_window(self):
        self.close()

    def change_window(self):
        self.next_window = Window_Selection_pokemon (self)
        self.next_window.show()

    def acteur_combat(self):
         
        pokemons =self.pokemons_zone_attente
        self.Nom_Pokemon_1.setText(pokemons[0].nom)
        self.Nom_Pokemon_2.setText(pokemons[1].nom)
        self.Nom_Pokemon_3.setText(pokemons[2].nom)
        self.Pokemon_1.setPixmap(QtGui.QPixmap( pokemons[0].Image))
        self.Pokemon_2.setPixmap(QtGui.QPixmap( pokemons[1].Image))
        self.Pokemon_3.setPixmap(QtGui.QPixmap( pokemons[2].Image))
        self.Adversaire.setPixmap(QtGui.QPixmap(self.pokemon_adversaire.Image))
        self.Nom_adversaire.setText(self.pokemon_adversaire.nom)
        self.Type_1.setPixmap(QtGui.QPixmap("../Images/Types/"+self.pokemon_adversaire.type1+".png"))
        self.Type_2.setPixmap(QtGui.QPixmap("../Images/Types/"+self.pokemon_adversaire.type2+".png"))
        self.Type_3.setPixmap(QtGui.QPixmap("../Images/Types/"+pokemons[0].type1+".png"))
        self.Type_4.setPixmap(QtGui.QPixmap("../Images/Types/"+pokemons[0].type2+".png"))
        self.Type_5.setPixmap(QtGui.QPixmap("../Images/Types/"+pokemons[1].type1+".png"))
        self.Type_6.setPixmap(QtGui.QPixmap("../Images/Types/"+pokemons[1].type2+".png"))
        self.Type_7.setPixmap(QtGui.QPixmap("../Images/Types/"+pokemons[2].type1+".png"))
        self.Type_8.setPixmap(QtGui.QPixmap("../Images/Types/"+pokemons[2].type2+".png"))
        self.Joueur.setPixmap(QtGui.QPixmap(self.joueur.Image))
        
        
##############################################################

             ########## Selection ###########     OK Besoin de lancement

##############################################################

class Window_Selection_pokemon (QMainWindow,Ui_Selection_pokemon):
    def __init__(self,lancement, parent=None):
        super(Window_Selection_pokemon, self).__init__(parent)
        self.setupUi(self)
        self.pokemons_zone_attente= lancement.pokemons_zone_attente
        self.affichage()
        self.joueur = lancement.joueur
        self.pokemon_adversaire= lancement.pokemon_adversaire
        self.Pokemon_1_etat= False
        self.Pokemon_2_etat= False
        self.Pokemon_3_etat= False
        self.lancement=lancement
        self.Pokemon_1.clicked.connect(self.press_Pokemon_1)
        self.Pokemon_2.clicked.connect(self.press_Pokemon_2)
        self.Pokemon_3.clicked.connect(self.press_Pokemon_3)
        self.Pokemon_1.clicked.connect(self.choix_pokemon_attaquant)
        self.Pokemon_2.clicked.connect(self.choix_pokemon_attaquant)
        self.Pokemon_3.clicked.connect(self.choix_pokemon_attaquant)

    def press_Pokemon_1(self):
        self.Pokemon_1_etat =True
        
    def press_Pokemon_2(self):
        self.Pokemon_2_etat =True
        
    def press_Pokemon_3(self):
        self.Pokemon_3_etat =True
        
    def choix_pokemon_attaquant(self):
        Combattants = self.pokemons_zone_attente
        if self.Pokemon_1_etat ==True:
            self.pokemon_zone_combat= Combattants[0]
        elif self.Pokemon_2_etat ==True:
            self.pokemon_zone_combat= Combattants[1]
        elif self.Pokemon_3_etat ==True:
            self.pokemon_zone_combat= Combattants[2]
        self.next_window = Window_Zone_de_bataille(self)
        self.next_window.show()
        self.close()
        self.lancement.close_window()
        
    def affichage(self):
        Combattants = self.pokemons_zone_attente
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(Combattants[0].Image), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Pokemon_1.setIcon(icon1)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(Combattants[1].Image), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Pokemon_2.setIcon(icon2)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(Combattants[2].Image), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Pokemon_3.setIcon(icon3)


##############################################################

             ########## Combat ###########

##############################################################
        
class Window_Zone_de_bataille (QMainWindow,Ui_Zone_de_bataille):
    def __init__(self, selection, parent=None):
        
        super(Window_Zone_de_bataille, self).__init__(parent)
        self.setupUi(self)
        self.pokemons_zone_attente= selection.pokemons_zone_attente
        self.pokemon_zone_combat= selection.pokemon_zone_combat
        self.pokemon_zone_adversaire= selection.pokemon_adversaire
        self.joueur= selection.joueur
        
        self.pokemons_zone_repos=[]
        self.progress_bar_attaquant = QtWidgets.QProgressBar(self)
        self.progress_bar_attaquant.setGeometry(QtCore.QRect(252, 215, 150, 15))
        self.progress_bar_attaquant.setTextVisible(False)
        self.progress_bar_attaquant.setStyleSheet("QProgressBar::chunk { background-color: rgb(255, 46, 46); }")
        self.progress_bar_adversaire = QtWidgets.QProgressBar(self)
        self.progress_bar_adversaire.setGeometry(QtCore.QRect(693, 215, 150, 15))
        self.progress_bar_adversaire.setTextVisible(False)
        self.progress_bar_adversaire.setStyleSheet("QProgressBar::chunk { background-color: rgb(255, 46, 46); }")
        
        self.acteur_combat()
        self.affichage_HP()
        
        self.KO= False
        self.fuir_etat=False
        self.Pokemon_1_etat= False
        self.Pokemon_2_etat= False
        self.Pokemon_3_etat= False
        self.type_1_etat =False
        self.type_2_etat=False
        self.Neutre_etat=False
        self.Echange_etat=False
        self.fin_combat=False
        
        self.Pokemon_1.clicked.connect(self.press_Pokemon_1)
        self.Pokemon_2.clicked.connect(self.press_Pokemon_2)
        self.Pokemon_3.clicked.connect(self.press_Pokemon_3)
        self.Type1.clicked.connect(self.press_type_1)
        self.Type2.clicked.connect(self.press_type_2)
        self.Neutre.clicked.connect(self.press_neutre)
        self.Type1.clicked.connect( self.press_type_1)
        self.Type2.clicked.connect( self.press_type_2)
        self.Fuir.clicked.connect( self.press_fuir)
        self.lance_echange_pokemon()
        self.Neutre.clicked.connect(self.attaque_neutre)
        self.Type1.clicked.connect(self.attaque_elementaire)
        self.Type2.clicked.connect(self.attaque_elementaire)
        self.Fuir.clicked.connect(self.fuite)
        self.debut_combat = QtCore.QTimer()
        self.combat()
        

        
    def acteur_combat(self):
        Combattants = self.pokemons_zone_attente
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(Combattants[0].Image), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Pokemon_1.setIcon(icon1)
        
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(Combattants[1].Image), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Pokemon_2.setIcon(icon2)
        
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(Combattants[2].Image), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Pokemon_3.setIcon(icon3)
        
        self.Pokemon_attaquant.setPixmap(QtGui.QPixmap(self.pokemon_zone_combat.Image))
        self.Nom_attaquant.setText(self.pokemon_zone_combat.nom)
        
        for bouton in [self.Pokemon_1,self.Pokemon_2,self.Pokemon_3]:
            icon = bouton.icon().pixmap(bouton.icon().availableSizes()[0]).cacheKey()
            image =self.Pokemon_attaquant.pixmap().cacheKey()
            if image == icon:
                bouton.setStyleSheet("background-color: rgba(255, 77, 61, 0.3)")
                bouton.setEnabled(False)

        self.Type1.setIcon(QtGui.QIcon("../Images/Types/"+self.pokemon_zone_combat.type1+".png"))
        self.Type2.setIcon(QtGui.QIcon("../Images/Types/"+self.pokemon_zone_combat.type2+".png"))
        
        if self.pokemon_zone_combat.type2 == "null":
            self.Type2.setStyleSheet("background-color: rgba(255, 77, 61, 0.3)")
            self.Type2.setEnabled(False)
            
        self.Type1_adversaire.setPixmap(QtGui.QPixmap("../Images/Types/"+self.pokemon_zone_adversaire.type1+".png"))
        self.Type2_adversaire.setPixmap(QtGui.QPixmap("../Images/Types/"+self.pokemon_zone_adversaire.type2+".png"))
        self.Adversaire.setPixmap(QtGui.QPixmap(self.pokemon_zone_adversaire.Image))
        self.Nom_adversaire.setText(self.pokemon_zone_adversaire.nom)
        
        self.Joueur.setPixmap(QtGui.QPixmap(self.joueur.Image))
        
        
    def affichage_HP(self):
        self.Nom_attaquant.setText(self.pokemon_zone_combat.nom)
        self.PV_adversaire.setText(str(self.pokemon_zone_adversaire.HP_combat)+" / "+str(self.pokemon_zone_adversaire.HP))
        self.PV_attaquant.setText(str(self.pokemon_zone_combat.HP_combat)+" / "+str(self.pokemon_zone_combat.HP)) 
        
        self.progress_bar_attaquant.setMaximum(self.pokemon_zone_combat.HP)
        self.progress_bar_attaquant.setValue(self.pokemon_zone_combat.HP_combat)
        
        self.progress_bar_adversaire.setMaximum(self.pokemon_zone_adversaire.HP)
        self.progress_bar_adversaire.setValue(self.pokemon_zone_adversaire.HP_combat)
        
    def press_Pokemon_1(self):
        self.Pokemon_1_etat =True
        if self.KO:
            self.remplacement()
            self.Pokemon_1_etat =False
        self.lance_echange_pokemon()
        

    def press_Pokemon_2(self):
        self.Pokemon_2_etat =True
        if self.KO:
            self.remplacement()
            self.Pokemon_2_etat =False
        self.lance_echange_pokemon()
        
    def press_Pokemon_3(self):
        self.Pokemon_3_etat =True
        if self.KO:
            self.remplacement()
            self.Pokemon_3_etat =False
        self.lance_echange_pokemon()
    
    def press_neutre(self):
        self.Neutre_etat =True
        
    def press_type_1(self):
        self.type_1_etat = "actif"
        
    def press_type_2(self):
        self.type_2_etat = "actif"
        
    def press_fuir (self):
        self.fuir_etat=True
        
    def lance_echange_pokemon(self):
        if self.Pokemon_1_etat or self.Pokemon_2_etat or self.Pokemon_3_etat:
            self.Echange_etat= True
            self.Echange.setEnabled(True)
        else:
            self.Echange.setEnabled(False)
   
    def echange_pokemon(self):
        
        if self.Echange_etat:
            for bouton in [self.Pokemon_1,self.Pokemon_2,self.Pokemon_3]:
                icon = bouton.icon().pixmap(bouton.icon().availableSizes()[0]).cacheKey()
                image =self.Pokemon_attaquant.pixmap().cacheKey()
                if icon == image:
                    bouton.setStyleSheet("background-color: transparent")
                    bouton.setEnabled(True) 
        if self.Pokemon_1_etat :
            self.pokemon_zone_combat= self.pokemons_zone_attente[0]
            self.Pokemon_1_etat =False
            
        elif self.Pokemon_2_etat :
            self.pokemon_zone_combat= self.pokemons_zone_attente[1]
            self.Pokemon_2_etat =False
            
        elif self.Pokemon_3_etat :
            self.pokemon_zone_combat= self.pokemons_zone_attente[2]
            self.Pokemon_3_etat =False
            
        self.Pokemon_attaquant.setPixmap(QtGui.QPixmap(self.pokemon_zone_combat.Image))
        self.acteur_combat()
        if self.pokemon_zone_combat.type2 != "null":
            self.Type2.setStyleSheet("background-color:rgb(255, 255, 255)")
            self.Type2.setEnabled(True)
        self.Echange.setEnabled(False)
        self.Echange_etat=False

    def fuite(self):
       if self.fuir_etat :
            self.Defaite()
            
    def restaure_HP(self):
        for pokemon in self.pokemons_zone_attente:
            pokemon.HP_combat =pokemon.HP
        
    def Victoire(self):   
        if self.pokemon_zone_adversaire.HP_combat==0:
            self.pokemons_zone_attente[0]
            self.restaure_HP()
            self.pokemon_zone_adversaire.HP_combat=self.pokemon_zone_adversaire.HP
            self.next_window=Window_Victoire_combat(self)
            self.fin_combat=True
            
            self.next_window.show()
            

    def Defaite(self): 
        if len(self.pokemons_zone_repos) ==3 or self.fuir_etat:
            self.restaure_HP()
            self.pokemon_zone_adversaire.HP_combat=self.pokemon_zone_adversaire.HP
            self.next_window=Window_Combat_perdu(self)
            self.next_window.show()
            self.fin_combat=True
            
    def attaque_neutre(self):
        if self.Neutre_etat:
           Dommage = self.pokemon_zone_combat.attaque_neutre(self.pokemon_zone_adversaire)
           self.Degats.setText(Dommage)
           self.Degats_attaquant.setPixmap(QtGui.QPixmap("../Images/Explosion.png"))
           self.info_combat()
        self.Neutre_etat=False
        self.affichage_HP()
        self.Victoire()
        
    def attaque_elementaire(self):
        if self.type_1_etat =="actif":
            Dommage =self.pokemon_zone_combat.attaque_elementaire(self.pokemon_zone_adversaire, False)
            self.Degats.setText(Dommage)
            self.Degats_attaquant.setPixmap(QtGui.QPixmap("../Images/Attaques/"+str(self.pokemon_zone_combat.type1)+".png"))
            self.info_combat()
            self.type_1_etat =False
        if self.type_2_etat =="actif":
            Dommage = self.pokemon_zone_combat.attaque_elementaire(self.pokemon_zone_adversaire, True)
            self.Degats.setText(Dommage)
            self.Degats_attaquant.setPixmap(QtGui.QPixmap("../Images/Attaques/"+str(self.pokemon_zone_combat.type2)+".png"))
            self.info_combat()
            self.type_2_etat=False
        self.affichage_HP()
        self.Victoire()    
        return Dommage

    def info_combat(self):
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.nettoyage)
        self.timer.start(3500)
        
    def nettoyage(self):
        self.Degats_attaquant.clear()
        self.Degats.clear()
        self.Degats_adversaire.clear()
        self.timer.stop()   

    def degats_elementaires(self,Dommage,booleen):
        if booleen:
            self.Degats.setText(Dommage)
            self.Degats_adversaire.setPixmap(QtGui.QPixmap("../Images/Attaques/"+str(self.pokemon_zone_combat.type2)+".png"))
            self.info_combat()
        else:
            
            self.Degats.setText(Dommage)
            self.Degats_adversaire.setPixmap(QtGui.QPixmap("../Images/Attaques/"+str(self.pokemon_zone_combat.type1)+".png"))
            self.info_combat()
        
    def attaque_adversaire(self):
        choix= [True, False]
        if rd.choice(choix):
            Dommage = self.pokemon_zone_adversaire.attaque_neutre(self.pokemon_zone_combat)
            self.Degats.setText(Dommage)
            self.Degats_adversaire.setPixmap(QtGui.QPixmap("../Images/Explosion.png"))
            self.info_combat()
            
        else:
            if self.pokemon_zone_adversaire.type2 == 'null':
                Dommage = self.pokemon_zone_adversaire.attaque_elementaire(self.pokemon_zone_combat, False)
                self.degats_elementaires(Dommage, False)
            else:
                elementaire =rd.choice(choix)
                Dommage = self.pokemon_zone_adversaire.attaque_elementaire(self.pokemon_zone_combat,elementaire )
                self.degats_elementaires(Dommage, elementaire)
        self.compteur += 1 
        self.affichage_HP()
        self.pokemon_KO()
        self.Defaite()
           
    
        
    def pokemon_KO(self):
        liste_boutons = [self.Pokemon_1,self.Pokemon_2,self.Pokemon_3]
        liste_labels = [self.Pokemon_KO_1, self.Pokemon_KO_2, self.Pokemon_KO_3]
        if self.pokemon_zone_combat.HP_combat == 0:
            for numero in range(len(liste_boutons)):
                bouton = liste_boutons[numero]
                icon = bouton.icon().pixmap(bouton.icon().availableSizes()[0]).cacheKey()
                image =self.Pokemon_attaquant.pixmap().cacheKey()
                if icon == image:
                    pokemon = self.pokemons_zone_attente[numero]
                    label = liste_labels[numero]
                    image =QtGui.QImage(pokemon.Image).convertToFormat(QtGui.QImage.Format_Grayscale8)
                    pixmap = QtGui.QPixmap.fromImage(image)
                    label.setPixmap(pixmap)
                    self.pokemons_zone_repos.append(pokemon)
            self.KO= True
         
    def  remplacement(self):
        if self.KO==True:
            if self.Pokemon_1_etat :
                self.pokemon_zone_combat= self.pokemons_zone_attente[0]
                self.Pokemon_1.setEnabled(False)
                self.Pokemon_1.setStyleSheet("background-color: rgba(255, 77, 61, 0.3)")
                self.Pokemon_1_etat =False
                
            elif self.Pokemon_2_etat :
                self.pokemon_zone_combat= self.pokemons_zone_attente[1]
                self.Pokemon_2.setEnabled(False)
                self.Pokemon_2.setStyleSheet("background-color: rgba(255, 77, 61, 0.3)")
                self.Pokemon_2_etat =False
                
            elif self.Pokemon_3_etat :
                self.pokemon_zone_combat= self.pokemons_zone_attente[2]
                self.Pokemon_3.setEnabled(False)
                self.Pokemon_3.setStyleSheet("background-color: rgba(255, 77, 61, 0.3)")
                self.Pokemon_3_etat =False
                
        if self.pokemon_zone_combat.type2 == "null":
            self.Type2.setIcon(QtGui.QIcon("../Images/Types/"+self.pokemon_zone_combat.type2+".png"))
            self.Type2.setStyleSheet("background-color: rgba(255, 77, 61, 0.3)")
            self.Type2.setEnabled(False)
        else:
            self.Type2.setIcon(QtGui.QIcon("../Images/Types/"+self.pokemon_zone_combat.type2+".png"))
            self.Type2.setEnabled(True)
            
        self.Type1.setIcon(QtGui.QIcon("../Images/Types/"+self.pokemon_zone_combat.type1+".png"))
        self.Pokemon_attaquant.setPixmap(QtGui.QPixmap(self.pokemon_zone_combat.Image))
        self.affichage_HP()
        self.KO= False

    
    def vitesse(self):
        if self.pokemon_zone_combat.Speed >= self.pokemon_zone_adversaire.Speed:
            return True
        else:
            return False
        
    def close_window(self):
        self.close()
        
    def tour_joueur(self):
        if self.Neutre_etat:
            self.attaque_neutre()
                 
        elif self.fuir_etat:
            self.fuite()
               
        elif self.Echange_etat :
            self.echange_pokemon()
               
        elif self.type_1_etat == "actif":
            self.attaque_elementaire()
            
        elif  self.type_2_etat == "actif":
            self.attaque_elementaire()
            
        self.compteur += 1 
        
        
    def Action_utilisateur(self):
        loop = QtCore.QEventLoop()  # Crée une boucle d'événements
        Action = False

        # Fonction pour gérer le clic du bouton
        def Action_joueur():
            nonlocal Action
            
            Action = True
            loop.quit()  
        self.Type1.clicked.connect(Action_joueur)
        self.Type2.clicked.connect(Action_joueur)
        self.Neutre.clicked.connect(Action_joueur)
        self.Type1.clicked.connect( Action_joueur)
        self.Type2.clicked.connect( Action_joueur)
        self.Fuir.clicked.connect( Action_joueur)
        self.Echange.clicked.connect(Action_joueur)
        self.show()
        loop.exec_()
        
        return Action
       
    # Long mais marche
    def combat(self):
        rapidite = self.vitesse()
        self.compteur = 1
        if rapidite:
            # QMessageBox.information(self,"   POKEMON", "Vous jouer en première position \nBonne chance  !")
            
            while self.fin_combat!= True :
                if self.compteur % 2 != 0 :
                    
                    Action= self.Action_utilisateur()
                    if Action:
                        self.timer = QtCore.QTimer(self)
                        self.timer.timeout.connect(self.tour_joueur)
                        self.timer.start(3500)
                else:
                    self.timer = QtCore.QTimer(self)
                    self.timer.timeout.connect(self.attaque_adversaire)
                    self.timer.start(3500)
                    
            
                if self.fin_combat:
                    break
        else:
            # QMessageBox.information(self,"   POKEMON", "Votre adversaire joue en première position\nBonne chance  !")
            while  self.fin_combat != True:
                if self.compteur % 2 != 0 :
                    self.timer = QtCore.QTimer(self)
                    self.timer.timeout.connect(self.attaque_adversaire)
                    self.timer.start(3500)
                else:
                    Action= self.Action_utilisateur()
                    if Action:
                        self.timer = QtCore.QTimer(self)
                        self.timer.timeout.connect(self.tour_joueur)
                        self.timer.start(3500)
                if self.fin_combat:
                    break
                
    # Court avec bug
    # def combat(self):
    #     rapidite = self.vitesse()
    #     if rapidite:
    #         print("1")
   #          self.debut_combat.start(5000)
    #         while self.fuir_etat != True or self.fin_combat != True:
    #             self.Action_utilisateur()
    #             self.tour_joueur()
    #             self.attaque_adversaire()
                
    #             if self.fin_combat:
    #                 break
                
    #             print(self.fuir_etat)
    #             print (self.fin_combat)
    #     else:
    #         print("2")
              #self.debut_combat.start(5000)
    #         while self.fuir_etat != True or self.fin_combat != True:
    #             self.attaque_adversaire()
    #             self.Action_utilisateur()
    #             self.tour_joueur()
    #             if self.fin_combat:
    #                 break
                
    #             print(self.fuir_etat)
    #             print (self.fin_combat)

##############################################################

             ########## Resultat ###########

##############################################################

class Window_Combat_perdu (QMainWindow,Ui_Combat_perdu):  #  OK Besoin de carte
    def __init__(self, Zone_de_bataille, parent=None):
        super(Window_Combat_perdu, self).__init__(parent)
        self.setupUi(self)
        self.Bataille= Zone_de_bataille
        self.PASS.clicked.connect(self.change_window)
        
    def change_window(self):
        self.next_window = Window_Carte (self.Bataille)
        self.next_window.show()
        self.Bataille.close_window()
        self.close()
        
        
class Window_Victoire_combat (QMainWindow,Ui_Victoire_combat ):  
    def __init__(self, Zone_de_bataille, parent=None):
        super(Window_Victoire_combat, self).__init__(parent)
        self.setupUi(self)
        self.Bataille= Zone_de_bataille
        self.PASS.clicked.connect(self.change_window)
        
    def change_window(self):
        self.next_window = Window_Capture_pokemon (self.Bataille)
        self.next_window.show()
        self.Bataille.close_window()
        self.close()
        
        
#############################################################

             ######### Capture ###########      OK Besoin de carte

#############################################################

class Window_Capture_pokemon(QMainWindow,Ui_Capture_pokemon):
    def __init__(self, Bataille, parent=None):
        super(Window_Capture_pokemon, self).__init__(parent)
        self.setupUi(self)
        self.joueur= Bataille.joueur
        self.pokemon_adversaire =  Bataille.pokemon_zone_adversaire
        self.Capture()
        self.PASS.clicked.connect(self.change_window)
        
        
    def change_window(self):
        self.next_window = Window_Carte (self)
        self.next_window.show()
        self.close()
        
    def Capture(self):
        self.joueur.attrape_pokemon(self.pokemon_adversaire)
        self.joueur.ajout_pokemon_sauvages()
        self.Nom_pokemon.setText(self.pokemon_adversaire.nom)
        self.Pokemon_Attrape.setPixmap(QtGui.QPixmap(self.pokemon_adversaire.Image))
        
if __name__ == "__main__":
##############################################################

             ########## Jeu ###########

##############################################################

    def run_app():
        app = QApplication(sys.argv)
        mainWin = Window_Bienvenue()
        mainWin.show()
        app.exec_()
    fenetre=run_app()
    
    