# -*- coding: utf-8 -*-
"""
Created on Tue May  7 20:13:38 2024

@author: Hp Probook i7
"""



import sys
sys.path.append('../../Gestion_pokemon/')

from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout

from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

from PyQt5 import QtCore, QtGui, QtWidgets

from Capture_pokemon import Ui_Capture_pokemon
from Combat_perdu import Ui_Combat_perdu
from Lancement_combat import Ui_Lancement_combat
from Zone_de_bataille import Ui_Zone_de_bataille
from Victoire_combat import Ui_Victoire_combat
from Selection_pokemon import Ui_Selection_pokemon
# from Player_profil import Ui_Player_profil
# from Bienvenue import Ui_Bienvenue
# from Inventaire_Pokemon import Ui_Inventaire_Pokemon
from Classes_Pokemons import *

Joueur= Dresseur("Sacha",'Masculin') #Univers_pokemon.Joueur
pokemon_adversaire =[Pikachu()]
Joueur.choix_pokemons_combattants()
Joueur.pokemons_on_map()

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

             ########## Lancement ###########     OK

##############################################################

class Window_Lancement_combat (QMainWindow,Ui_Lancement_combat,music):
    def __init__(self, parent=None):
        super(Window_Lancement_combat, self).__init__(parent)
        self.setupUi(self)
        
        self.acteur_combat()
        self.PASS.clicked.connect(self.change_window)
        self.pokemon_adversaire= Dresseur.dict_pokemons[Carte.adversaire[0]]
        
        
    def change_window(self):
        self.next_window_1 = Window_Zone_de_bataille ()
        self.next_window_1.show()
        self.next_window_2 = Window_Selection_pokemon ()
        self.next_window_2.show()
        self.hide()
        

    def acteur_combat(self):
         
        noms =player_profil.pokemons_combattants
        Joueur = player_profil.Dressur
        pokemon_1= Dresseur.dict_pokemons[noms[0]]
        pokemon_2= Dresseur.dict_pokemons[noms[1]]
        pokemon_3= Dresseur.dict_pokemons[noms[2]]
        
        self.liste_combattants=[pokemon_1,pokemon_2,pokemon_3]
        self.Nom_Pokemon_1.setText(noms[0])
        self.Nom_Pokemon_2.setText(noms[1])
        self.Nom_Pokemon_3.setText(noms[2])
        
        self.Pokemon_1.setPixmap(QtGui.QPixmap( pokemon_1.Image))
        self.Pokemon_2.setPixmap(QtGui.QPixmap( pokemon_2.Image))
        self.Pokemon_3.setPixmap(QtGui.QPixmap( pokemon_3.Image))
        
        self.Adversaire.setPixmap(QtGui.QPixmap(self.pokemon_adversaire.Image))            #A modifier
        self.Nom_adversaire.setText(self.pokemon_adversaire.nom)
        
        self.Joueur.setPixmap(QtGui.QPixmap(Joueur.Image))
        
        
##############################################################

             ########## Selection ###########     OK

##############################################################

class Window_Selection_pokemon (QMainWindow,Ui_Selection_pokemon,music):
    def __init__(self, parent=None):
        super(Window_Selection_pokemon, self).__init__(parent)
        self.setupUi(self)
        self.Pokemon_1_etat= False
        self.Pokemon_2_etat= False
        self.Pokemon_3_etat= False
        self.Pokemon_1.clicked.connect(self.press_Pokemon_1)
        self.Pokemon_2.clicked.connect(self.press_Pokemon_2)
        self.Pokemon_3.clicked.connect(self.press_Pokemon_3)
        self.liste_combattants=Window_Lancement_combat.liste_combattants
        self.choix_pokemon_attaquant()
        
        self.Pokemon_1_etat= False
        self.Pokemon_2_etat= False
        self.Pokemon_3_etat= False
        
    def press_Pokemon_1(self):
        self.Pokemon_1_etat =True
        
    def press_Pokemon_2(self):
        self.Pokemon_2_etat =True
        
    def press_Pokemon_3(self):
        self.Pokemon_2_etat =True
        
    def choix_pokemon_attaquant(self):
        
        Combattants = self.liste_combattants
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(Combattants[0].image), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Pokemon_1.setIcon(icon1)
        
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(Combattants[1].image), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Pokemon_2.setIcon(icon2)
        
        icon3 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(Combattants[2].image), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Pokemon_3.setIcon(icon3)
        
        if self.Pokemon_1_etat ==True:
            self.pokemon_zone_combat=Combattants[2]
            
        elif self.Pokemon_2_etat ==True:
            self.pokemon_zone_combat=Combattants[2]
            
        elif self.Pokemon_3_etat ==True:
            self.pokemon_zone_combat=Combattants[2]
            
        self.close()
        


##############################################################

             ########## Combat ###########

##############################################################
        
class Window_Zone_de_bataille (QMainWindow,Ui_Zone_de_bataille):
    def __init__(self, parent=None):
        super(Window_Zone_de_bataille, self).__init__(parent)
        self.setupUi(self)
        self.pokemon_zone_attente=Window_Lancement_combat.liste_combattants
        self.pokemon_zone_combat= Window_Selection_pokemon.pokemon_zone_combat
        self.pokemon_zone_repos=[]
        self.fuir_etat=False
        self.Pokemon_1_etat= False
        self.Pokemon_2_etat= False
        self.Pokemon_3_etat= False
        self.pokemon_zone_adversaire=self.pokemon_adversaire
        self.Fuir.clicked.connect(self.fuite)
        self.resultat()
        self.acteur_combat()
        
        
    def press_Pokemon_1(self):
        self.Pokemon_1_etat =True
        
    def press_Pokemon_2(self):
        self.Pokemon_2_etat =True
        
    def press_Pokemon_3(self):
        self.Pokemon_2_etat =True
    
        
    
    # def attaque_neutre():
    #     return 0
    
    # def attaque_elementaire():
    #     return 0
    
    # def pokemon_KO(self):
    #     return 0
    def fuite(self): #ok
        self.fuir_etat= True
        
    def affichage_HP(self):   # ok 
        self.PV_adversaire.setText(str(self.pokemon_zone_adversaire.HP_combat)+" / "+str(self.pokemon_zone_adversaire.HP))
        self.PV_attaquant.setText(str(self.pokemon_zone_combat.HP_combat)+" / "+str(self.pokemon_zone_combat.HP))
             
    def Victoire(self):   # ok  
        pokemon_adversaire= self.pokemon_zone_adversaire
        pokemon_adversaire.HP_combat=0
        if pokemon_adversaire.HP_combat==0:
            return True
    
    
    def defaite(self): # ok
        if len(Joueur.pokemons_zone_repos)==3  or self.fuir_etat ==True:
            return True
            
    def resultat(self): # ok
        if self.Victoire() ==True:
            Window_Victoire_combat().show()
            self.hide()
        elif self.defaite()==True:
            Window_Combat_perdu().show()
            self.hide()
        
    def echange_pokemon(self):  #ok
        
        pokemon_attaquant=Window_Selection_pokemon.pokemon_zone_combat
        
        for bouton in [self.Pokemon_1,self.Pokemon_2,self.Pokemon_3]:
            if bouton.icon() == pokemon.image:
                bouton.setEnabled(True)
                
        if self.Pokemon_1_etat ==True:
            self.pokemon_zone_combat= self.pokemon_zone_attente[0]
            self.pokemon_attaquant.setPixmap(QtGui.QPixmap(pokemon_attaquant.image))
            
        elif self.Pokemon_2_etat ==True:
            self.pokemon_zone_combat= self.pokemon_zone_attente[0]
            self.pokemon_attaquant.setPixmap(QtGui.QPixmap(pokemon_attaquant.image))
            
        elif self.Pokemon_3_etat ==True:
            self.pokemon_zone_combat= self.pokemon_zone_attente[0]
            self.pokemon_attaquant.setPixmap(QtGui.QPixmap(pokemon_attaquant.image))
       
    
        
    
    def vitesse(self):  #ok
      
        if self.pokemon_zone_combat.Speed >= self.pokemon_zone_adversaire.Speed:
            return self.pokemon_zone_combat
        else:
            return self.pokemon_zone_adversaire
        

    def acteur_combat(self):  #ok
        
        pokemon_adversaire= Window_Lancement_combat.pokemon_adversaire
        noms =player_profil.pokemons_combattants
        Joueur = player_profil.Dressur
        
        Combattants = self.liste_combattants
        
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(Combattants[0].image), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Pokemon_1.setIcon(icon1)
        
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(Combattants[1].image), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Pokemon_2.setIcon(icon2)
        
        icon3 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(Combattants[2].image), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Pokemon_3.setIcon(icon3)
        
        self.pokemon_attaquant.setPixmap(QtGui.QPixmap(self.pokemon_zone_combat.image))
            
        for bouton in [self.Pokemon_1,self.Pokemon_2,self.Pokemon_3]:
            if bouton.icon() == pokemon.image:
                bouton.setEnabled(False)
                
        
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../Images_interface/Types/"+pokemon_attaquant.type1+".png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Type1.setIcon(icon4)
        self.Type1.textEdit.toolTip(pokemon_attaquant.type1)
        self.Type1.setToolTip(pokemon_attaquant.type1)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../Images_interface/Types/"+pokemon_attaquant.type2+".png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Type2.setIcon(icon5)
        self.Type2.textEdit.toolTip(pokemon_attaquant.type2)
        self.Adversaire.setPixmap(QtGui.QPixmap(pokemon_adversaire.Image))            #A modifier
        
        self.Joueur.setPixmap(QtGui.QPixmap(Joueur.Image))
        
    def close_window(self): #ok
        self.hide()

##############################################################

             ########## Resultat ###########

##############################################################

class Window_Combat_perdu (QMainWindow,Ui_Combat_perdu):
    def __init__(self, parent=None):
        super(Window_Combat_perdu, self).__init__(parent)
        self.setupUi(self)
        self.PASS.clicked.connect(self.change_window)
        self.PASS.clicked.connect(Window_Zone_de_bataille.close_window)
        
    def change_window(self):
        self.next_window = Window_Combat_perdu ()   # A changer
        self.next_window.show()
        self.close()
        
        
class Window_Victoire_combat (QMainWindow,Ui_Victoire_combat ):
    def __init__(self, parent=None):
        super(Window_Victoire_combat, self).__init__(parent)
        self.setupUi(self)
        self.PASS.clicked.connect(self.change_window)
        self.PASS.clicked.connect(Window_Zone_de_bataille.close_window)
        
    def change_window(self):
        self.next_window = Window_Capture_pokemon ()   # A changer
        self.next_window.show()
        self.close()
        
        
##############################################################

             ########## Capture ###########      OK

##############################################################

class Window_Capture_pokemon(QMainWindow,Ui_Capture_pokemon):
    def __init__(self, parent=None):
        super(Window_Capture_pokemon, self).__init__(parent)
        self.setupUi(self)
        self.Capture()
        
    def change_window(self):
        self.second_window = Window_Zone_de_bataille ()
        self.second_window.show()
        self.hide()
        Victoire().hide()
        
    def Capture(self):
        nom=list(pokemon_adversaire.keys())[0]
        image=pokemon_adversaire[nom].Image
        Joueur.attrape_pokemon(pokemon_adversaire[nom])
        self.Nom_pokemon.setText(nom)
        self.Pokemon_Attrape.setPixmap(QtGui.QPixmap(image))
        del pokemon_adversaire[nom]
        
if __name__ == "__main__":
    
    def run_app():
        app = QApplication(sys.argv)
        
        # Depart =Window_Lancement_combat()
        # Battaille= Window_Zone_de_bataille()
        # Reussite=Window_Victoire_combat()
        # Defaite=Window_Combat_perdu()
        # New_pokemon =Window_Capture_pokemon()
     
        mainWin = Window_Lancement_combat()
        mainWin.show()
        app.exec_()
    fenetre=run_app()
    
    