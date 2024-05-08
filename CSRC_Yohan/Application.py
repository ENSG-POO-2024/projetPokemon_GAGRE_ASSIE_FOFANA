# -*- coding: utf-8 -*-
"""
Created on Tue May  7 20:13:38 2024

@author: Hp Probook i7
"""



import sys
import Classes_Pokemons
from PyQt5.QtWidgets import QMainWindow, QApplication

sys.path.append('../data/interface_combat')
from Capture_pokemon import Ui_Capture_pokemon
from Combat_perdu import Ui_Combat_perdu
from Lancement_combat import Ui_Lancement_combat
from Zone_de_bataille import Ui_Zone_de_bataille





class Window_Lancement_combat (QMainWindow,Ui_Lancement_combat):
    def __init__(self, parent=None):
        super(Window_Lancement_combat, self).__init__(parent)
        self.setupUi(self)
        self.PASS.clicked.connect(self.change_window)
        
    def change_window(self):
        self.second_window = Window_Zone_de_bataille ()
        self.second_window.show()
        self.hide()
        
    # def acteur_combat(self):
    #     Joueur= Dresseur("Sacha",'Masculin')                                  #Univers_pokemon.Joueur
    #     self.Nom_Pokemon_1=Joueur.noms_pokemons_combats[0]
    #     self.Nom_Pokemon_2=Joueur.noms_pokemons_combats[1]
    #     self.Nom_Pokemon_3=Joueur.noms_pokemons_combats[2]
    #     self.Pokemon1
    #     self.Pokemon_2
    #     self.Pokemon_3
    #     self.Adversaire
    #     self.Nom_adversaire
    #     self.Joueur
        
        
class Window_Zone_de_bataille (QMainWindow,Ui_Zone_de_bataille):
    def __init__(self, parent=None):
        super(Window_Zone_de_bataille, self).__init__(parent)
        self.setupUi(self)
        self.Fuir.clicked.connect(self.fuir)        
        
class Window_Capture_pokemon(QMainWindow,Ui_Capture_pokemon):
    def __init__(self, parent=None):
        super(Window_Capture_pokemon, self).__init__(parent)
        self.setupUi(self)
        
    def change_window(self):
        self.second_window = Window_Zone_de_bataille ()
        self.second_window.show()
        self.hide()
        

        
    def fuir(self):
        self.second_window = Window_Combat_perdu ()
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
        mainWin = Window_Combat_perdu()
        mainWin.show()
        app.exec_()
    fenetre=run_app()