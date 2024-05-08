# -*- coding: utf-8 -*-
"""
Created on Tue May  7 20:13:38 2024

@author: Hp Probook i7
"""



import sys
sys.path.append('../../CSRC_Yohan/')
from Classes_Pokemons import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout

from PyQt5 import QtCore, QtGui, QtWidgets

from Capture_pokemon import Ui_Capture_pokemon
from Combat_perdu import Ui_Combat_perdu
from Lancement_combat import Ui_Lancement_combat
from Zone_de_bataille import Ui_Zone_de_bataille





class Window_Lancement_combat (QMainWindow,Ui_Lancement_combat):
    def __init__(self, parent=None):
        super(Window_Lancement_combat, self).__init__(parent)
        layout = QVBoxLayout()
        self.setupUi(self)
        self.PASS.clicked.connect(self.change_window)
        self.setLayout(layout)
        self.acteur_combat()
        
    def change_window(self):
        self.second_window = Window_Zone_de_bataille ()
        self.second_window.show()
        self.hide()
        
    def acteur_combat(self):
        Joueur= Dresseur("Sacha",'Masculin')                                  #Univers_pokemon.Joueur
        pokemon_adversaire=Pikachu()
        Joueur.choix_pokemons_combattants()
        Liste_choix,noms,IDs=Dresseur.info_pokemon(Joueur.pokemons_combattants)
        self.Nom_Pokemon_1.setText(noms[0])
        self.Nom_Pokemon_2.setText(noms[1])
        self.Nom_Pokemon_3.setText(noms[2])
        
        self.Pokemon1.setPixmap(QtGui.QPixmap( Joueur.pokemons_zone_attente[noms[0]].Image))
        self.Pokemon_2.setPixmap(QtGui.QPixmap(Joueur.pokemons_zone_attente[noms[1]].Image))
        self.Pokemon_3.setPixmap(QtGui.QPixmap(Joueur.pokemons_zone_attente[noms[2]].Image))
        
        
        self.Adversaire.setPixmap(QtGui.QPixmap(pokemon_adversaire.Image))            #A modifier
        self.Nom_adversaire.setText(pokemon_adversaire.nom)
        
        
        self.Joueur.setPixmap(QtGui.QPixmap(Joueur.Image))
        
        
class Window_Zone_de_bataille (QMainWindow,Ui_Zone_de_bataille):
    def __init__(self, parent=None):
        super(Window_Zone_de_bataille, self).__init__(parent)
        self.setupUi(self)
        self.Fuir.clicked.connect(self.fuite) 
        
    def fuite(self):
        self.second_window = Window_Combat_perdu ()
        self.second_window.show()
        self.hide()
        
    def Victoire(self):
        pokemon_adversaire
        
class Window_Capture_pokemon(QMainWindow,Ui_Capture_pokemon):
    def __init__(self, parent=None):
        super(Window_Capture_pokemon, self).__init__(parent)
        self.setupUi(self)
        
    def change_window(self):
        self.second_window = Window_Zone_de_bataille ()
        self.second_window.show()
        self.hide()
        

        
    
        
    # def pokemon
        
        
class Window_Combat_perdu (QMainWindow,Ui_Combat_perdu):
    def __init__(self, parent=None):
        super(Window_Combat_perdu, self).__init__(parent)
        self.setupUi(self)
        self.PASS.clicked.connect(self.change_window)
        
    def change_window(self):
        self.second_window = Window_Zone_de_bataille ()
        self.second_window.show()
        self.hide()
        
        
if __name__ == "__main__":
    def run_app():
        app = QApplication(sys.argv)
        mainWin = Window_Lancement_combat ()
        mainWin.show()
        app.exec_()
    fenetre=run_app()