# -*- coding: utf-8 -*-
"""
Created on Fri May 10 20:10:24 2024

@author: Hp Probook i7
"""

import sys
import random as rd
sys.path.append('../../Gestion_pokemon/')

from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout

from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets

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


class HealthBar(QWidget):
    def _init_(self):
        super()._init_()
        self.health = 100

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Fond de la barre de vie
        painter.setBrush(Qt.gray)
        painter.drawRect(10, 10, 200, 20)

        # Barre de vie remplie
        painter.setBrush(Qt.green)
        health_width = 2 * self.health
        painter.drawRect(10, 10, health_width, 20)

        # Texte affichant le pourcentage de vie
        painter.setPen(Qt.white)
        font = QFont('Arial', 10)
        painter.setFont(font)
        text = f"{self.health}%"
        painter.drawText(10, 40, text)

    def setHealth(self, value):
        self.health = value
        self.update()
class Window_Lancement_combat (QMainWindow,Ui_Lancement_combat):
    def __init__(self,Joueur= Dresseur("Sacha",'Masculin'),pokemon_adversaire =Krabby(),liste_pokemons_combattants=["Nidoking", "Graveler", "Mew"] , parent=None): #Joueur, pokemon_adversaire, liste_pokemons_combattants
        super(Window_Lancement_combat, self).__init__(parent)
        self.setupUi(self)
        self.joueur= Joueur
        self.joueur.choix_pokemons_combattants()
        self.joueur.pokemons_on_map()
        
        self.pokemon_adversaire=pokemon_adversaire
        self.Combattants=liste_pokemons_combattants
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
        
        
class Window_Zone_de_bataille (QMainWindow,Ui_Zone_de_bataille):
    def __init__(self, selection, parent=None):
        
        super(Window_Zone_de_bataille, self).__init__(parent)
        self.setupUi(self)
        self.pokemons_zone_attente= selection.pokemons_zone_attente
        self.pokemon_zone_combat= selection.pokemon_zone_combat
        self.pokemon_zone_adversaire= selection.pokemon_adversaire
        self.joueur= selection.joueur
        self.pokemons_zone_repos=[]
        
        self.acteur_combat()
        self.affichage_HP()
        self.Attaquer = True
        self.fuir_etat=False
        self.Pokemon_1_etat= False
        self.Pokemon_2_etat= False
        self.Pokemon_3_etat= False
        self.type_1_etat =False
        self.type_2_etat=False
        self.Neutre_etat=False
        self.Echange_etat=False
        
        
        self.Pokemon_1.clicked.connect(self.press_Pokemon_1)
        self.Pokemon_2.clicked.connect(self.press_Pokemon_2)
        self.Pokemon_3.clicked.connect(self.press_Pokemon_3)
        self.Type1.clicked.connect(self.press_type_1)
        self.Type2.clicked.connect(self.press_type_2)
        self.Neutre.clicked.connect(self.press_neutre)
        self.Type1.clicked.connect( self.press_type_1)
        self.Type2.clicked.connect( self.press_type_2)
        self.Fuir.clicked.connect( self.press_fuir)
        self.Echange.clicked.connect(self.press_echange_pokemon)
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
        for bouton in [self.Pokemon_1,self.Pokemon_2,self.Pokemon_3]:
            icon = bouton.icon().pixmap(bouton.icon().availableSizes()[0]).cacheKey()
            image =self.Pokemon_attaquant.pixmap().cacheKey()
            if icon == image:
                bouton.setStyleSheet("background-color: rgba(255, 77, 61, 0.3)")
                bouton.setEnabled(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../Images/Types/"+self.pokemon_zone_combat.type1+".png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Type1.setIcon(icon4)
        self.Type1.setToolTip(self.pokemon_zone_combat.type1)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../Images/Types/"+self.pokemon_zone_combat.type2+".png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Type2.setIcon(icon5)
        self.Type2.setToolTip(self.pokemon_zone_combat.type2)
        if self.pokemon_zone_combat.type2 == "null":
            self.Type2.setStyleSheet("background-color: rgba(255, 77, 61, 0.3)")
            self.Type2.setEnabled(False)
        self.Adversaire.setPixmap(QtGui.QPixmap(self.pokemon_zone_adversaire.Image))
        self.Joueur.setPixmap(QtGui.QPixmap(self.joueur.Image))
        
    def affichage_HP(self):
        self.pv_adversaire = HealthBar(self)
        self.pv_adversaire.setHealth(self.pokemon_zone_adversaire.HP_combat / self.pokemon_zone_adversaire.HP * 100)
        self.gridLayout.addWidget(self.pv_adversaire, 0, 0)

        self.pv_attaquant = HealthBar(self)
        self.pv_attaquant.setHealth(self.pokemon_zone_combat.HP_combat / self.pokemon_zone_combat.HP * 100)
        self.gridLayout.addWidget(self.pv_attaquant, 0, 1)

    def press_Pokemon_1(self):
        self.Pokemon_1_etat =True
        
    def press_Pokemon_2(self):
        self.Pokemon_2_etat =True
        
    def press_Pokemon_3(self):
        self.Pokemon_3_etat =True
    
    def press_neutre(self):
        self.Neutre_etat =True
        
    def press_echange_pokemon(self):
        self.Echange_etat= True
        
    def press_fuir (self):
        self.fuir_etat=True
        
    def echange_pokemon(self):  
        
        for bouton in [self.Pokemon_1,self.Pokemon_2,self.Pokemon_3]:
            icon = bouton.icon().pixmap(bouton.icon().availableSizes()[0]).cacheKey()
            image =self.Pokemon_attaquant.pixmap().cacheKey()
            if icon == image:
                bouton.setStyleSheet("background-color: transparent")
                bouton.setEnabled(True)
                
        print(self.Pokemon_1_etat)
        print(self.Pokemon_2_etat)
        print(self.Pokemon_3_etat)
        print(self.pokemon_zone_combat.Sp_Atk)
        print(self.pokemon_zone_adversaire.Sp_Def)       
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
            
            
        print(self.pokemon_zone_combat.nom)
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

    def fuite(self):
       if self.fuir_etat== True :
            self.next_window=Window_Combat_perdu(self)
            self.next_window.show()
        
    def Victoire(self):   #   
        if self.pokemon_zone_adversaire.HP_combat==0:
            self.next_window=Window_Victoire_combat(self)
            self.next_window.show()

    def defaite(self): 
        if len(self.pokemons_zone_repos)==3:
            self.next_window=Window_Combat_perdu(self)
            self.next_window.show()
            self.hide()
            
    def attaque_neutre(self):
        if self.Neutre_etat:
            self.pokemon_zone_combat.attaque_neutre(self.pokemon_zone_adversaire)
        self.Neutre_etat=False
        self.affichage_HP()
        self.Victoire()
        
             
    def press_type_1(self):
        self.type_1_etat = "actif"
        
    def press_type_2(self):
        self.type_2_etat = "actif"
        
    def attaque_elementaire(self):
        if self.type_1_etat =="actif":
            self.pokemon_zone_combat.attaque_elementaire(self.pokemon_zone_adversaire, False)
            self.type_1_etat =False
        if self.type_2_etat =="actif":
            self.pokemon_zone_combat.attaque_elementaire(self.pokemon_zone_adversaire, True)
            self.type_2_etat=False
        self.affichage_HP()
        self.Victoire()    

        
    def attaque_adversaire(self):
        choix= [True, False]
        if rd.choice(choix):
            self.pokemon_zone_adversaire.attaque_neutre(self.pokemon_zone_combat)
            
        else:
            if self.pokemon_zone_adversaire.type2 == 'null':
                self.pokemon_zone_adversaire.attaque_elementaire(self.pokemon_zone_combat, False)
            else:
                self.pokemon_zone_adversaire.attaque_elementaire(self.pokemon_zone_combat, rd.choice(choix))
        self.affichage_HP()
        self.pokemon_KO()
        # self.remplacement()
        self.defaite()
    
        
    def pokemon_KO(self):
        liste_boutons = [self.Pokemon_1,self.Pokemon_2,self.Pokemon_3]
        liste_labels = [self.Pokemon_KO_1, self.Pokemon_KO_2, self.Pokemon_KO_3]
        if self.pokemon_zone_combat.HP_combat == 0:
            # image = self.pokemon_zone_combat.Image
            for numero in range(len(liste_boutons)):
                bouton = liste_boutons[numero]
                icon = bouton.icon().pixmap(bouton.icon().availableSizes()[0]).cacheKey()
                image =self.Pokemon_attaquant.pixmap().cacheKey()
                if icon == image:
                    bouton.setStyleSheet("background-color: rgba(255, 77, 61, 0.3)")
                    bouton.setEnabled(False)
                    pokemon = self.pokemons_zone_attente[numero]
                    label = liste_labels[numero]
                    
                    image =QtGui.QImage(pokemon.Image).convertToFormat(QtGui.QImage.Format_Grayscale8)
                    pixmap = QtGui.QPixmap.fromImage(image)
                    label.setPixmap(pixmap)
                    self.pokemons_zone_repos.append(pokemon)
    #     
                    
    d
            
            
                    
    def vitesse(self):
      
        if self.pokemon_zone_combat.Speed >= self.pokemon_zone_adversaire.Speed:
            return True
        else:
            return False
        
    def close_window(self):
        self.close()
        
    def combat(self):
        if self.Attaquer:
            if self.vitesse():  # Vérifie la vitesse pour déterminer qui attaque en premier
                print("1")
                self.Pokemon_1.clicked.connect(self.press_Pokemon_1)
                self.Pokemon_2.clicked.connect(self.press_Pokemon_2)
                self.Pokemon_3.clicked.connect(self.press_Pokemon_3)
                self.Type1.clicked.connect(self.press_type_1)
                self.Type2.clicked.connect(self.press_type_2)
                self.Neutre.clicked.connect(self.press_neutre)
                self.Type1.clicked.connect( self.press_type_1)
                self.Type2.clicked.connect( self.press_type_2)
                self.Fuir.clicked.connect( self.press_fuir)
                self.Echange.clicked.connect(self.press_echange_pokemon)
                self.action_joueur()
                print("1")
                self.attaque_adversaire()
                print("1")
            else:
                print("2")
                self.Pokemon_1.clicked.connect(self.press_Pokemon_1)
                self.Pokemon_2.clicked.connect(self.press_Pokemon_2)
                self.Pokemon_3.clicked.connect(self.press_Pokemon_3)
                self.Type1.clicked.connect(self.press_type_1)
                self.Type2.clicked.connect(self.press_type_2)
                self.Neutre.clicked.connect(self.press_neutre)
                self.Type1.clicked.connect( self.press_type_1)
                self.Type2.clicked.connect( self.press_type_2)
                self.Fuir.clicked.connect( self.press_fuir)
                self.Echange.clicked.connect(self.press_echange_pokemon)
                self.attaque_adversaire()
                print("2")
                self.action_joueur()
                print("2")
        
    
    def action_joueur(self):
        if self.Echange_etat:
            self.echange_pokemon()
            self.Echange_etat = False
        elif self.Neutre_etat:
            self.attaque_neutre()
            self.Neutre_etat = False
        elif self.type_1_etat or self.type_2_etat:
            self.attaque_elementaire()
            self.type_1_etat = False
            self.type_2_etat = False
                        
if __name__ == "__main__":
##############################################################

             ########## Jeu ###########

##############################################################

    def run_app():
        app = QApplication(sys.argv)
        # mainWin = Window_Zone_de_bataille(pokemon_attaquant =Seadra(),joueur= Dresseur("Sacha",'Masculin'),pokemons_zone_attente=[Nidoking(), Graveler(), Seadra()],adversaire =Pikachu())
        mainWin = Window_Lancement_combat()
        mainWin.show()
        app.exec_()
    fenetre=run_app()                        