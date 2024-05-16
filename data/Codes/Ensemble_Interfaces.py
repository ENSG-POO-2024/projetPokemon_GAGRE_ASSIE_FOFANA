# -*- coding: utf-8 -*-
"""
Created on Tue May  7 20:13:38 2024

@author: Hp Probook i7
"""


# Import des differentes librairies et modules necessaires
import sys
import random as rd
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QMainWindow, QApplication, QMessageBox, QAction,
                             QDialog, QVBoxLayout, QPushButton, QLabel)

# Import des differentes interfaces construites
from Capture_pokemon import Ui_Capture_pokemon
from Combat_perdu import Ui_Combat_perdu
from Lancement_combat import Ui_Lancement_combat
from Zone_de_bataille import Ui_Zone_de_bataille
from Victoire_combat import Ui_Victoire_combat
from Selection_pokemon import Ui_Selection_pokemon
from Player_profil import Ui_Player_profil
from Bienvenue import Ui_Bienvenue
from Inventaire_Pokemon import Ui_Inventaire_Pokemon
from Carte_pokemon import Carte

# Import des classes pokemons et dresseur
from Classes_Pokemons import *

# Import de musique
import pygame

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
        
        

####################################################################################################################

################################               Bienvenue                    ################################

####################################################################################################################

class Window_Bienvenue (QMainWindow,Ui_Bienvenue):
    def __init__(self, parent=None):
        super(Window_Bienvenue, self).__init__(parent)
        self.setupUi(self)
        self.play.clicked.connect(self.update_pseudo)
        pygame.mixer.init()                                 # Initialisation de la musique
        pygame.mixer.music.set_volume(0.1)                  # Reglage du volume
        pygame.mixer.music.load("../Musique/bienvenue.mp3") # Chargement de la musique de bienvenue
        pygame.mixer.music.play(-1)                         # Repetition en boucle infinie

    def update_pseudo(self):
        name = self.player_name.text()
        age_text = self.player_age.text()
        genre = self.gender_choice.currentText()
        self.joueur= Dresseur(name,genre)
        self.joueur.age=age_text
        self.joueur.pokemons_on_map()
        pygame.mixer.music.pause()           #Arrêt de la musique de l'accueil
        self.player_profil = Window_Player_profil(self)
        self.player_profil.show()
        self.player_profil.musique_profil()  # Lancement de la musique du profil
        self.close()

class Window_Player_profil (QMainWindow,Ui_Player_profil):
    def __init__(self, Donnees, parent=None):
        super(Window_Player_profil, self).__init__(parent)
        self.setupUi(self)
        self.joueur = Donnees.joueur
        self.Carte = Donnees
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

    def musique_profil(self):
        pygame.mixer.music.load("../Musique/profil.mp3")
        pygame.mixer.music.play(-1)

    def afficher_inventaire(self):
        self.inventaire_window = Window_Inventaire_Pokemon(self) # Ouvrir la fenêtre de l'inventaire des pokemons
        self.inventaire_window.tableWidget.cellClicked.connect(self.selectionner_pokemon)
        self.inventaire_window.show()

    def selectionner_pokemon(self, row, col):
        pokemon_selectionne = self.inventaire_window.tableWidget.cellWidget(row, col).layout().itemAt(3).widget().text()    # Récupérer le nom du pokemon sélectionné dans le tableau
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
                confirm_box.setWindowIcon(QtGui.QIcon("../Images/Pokemon_logo.png"))
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
        
        """
        Fonction qui permet de retourner à la carte avec les donnees à jour

        """
        pygame.mixer.music.pause()                   # Arrêt de la musique du profil
        self.next_window =  Window_Carte (self)      # renvoie les donnees à l'interface suivante
        self.next_window.show()
        self.next_window.musique_carte()             # Lancement de la musique de la carte
        self.Carte.close()                           # Fermeture de la carte
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
        num_rows = len(Profil.joueur.pokemons_attrapes) // 17 + 1    # Ce calcul de nombre de lignes me pert de créer des cellules en focntion du nombre de pokemon attrapé
        num_cols = len(Profil.joueur.pokemons_attrapes) if len(Profil.joueur.pokemons_attrapes) < 17 else 17 # Pareil comme le nombre de lignes
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
            layout = QtWidgets.QGridLayout(widget)
            image_label = QtWidgets.QLabel()
            type1_label = QtWidgets.QLabel()  # Ajouter l'image
            type2_label = QtWidgets.QLabel()
            pokemon = Dresseur.dict_pokemons[self.pokemons_attrapes[i]]
            image_path = pokemon.Image
            pokemon_type1 = QtGui.QPixmap("../Images/Types/" + pokemon.type1 + ".png")
            pokemon_type2 = QtGui.QPixmap("../Images/Types/" + pokemon.type2 + ".png")
            pixmap = QtGui.QPixmap(image_path)  # Redimensionner l'image
            type1_label.setPixmap(pokemon_type1)
            type1_label.setScaledContents(True)
            type2_label.setPixmap(pokemon_type2)
            type2_label.setScaledContents(True)
            image_label.setPixmap(pixmap)
            image_label.setScaledContents(True)
            name_label = QtWidgets.QLabel(self.pokemons_attrapes[i])  # Ajouter le nom de l'image
            layout.addWidget(image_label, 0, 0, 2, 2)                 # Image de pokemon reparti sur 4 cases
            layout.addWidget(type1_label, 1, 2)                       # Type1 du pokemon sur le côté de l'image
            layout.addWidget(type2_label, 0, 2)                       # Type2 du pokemon sur le côté de l'image
            layout.addWidget(name_label, 2, 0, 1, 3,alignment=QtCore.Qt.AlignHCenter)  # Ajouter le nom centré sous l'image
            self.tableWidget.setCellWidget(row, col, widget)                           # Ajout du widget à la cellule du tableau
        self.layout.addWidget(self.tableWidget)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)  # Augmenter la taille des cellules
        self.tableWidget.verticalHeader().setDefaultSectionSize(110)

        # Ajout du bouton affinités de la table inventaire
        self.affinites = QtWidgets.QPushButton("Afficher la tableau des affinités")
        self.affinites.setStyleSheet( "background-color: rgb(255,255,255); color: rgb(0,0,0); font: bold 75 10pt \"Arial\"")      # Style du bouton
        self.layout.addWidget(self.affinites)    # Ajout du bouton à la table
        self.affinites.clicked.connect(self.tableau_affinites) # Action : lancer la fonction pour l'ouverture de la table des affinités
        # Ajout du bouton sortir de la table inventaire
        self.sortir_bouton = QtWidgets.QPushButton("Sortir")
        self.sortir_bouton.setStyleSheet("background-color: rgb(110,255,100); color: rgb(0,0,0); font: bold 75 10pt \"Arial\"")  # Style du bouton
        self.layout.addWidget(self.sortir_bouton)  # Ajout du bouton à la table
        self.sortir_bouton.clicked.connect(self.close) # Action : fermer la table


    def tableau_affinites(self):

        layout = QtWidgets.QVBoxLayout()    # Création du layout vertical
        affinites = QtWidgets.QLabel()      # Création du QLabel pour afficher le tableau des affinités
        affinites.setPixmap(QtGui.QPixmap("../Donnees_crees/tableau_affinites.png"))  # Import de la table d'affinité
        layout.addWidget(affinites)  # Ajout de l'image

        fermer = QtWidgets.QPushButton("Fermer")
        fermer.setStyleSheet("background-color: rgb(110,255,100); color: rgb(0,0,0); font: bold 75 10pt \"Arial\"")
        layout.addWidget(fermer)  # Ajout deu bouton fermer
        self.affinites_fenetre = QtWidgets.QWidget()            # Création de la fenêtre d'affinités avant avant de connecter le bouton (Dans ce ordre pour éviter de créer une fonction supplémntaire)
        self.affinites_fenetre.setFixedSize(960, 630)           # On fixe la taille de la fenetre
        fermer.clicked.connect(self.affinites_fenetre.close)    # Connexion du bouton fermer à la fermeture de l'image

        self.affinites_fenetre.setWindowIcon(QtGui.QIcon("../Images/Pokemon_logo.png"))   # Import du logo pokemon
        self.affinites_fenetre.setLayout(layout)
        self.affinites_fenetre.setWindowTitle("Tableau des Affinités")                    # Titre tableau
        self.affinites_fenetre.setGeometry(100, 100, 600, 400)
        self.affinites_fenetre.show()                                                     # Affichage de la fenêtre


        
        
##############################################################

             ########## Carte ###########     

##############################################################
        

class Window_Carte (Carte):
    def __init__(self, Profil ): 
        super( ).__init__()
        self.joueur = Profil.joueur
        # Les coordonnées sont ajustées avant d'être passées pour positionner le joueur correctement sur la carte
        self.joueur.x, self.joueur.y = self.coord_choice[0] / 2, 2 * self.coord_choice[1]
        self.joueur.sizeJ = 40
        self.pokemons_libres =self.joueur.pokemons_libres
        self.pokemons_sauvages= self.joueur.pokemons_sauvages
        self.pokemons_hors_map=  self.joueur.pokemons_hors_map
        self.pokemon_adversaire= None
        self.create_menu()
        if len(self.joueur) == 151:
            self.fin_de_jeu()
###############################################################################################

###############################  Message de fin de Jeu  ###############################

###############################################################################################
    def fin_de_jeu(self):
        """
        Vérifier si le jeu est fini.

        Returns:
            None
        """
        
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

    def musique_carte(self):
        pygame.mixer.music.load("../Musique/carte.mp3")  # Chargement de la musique de la carte de jeu
        pygame.mixer.music.play(-1)                      # Répétition en boucle infinie
            
    def reinitialisation(self):
        self.relancer=Window_Bienvenue()
        self.relancer.show()
        self.fin.close()
        self.close()

###############################################################################################
    def recherche_pokemon(self):
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
            pokemon = Dresseur.dict_pokemons[pokemon_nom]
            position= pokemon.Coordonnees
            dist = ((2 *self.joueur.x - position[0])**2 + (self.joueur.y/2 - position[1])**2)**0.5
            # Mise à jour du Pokémon le plus proche si la nouvelle distance est plus petite
            if dist < nearest_distance:
                nearest_distance = dist
                nearest_pokemon = pokemon

        if nearest_pokemon != None:
            pygame.mixer.music.pause()                              # Mis en pause de la musique de la carte
            walking = pygame.mixer.Sound("../Musique/danger.mp3")   # Chargement du son de deplacement
            walking.play()                                          # lancement
            walking.set_volume(0.01)                                # Réglage de Volume
            self.pokemon_adversaire = nearest_pokemon
            nearest_pokemon = None
            confirm_box = QMessageBox()
            confirm_box.setIcon(QMessageBox.Icon.Question)
            confirm_box.setWindowTitle("Alerte !")
            confirm_box.setWindowIcon(QtGui.QIcon("../Images/Pokemon_logo.png"))
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
                walking.stop()
                confrontation = pygame.mixer.Sound("../Musique/confrontation.mp3")  # Chargement du son de confrontation
                confrontation.play()
                confrontation.set_volume(0.07)
            else:
                walking.stop()
                pygame.mixer.music.unpause()
                self.pokemon_adversaire=None
                player_position = rd.sample(self.coord_surete, k=1)[0]
                self.joueur.x, self.joueur.y= int(player_position[0] /2), 2* int(player_position[1] )
                self.update()

    def display_developpers(self):
        """
            Afficher un label contenant les développeurs du jeu.

            Returns:
                None
        """
        pygame.mixer.music.pause()
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
        pygame.mixer.music.unpause()

                    
               
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
        x = round(self.joueur.x * (self.width() - 2 * Carte.MARGIN) // Carte.GRID_SIZE + Carte.MARGIN)
        y = round(self.joueur.y * (self.height() - 2 * Carte.MARGIN) // Carte.GRID_SIZE + Carte.MARGIN)
        painter.drawPixmap(x, y, self.joueur.sizeJ, self.joueur.sizeJ, QtGui.QPixmap("../Images/joueur.png"))

        # le facteur d'echelle pour convertir les coordoonnées du fichier en coordonnées pixelisées.
        # Coordonnée maximun dans le fichier : x = 40 et y = 10.
        self.echelleX = (self.width() - 2 * Carte.MARGIN) / 40
        self.echelleY = (self.height() - 2 * Carte.MARGIN) / 10

        # Dessin des pokemons libres
        for pokemon_libre in self.pokemons_libres:
            pokemon = Dresseur.dict_pokemons[pokemon_libre]
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
        voir_profil = QAction("Voir profil", self)
        voir_profil.triggered.connect(self.retour_profil)

        developpers = QAction("Voir les developpeurs", self)
        developpers.triggered.connect(self.display_developpers)

        # Création d'un menu
        menu = self.menuBar()
        menu.setStyleSheet("background-color: transparent;")
        fichier_menu = menu.addMenu(QtGui.QIcon("../Images/menu.png"),"Menu")
        fichier_menu.setStyleSheet("background-color: rgb(255,255,255); color : black;")
        fichier_menu.addAction(voir_profil)
        fichier_menu.addAction(developpers)
        
        
    def keyPressEvent(self, event):
        """
            Gère les événements de pression de touche.

            Args:
                event: L'événement de pression de touche.

            """
        # Déplace le joueur en fonction de la touche pressée

        if event.key() == QtCore.Qt.Key.Key_Up:
            self.marche()
            self.joueur.deplacer("haut")
        elif event.key() == QtCore.Qt.Key.Key_Down:
            self.marche()
            self.joueur.deplacer("bas")
        elif event.key() == QtCore.Qt.Key.Key_Left:
            self.marche()
            self.joueur.deplacer("gauche")
        elif event.key() == QtCore.Qt.Key.Key_Right:
            self.marche()
            self.joueur.deplacer("droite")
        # Affiche le Pokémon le plus proche du joueur
        self.recherche_pokemon()
        # Actualise l'affichage de la carte
        self.repaint()

    def marche(self):
        walking = pygame.mixer.Sound("../Musique/deplacement.mp3")  # Chargement ddu son de deplacement
        walking.play()  # lancement
        walking.set_volume(1)  # Volume

    def change_window(self):
        """
        Fonction qui permet d'ouvrir l'interface de combat

        """
        self.next_window = Window_Lancement_combat (self)      # renvoie les donnees à l'interface suivante
        self.next_window.show()
        self.close()
        
    def retour_profil(self):
        pygame.mixer.music.pause()           # Mis en pause de la musique de carte
        self.back_window = Window_Player_profil(self)
        self.back_window.musique_profil()    # Lancement de la musique du profil
        self.back_window.show()
        
##############################################################

             ########## Lancement ###########     

##############################################################

class Window_Lancement_combat (QMainWindow,Ui_Lancement_combat):
    
    # Constructeur
    def __init__(self,Carte, parent=None): 
        super(Window_Lancement_combat, self).__init__(parent)
        self.setupUi(self)
        
        # Recuperation des donnees sur le joueur
        self.joueur= Carte.joueur
        
        # Recuperation du pokemon rencontre
        self.pokemon_adversaire= Carte.pokemon_adversaire
        
        # Recuperations des combattants du joueur
        self.Combattants=self.joueur.pokemons_combats
        self.pokemons_zone_attente = [Dresseur.dict_pokemons[self.Combattants[0]],
                                      Dresseur.dict_pokemons[self.Combattants[1]],
                                      Dresseur.dict_pokemons[self.Combattants[2]]]
        
        # Affichage des acteurs dans le combat
        self.acteur_combat()
        
        # Bouton de passage à la fenetre suivante
        self.PASS.clicked.connect(self.change_window)
        

    def change_window(self):
        """
        Fonction qui permet de retourner à la carte avec les donnees à jour

        """
        self.next_window = Window_Selection_pokemon (self)      # renvoie les donnees à l'interface suivante
        self.next_window.show()

    def acteur_combat(self):
        """
        Fonction affichant tous les acteurs du combats
        """
        
        # Affichage d joueur
        self.Joueur.setPixmap(QtGui.QPixmap(self.joueur.Image))
        
        # Pokemons du joueur
        pokemons =self.pokemons_zone_attente
        
        # Affichage de leurs noms
        self.Nom_Pokemon_1.setText(pokemons[0].nom)
        self.Nom_Pokemon_2.setText(pokemons[1].nom)
        self.Nom_Pokemon_3.setText(pokemons[2].nom)
        
        # Affichage de leurs images
        self.Pokemon_1.setPixmap(QtGui.QPixmap( pokemons[0].Image))
        self.Pokemon_2.setPixmap(QtGui.QPixmap( pokemons[1].Image))
        self.Pokemon_3.setPixmap(QtGui.QPixmap( pokemons[2].Image))
        
        # Affichage de leurs types
        self.Type_4.setPixmap(QtGui.QPixmap("../Images/Types/"+pokemons[0].type1+".png"))
        self.Type_3.setPixmap(QtGui.QPixmap("../Images/Types/"+pokemons[0].type2+".png"))
        self.Type_5.setPixmap(QtGui.QPixmap("../Images/Types/"+pokemons[1].type1+".png"))
        self.Type_6.setPixmap(QtGui.QPixmap("../Images/Types/"+pokemons[1].type2+".png"))
        self.Type_8.setPixmap(QtGui.QPixmap("../Images/Types/"+pokemons[2].type1+".png"))
        self.Type_7.setPixmap(QtGui.QPixmap("../Images/Types/"+pokemons[2].type2+".png"))
        
        # Info sur le pokemon rencontre
        self.Nom_adversaire.setText(self.pokemon_adversaire.nom)
        self.Adversaire.setPixmap(QtGui.QPixmap(self.pokemon_adversaire.Image))
        self.Type_1.setPixmap(QtGui.QPixmap("../Images/Types/"+self.pokemon_adversaire.type1+".png"))
        self.Type_2.setPixmap(QtGui.QPixmap("../Images/Types/"+self.pokemon_adversaire.type2+".png"))
        
        
        
        
##############################################################

             ########## Selection ###########   

##############################################################

class Window_Selection_pokemon (QMainWindow,Ui_Selection_pokemon):
    # Constructeur
    def __init__(self,lancement, parent=None):
        super(Window_Selection_pokemon, self).__init__(parent)
        self.setupUi(self)
        self.pokemons_zone_attente= lancement.pokemons_zone_attente
        self.affichage()
        self.joueur = lancement.joueur
        self.pokemon_adversaire= lancement.pokemon_adversaire
        
        # Indicateur de pokemon
        self.Pokemon_1_etat= False
        self.Pokemon_2_etat= False
        self.Pokemon_3_etat= False
        
        # Recuperation de donnes de la fenetre de lancement de combat
        self.lancement= lancement
        
        # Connection des boutons aux methodes pour recuperer le pokemon choisi 
        self.Pokemon_1.clicked.connect(self.press_Pokemon_1)
        self.Pokemon_2.clicked.connect(self.press_Pokemon_2)
        self.Pokemon_3.clicked.connect(self.press_Pokemon_3)
        self.Pokemon_1.clicked.connect(self.choix_pokemon_attaquant)
        self.Pokemon_2.clicked.connect(self.choix_pokemon_attaquant)
        self.Pokemon_3.clicked.connect(self.choix_pokemon_attaquant)

    def press_Pokemon_1(self):
        # Indicateur du pokemon choisi
        self.Pokemon_1_etat =True
        
    def press_Pokemon_2(self):
        # Indicateur du pokemon choisi
        self.Pokemon_2_etat =True
        
    def press_Pokemon_3(self):
        # Indicateur du pokemon choisi
        self.Pokemon_3_etat =True
        
    def choix_pokemon_attaquant(self):
        """
        Fonction recuperant le pokemon choisi comme pokemon attaquant
        """
        # Recupere les combattants du joueur
        Combattants = self.pokemons_zone_attente
        
        # Recherche du pokemon choisi
        if self.Pokemon_1_etat ==True:
            self.pokemon_zone_combat= Combattants[0]
        elif self.Pokemon_2_etat ==True:
            self.pokemon_zone_combat= Combattants[1]
        elif self.Pokemon_3_etat ==True:
            self.pokemon_zone_combat= Combattants[2]
            
        # Creation de la fenetre decombat et transfert des donnees
        self.next_window = Window_Zone_de_bataille(self)
        self.next_window.show()
        
        # Fermeture des fenetres selection et lancement
        self.lancement.close()
        self.close()
        
    def affichage(self):
        """
        Fonction d'affichage des pokemons de combats du joueur

        """
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
    
    # Constructeur
    def __init__(self, selection, parent=None):
        super(Window_Zone_de_bataille, self).__init__(parent)
        self.setupUi(self)
        
        # Recuperation des pokemons du joueur et adverse
        self.pokemons_zone_attente= selection.pokemons_zone_attente
        self.pokemon_zone_combat= selection.pokemon_zone_combat
        self.pokemon_zone_adversaire= selection.pokemon_adversaire
        
        # Recuperation des infos du joueur
        self.joueur= selection.joueur
        
        # Creation de la zone de rpos pour les pokemons KO
        self.pokemons_zone_repos=[]
        
        # Creation des bars de vie des pokemon attaquant et adverse
        self.progress_bar_attaquant = QtWidgets.QProgressBar(self)
        self.progress_bar_attaquant.setGeometry(QtCore.QRect(252, 215, 150, 15))
        self.progress_bar_attaquant.setTextVisible(False)
        self.progress_bar_attaquant.setStyleSheet("QProgressBar::chunk { background-color: rgb(255, 46, 46); }")
        
        self.progress_bar_adversaire = QtWidgets.QProgressBar(self)
        self.progress_bar_adversaire.setGeometry(QtCore.QRect(693, 215, 150, 15))
        self.progress_bar_adversaire.setTextVisible(False)
        self.progress_bar_adversaire.setStyleSheet("QProgressBar::chunk { background-color: rgb(255, 46, 46); }")
        
        # Affichage 
        self.acteur_combat()
        self.affichage_HP()
        
        # Creation des indicateurs de boutons et d'etats
        
        self.Pokemon_1_etat= False
        self.Pokemon_2_etat= False
        self.Pokemon_3_etat= False
        self.type_1_etat =False         #  Boutons
        self.type_2_etat=False
        self.Neutre_etat=False
        
        self.Echange_etat=False
        self.fin_combat=False
        self.KO= False                  #  Etats
        self.fuir_etat=False
        
        # Connection des boutons aux methodes de changement d'etat
        self.Pokemon_1.clicked.connect(self.press_Pokemon_1)
        self.Pokemon_2.clicked.connect(self.press_Pokemon_2)
        self.Pokemon_3.clicked.connect(self.press_Pokemon_3)
        self.Neutre.clicked.connect(self.press_neutre)
        self.Type1.clicked.connect( self.press_type_1)
        self.Type2.clicked.connect( self.press_type_2)
        self.Fuir.clicked.connect( self.press_fuir)
        
        # Connection des boutons aux options du joueur
        self.Neutre.clicked.connect(self.attaque_neutre)
        self.Type1.clicked.connect(self.attaque_elementaire)
        self.Type2.clicked.connect(self.attaque_elementaire)
        self.Fuir.clicked.connect(self.fuite)
        
        self.lance_echange_pokemon()
        self.combat()
        

        
    def acteur_combat(self):
        """
        Fonction d'affichage des pokemons et leurs infos sur la zone de combat

        """
        Window_Selection_pokemon.affichage(self) # Affiche les images des pokemons
        
        # Nom et image du pokemon attaquant
        self.Pokemon_attaquant.setPixmap(QtGui.QPixmap(self.pokemon_zone_combat.Image))
        self.Nom_attaquant.setText(self.pokemon_zone_combat.nom)
        
        # Desactive le bouton du pokemon attaquant
        for bouton in [self.Pokemon_1,self.Pokemon_2,self.Pokemon_3]:
            icon = bouton.icon().pixmap(bouton.icon().availableSizes()[0]).cacheKey()
            image =self.Pokemon_attaquant.pixmap().cacheKey()
            if image == icon:
                bouton.setStyleSheet("background-color: rgba(255, 77, 61, 0.3)")
                bouton.setEnabled(False)

        # Affiche les types du pokemons attaqants
        self.Type1.setIcon(QtGui.QIcon("../Images/Types/"+self.pokemon_zone_combat.type1+".png"))
        self.Type2.setIcon(QtGui.QIcon("../Images/Types/"+self.pokemon_zone_combat.type2+".png"))
        if self.pokemon_zone_combat.type2 == "null":
            self.Type2.setStyleSheet("background-color: rgba(255, 77, 61, 0.3)")
            self.Type2.setEnabled(False)
            
        # Affiche les informations du pokemon adverse
        self.Type1_adversaire.setPixmap(QtGui.QPixmap("../Images/Types/"+self.pokemon_zone_adversaire.type1+".png"))
        self.Type2_adversaire.setPixmap(QtGui.QPixmap("../Images/Types/"+self.pokemon_zone_adversaire.type2+".png"))
        self.Adversaire.setPixmap(QtGui.QPixmap(self.pokemon_zone_adversaire.Image))
        self.Nom_adversaire.setText(self.pokemon_zone_adversaire.nom)
        
        # Affiche le joueur
        self.Joueur.setPixmap(QtGui.QPixmap(self.joueur.Image))
        
    def affichage_HP(self):
        """
        Fonction d'affichage des points de vie

        """
        
        # Ecriture numérique de la bar de vie
        self.Nom_attaquant.setText(self.pokemon_zone_combat.nom)
        self.PV_adversaire.setText(str(self.pokemon_zone_adversaire.HP_combat)+" / "+str(self.pokemon_zone_adversaire.HP))
        self.PV_attaquant.setText(str(self.pokemon_zone_combat.HP_combat)+" / "+str(self.pokemon_zone_combat.HP)) 
        
        #  Niveau de vie max et niveau de vie actuelle de l'attaquant
        self.progress_bar_attaquant.setMaximum(self.pokemon_zone_combat.HP)
        self.progress_bar_attaquant.setValue(self.pokemon_zone_combat.HP_combat)
        
        #  Niveau de vie max et niveau de vie actuelle de l'adversaire
        self.progress_bar_adversaire.setMaximum(self.pokemon_zone_adversaire.HP)
        self.progress_bar_adversaire.setValue(self.pokemon_zone_adversaire.HP_combat)
        
    def press_Pokemon_1(self):
        """
        Fonction pour gerer un echange de pokemon ou un
        remplacement de pokemon avec le pokemon 1

        """
        # Indicateur du pokemon choisi
        self.Pokemon_1_etat =True
        # Verification pour un pokemon hors de combat
        if self.KO:
            # Remplacement du pokemon KO
            self.remplacement()
            
            self.Pokemon_1_etat =False # Desactivation de l'indicateur
        self.lance_echange_pokemon()   # Appel de fonction
        

    def press_Pokemon_2(self):
        """
        Fonction pour gerer un echange de pokemon ou un
        remplacement de pokemon avec le pokemon 2

        """
        # Indicateur du pokemon choisi
        self.Pokemon_2_etat =True
        # Verification pour un pokemon hors de combat
        if self.KO:
            self.remplacement()
            self.Pokemon_2_etat =False  # Desactivation de l'indicateur
        self.lance_echange_pokemon()    # Appel de fonction
        
    def press_Pokemon_3(self):
        """
        Fonction pour gerer un echange de pokemon ou un
        remplacement de pokemon avec le pokemon 3

        """
        # Indicateur du pokemon choisi
        self.Pokemon_3_etat =True
        # Verification pour un pokemon hors de combat
        if self.KO:
            self.remplacement()
            self.Pokemon_3_etat =False  # Desactivation de l'indicateur
        self.lance_echange_pokemon()    # Appel de fonction
    
    def press_neutre(self):
        # Indicateur de l'attaque neutre
        self.Neutre_etat =True
        
    def press_type_1(self):
        # Indicateur de l'attaque elementaire 1
        self.type_1_etat = "actif"
        
    def press_type_2(self):
        # Indicateur de l'attaque elementaire 
        self.type_2_etat = "actif"
        
    def press_fuir (self):
        # Indicateur de la fuite du joueur
        self.fuir_etat=True
        
    def lance_echange_pokemon(self):
        """
        Fonction de gestion du bouton echange

        """
        # Detection du pokemon choisi pour l'echange
        if self.Pokemon_1_etat or self.Pokemon_2_etat or self.Pokemon_3_etat:
            self.Echange_etat= True            # Indicateur d'un echange
            self.Echange.setEnabled(True)      # Activation du bouton echange
        else:
            self.Echange.setEnabled(False)     # Desactivation du bouton echange
   
    def echange_pokemon(self):
        """
        Fonction permettant d'echanger les pokemons

        """
        if self.Echange_etat: # Active la fonction lorsque le bouton Echange est active
            # Recherche du pokemon et active son bouton 
            for bouton in [self.Pokemon_1,self.Pokemon_2,self.Pokemon_3]:
                icon = bouton.icon().pixmap(bouton.icon().availableSizes()[0]).cacheKey()
                image =self.Pokemon_attaquant.pixmap().cacheKey()
                if icon == image:
                    bouton.setStyleSheet("background-color: transparent")
                    bouton.setEnabled(True)
                    
            # Verification chaque indicateur pour trouver le pokemon à remplacer 
            if self.Pokemon_1_etat :
                self.pokemon_zone_combat= self.pokemons_zone_attente[0]
                self.Pokemon_1_etat =False
                
            elif self.Pokemon_2_etat :
                self.pokemon_zone_combat= self.pokemons_zone_attente[1]
                self.Pokemon_2_etat =False
                
            elif self.Pokemon_3_etat :
                self.pokemon_zone_combat= self.pokemons_zone_attente[2]
                self.Pokemon_3_etat =False
            
            # Mise à jour de la zone de combat, booleen à false et desactivation du bouton echange
            self.acteur_combat()
            self.affichage_HP()
            self.Echange.setEnabled(False)
            self.Echange_etat=False
                    
    def fuite(self):
        """
        Fonction qui provoque une defaite immediate
        """
        if self.fuir_etat :
            self.Defaite()
            
    def restaure_HP(self):
        """
        Fonction restaurant les HP detous les pokemons
        """
        for pokemon in self.pokemons_zone_attente:
            pokemon.HP_combat =pokemon.HP
        self.pokemon_zone_adversaire.HP_combat=self.pokemon_zone_adversaire.HP
        
    def Victoire(self):   
        """
        Fonction qui renvoie la fenetre victoire

        """
        # Verifie l'etat des points de vie de l'adversaire
        if self.pokemon_zone_adversaire.HP_combat==0:
            # Restauration des HP de tous les pokemons
            self.restaure_HP()
            # Indique que le combat est fini et affiche la fenetre victoire
            self.next_window=Window_Victoire_combat(self)
            self.fin_combat=True
            self.next_window.show()
            victoire = pygame.mixer.Sound("../Musique/victoire.mp3") # Mise en pause de la musique de combat
            victoire.play()                                         # Son de la victoire
            victoire.set_volume(0.3)                                # Réglage du volume

            

    def Defaite(self): 
        """
        Fonction qui affiche la fenêtre de defaite

        """
        # Verifie si tous les pokemons du joueur son KO
        if len(self.pokemons_zone_repos) ==3 or self.fuir_etat:
            self.restaure_HP()
            self.next_window=Window_Combat_perdu(self)
            self.next_window.show()
            defaite = pygame.mixer.Sound("../Musique/defaite.mp3")  # Mise en pause de la musique de combat
            defaite.play()
            defaite.set_volume(0.3)
            self.fin_combat=True
            
    def attaque_neutre(self):
        """
        Fonction qui lance une attaque sans type

        """
        if self.Neutre_etat:
           Dommage = self.pokemon_zone_combat.attaque_neutre(self.pokemon_zone_adversaire)
           self.Degats.setText(Dommage)
           self.Degats_attaquant.setPixmap(QtGui.QPixmap("../Images/Explosion.png"))
           self.Neutre_etat=False 
        
        
    def attaque_elementaire(self):
        """
        Fonction qui lance une attaque elementaire

        """
        if self.type_1_etat =="actif":
            Dommage =self.pokemon_zone_combat.attaque_elementaire(self.pokemon_zone_adversaire, False)
            self.Degats.setText(Dommage)
            self.Degats_attaquant.setPixmap(QtGui.QPixmap("../Images/Attaques/"+str(self.pokemon_zone_combat.type1)+".png"))
            self.type_1_etat =False
        if self.type_2_etat =="actif":
            Dommage = self.pokemon_zone_combat.attaque_elementaire(self.pokemon_zone_adversaire, True)
            self.Degats.setText(Dommage)
            self.Degats_attaquant.setPixmap(QtGui.QPixmap("../Images/Attaques/"+str(self.pokemon_zone_combat.type2)+".png"))
            self.type_2_etat=False

    def info_combat(self):
        """
        Fonction appel la fonction de nettoyage 2 secondes plus tard

        """
        self.timer_nettoyage = QtCore.QTimer(self)
        self.timer_nettoyage.timeout.connect(self.nettoyage)
        self.timer_nettoyage.start(2000)
        
    def nettoyage(self):
        """
        Fonction qui supprime les information des attaques lancees et arrete le chrono
        """
        self.Degats_attaquant.clear()
        self.Degats.clear()
        self.Degats_adversaire.clear()
        self.timer_nettoyage.stop()   

        
    def pokemon_KO(self):
        """
        Fonction verifiant l'etat du pokemon attaquant et
        le met en zone de repos s'il est KO

        """
        # Verifie la quantite de points de vie du pokemon attaquant
        if self.pokemon_zone_combat.HP_combat == 0:
            
            # Liste des boutons et labels en ordre
            liste_boutons = [self.Pokemon_1,self.Pokemon_2,self.Pokemon_3]
            liste_labels = [self.Pokemon_KO_1, self.Pokemon_KO_2, self.Pokemon_KO_3]
            
            # Recherche du pokemon
            for numero in range(len(liste_boutons)):
                bouton = liste_boutons[numero]
                icon = bouton.icon().pixmap(bouton.icon().availableSizes()[0]).cacheKey()
                image =self.Pokemon_attaquant.pixmap().cacheKey()
                if icon == image:
                    
                    # Recupere l'image du pokemon, la convertie en noir et blanc et l'associe au label correspondant
                    pokemon = self.pokemons_zone_attente[numero]
                    label = liste_labels[numero]
                    image =QtGui.QImage(pokemon.Image).convertToFormat(QtGui.QImage.Format_Grayscale8)
                    pixmap = QtGui.QPixmap.fromImage(image)
                    label.setPixmap(pixmap)
                    self.pokemons_zone_repos.append(pokemon)
            self.KO= True
            if self.KO==True:
                self.desactivation_boutons()
                
    def remplacement(self):
        """
        Fonction qui remplace le pokemon KO par le pokemon choisi

        """
        if self.KO==True:  # Verifie si un pokemon est KO
            #Recherche du pokemon choisi, desactive le bouton et renvoie le signal à false
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
        # Mise à jour de la zone de combat
        self.acteur_combat()
        self.affichage_HP()
        self.KO= False
        self.activation_boutons()
        
    def tour_joueur(self):
        """
        Fonction qui regroupe les differentes actions possibles du joueur

        """
        if self.Neutre_etat:
            self.attaque_neutre()
                 
        elif self.fuir_etat:
            self.fuite()
               
        elif self.Echange_etat :
            self.echange_pokemon()
               
        elif self.type_1_etat == "actif":
            self.attaque_elementaire()
            
        elif self.type_2_etat == "actif":
            self.attaque_elementaire()
        self.info_combat()
        self.affichage_HP()
        self.Victoire()
        
        
    def Action_utilisateur(self):
        """
        Fonction qui met l'interface en attente pour que le joueur face son choix

        Returns
        -------
        Action : Booleen
            Renvoie un True lorsque le joueur fait son choix.

        """
        loop = QtCore.QEventLoop()  # Crée une boucle d'événements
        Action = False
        
        # Fonction pour gérer les options du joueur
        def Action_joueur():
            nonlocal Action
            Action = True
            loop.quit()  
        
        # Connection des options du joueur pour recuperer le choix du joueur
        self.Neutre.clicked.connect(Action_joueur)
        self.Type1.clicked.connect(Action_joueur)
        self.Type2.clicked.connect(Action_joueur)
        self.Fuir.clicked.connect(Action_joueur)
        self.Echange.clicked.connect(Action_joueur)
        
        self.show() # Activation del'interface de combat
        loop.exec_()
        return Action # Renvoie le signal lorsque le joueur fait son choix
    
    def degats_elementaires(self,Dommage,booleen):
        """
        

        Parameters
        ----------
        Dommage : string
            Information du pokemon et l'attaque.
        booleen : Booleen
            Permet de determiner le type de l'attaque elementaire.

        """
        if booleen:
            self.Degats.setText(Dommage) # Information sur l'attaque
            # Ajout de l'image correspondant
            self.Degats_adversaire.setPixmap(QtGui.QPixmap("../Images/Attaques/"+str(self.pokemon_zone_adversaire.type2)+".png"))
            # Suppression de l'image et des informations
            self.info_combat()
        else:
            
           self.Degats.setText(Dommage) # Information sur l'attaque
           # Ajout de l'image correspondant
           self.Degats_adversaire.setPixmap(QtGui.QPixmap("../Images/Attaques/"+str(self.pokemon_zone_adversaire.type1)+".png"))
           # Suppression de l'image et des informations
           self.info_combat()
    
    def attaque_adversaire(self):
        """
        Fonction generant les attaques du pokemons adverse

        """
        
        choix= [True, False]
        # Fait un premier choix aleatoire si true attaque neutre
        if rd.choice(choix):
            Dommage = self.pokemon_zone_adversaire.attaque_neutre(self.pokemon_zone_combat)
            # Afichage des infos des attaques et suppression
            self.Degats.setText(Dommage)
            self.Degats_adversaire.setPixmap(QtGui.QPixmap("../Images/Explosion.png"))
            self.info_combat()
            
        else: # Sinon attaque elementaire
            if self.pokemon_zone_adversaire.type2 == 'null': # attaque de type 1 si le pokemon est d'un seul type 
                Dommage = self.pokemon_zone_adversaire.attaque_elementaire(self.pokemon_zone_combat, False)
                # Afichage des infos des attaques et suppression
                self.degats_elementaires(Dommage, False)
                
            else:# Sinon attaque elementaire aleatoire
                elementaire =rd.choice(choix)
                Dommage = self.pokemon_zone_adversaire.attaque_elementaire(self.pokemon_zone_combat,elementaire )
                # Afichage des infos des attaques et suppression
                self.degats_elementaires(Dommage, elementaire)
        self.info_combat()
        
        # Activation des boutons d'options du joueur, actualisation des 
        self.activation_boutons()
        
        # Actualisation des HP et verifications des etats du combat
        self.affichage_HP()
        self.pokemon_KO()
        self.Defaite()
        
        # Arret du chrono
        self.timer_adversaire.stop()
      
    def tour_adversaire(self):
        """
        Fontion de retardement de l'action de l'adversaire 

        """
        self.desactivation_boutons()
        # Chrono pour que l'action de l'adversaire se passe après 2 secondes
        self.timer_adversaire = QtCore.QTimer(self)
        self.timer_adversaire.timeout.connect(self.attaque_adversaire)
        self.timer_adversaire.start(2000)
        
        
    def desactivation_boutons(self):
        """
        Fonction de desactivation des boutons du joueur lors du tour de l'adversaire

        """
        self.Neutre.setEnabled(False)
        self.Type1.setEnabled(False)
        self.Type2.setEnabled(False)
        
        
    def activation_boutons (self):
        """
        Fonction d'activation des boutons du joueur lors du tour de l'adversaire

        """
        self.Neutre.setEnabled(True)
        self.Type1.setEnabled(True)
        self.Type2.setEnabled(True)
        if self.pokemon_zone_combat.type2 == "null":
            self.Type2.setStyleSheet("background-color: rgba(255, 77, 61, 0.3)")
            self.Type2.setEnabled(False)
                        
    
    # Optimisation
    def combat(self):
        """
        Fonction de gestion de combat

        """
        # Comparaison des vitesses pour determiner le 1er joueur
        if self.pokemon_zone_combat.Speed >= self.pokemon_zone_adversaire.Speed:
            
            # Message  pour le joueur 
            QMessageBox.information(self,"   POKEMON", "Vous jouer en première position \nBonne chance  !")
            
            # Boucle jusqu'à la victoire ou la defaite du joueur
            while  self.fin_combat == False: 
                Action =self.Action_utilisateur() #Attente de la reponse de l'utilisateur
                if Action:
                    self.tour_joueur() # Tour du joueur
                    self.musique_coup()
                self.tour_adversaire() # Tour de l'adversaire
        else:
            # Message  pour le joueur
            QMessageBox.information(self,"   POKEMON", "Votre adversaire joue en première position\nBonne chance  !")
            # Boucle jusqu'à la victoire ou la defaite du joueur
            while  self.fin_combat == False:
                self.tour_adversaire()  # Tour de l'adversaire
                Action =self.Action_utilisateur() #Attente de la reponse de l'utilisateur
                if Action:
                    self.tour_joueur() # Tour du joueur
                    self.musique_coup()

    def musique_coup(self):
        coups = pygame.mixer.Sound("../Musique/coups.mp3")  # Chargement du son des coups
        coups.play()
        coups.set_volume(0.5)

                 
                    


##############################################################

             ########## Resultat ###########

##############################################################

class Window_Combat_perdu (QMainWindow,Ui_Combat_perdu):  
    # Constructeur
    def __init__(self, Zone_de_bataille, parent=None):
        super(Window_Combat_perdu, self).__init__(parent)
        self.setupUi(self)
        self.Bataille= Zone_de_bataille
        self.PASS.clicked.connect(self.change_window)

        
    def change_window(self):
        """
        Fonction qui permet de retourner à la carte avec les donnees à jour

        """
        self.next_window = Window_Carte (self.Bataille)      # renvoie les donnees à l'interface suivante
        self.next_window.show()
        self.next_window.musique_carte()
        self.Bataille.close()
        self.close()
        
        
class Window_Victoire_combat (QMainWindow,Ui_Victoire_combat ):  
    
    # Constructeur
    def __init__(self, Zone_de_bataille, parent=None):
        super(Window_Victoire_combat, self).__init__(parent)
        self.setupUi(self)
        self.Bataille= Zone_de_bataille
        self.PASS.clicked.connect(self.change_window)
        
    def change_window(self):
        """
        Fonction qui permet de retourner à la carte avec les donnees à jour

        """
        self.next_window = Window_Capture_pokemon (self.Bataille)      # renvoie les donnees à l'interface suivante
        self.next_window.show()
        sound = pygame.mixer.Sound("../Musique/capture.mp3")   # Chargement du son de capture
        sound.play()
        sound.set_volume(0.5)
        self.Bataille.close()
        self.close()
        
        
#############################################################

             ######### Capture ###########  

#############################################################


class Window_Capture_pokemon(QMainWindow,Ui_Capture_pokemon):
    
    # constructeur
    def __init__(self, Bataille, parent=None):
        super(Window_Capture_pokemon, self).__init__(parent)
        self.setupUi(self)
        self.joueur= Bataille.joueur                                 #  Recuperation de la classe dresseur 
        self.pokemon_adversaire =  Bataille.pokemon_zone_adversaire  #  Recuperation 
        self.Capture()                                               #  Appel de la foncton capture
        self.PASS.clicked.connect(self.change_window)                #  Bouton permettant de retourner à la carte
        
    def change_window(self):
        """
        Fonction qui permet de retourner à la carte avec les donnees à jour

        """
        self.next_window = Window_Carte (self)      # renvoie les donnees à l'interface suivante
        self.next_window.show()
        self.next_window.musique_carte()
        self.close()
        
    def Capture(self):
        """
        Fonction permettant de recuperer le pokemon battu

        """
        self.joueur.attrape_pokemon(self.pokemon_adversaire)        # le joueur capture le pokemon battu
        self.joueur.ajout_pokemon_sauvages()                        # Remplacement du pokemon sauvage battu
        self.Nom_pokemon.setText(self.pokemon_adversaire.nom)
        
        # Recupration de l'image du pokemon battu
        self.Pokemon_Attrape.setPixmap(QtGui.QPixmap(self.pokemon_adversaire.Image))
        
