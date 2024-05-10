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
from Player_profil import Ui_Player_profil
from Bienvenue import Ui_Bienvenue
from Inventaire_Pokemon import Ui_Inventaire_Pokemon
from Classes_Pokemons import *

poke =Seadra()
Joueur= Dresseur("Sacha",'Masculin')
liste_pokemons_combattants=["Nidoking", "Graveler", "Seadra"]
pokemon_adversaire =Pikachu()
# poke =Seadra()
# Joueur.choix_pokemons_combattants()
# Joueur.pokemons_on_map()


class Window_Bienvenue (QMainWindow,Ui_Bienvenue):
    def __init__(self, parent=None):
        super(Window_Bienvenue, self).__init__(parent)
        self.setupUi(self)
        
        self.play.clicked.connect(self.update_pseudo)
        # self.play.clicked.connect(self.change_window)

    def update_pseudo(self):
        pseudo = self.player_name.text()
        age = self.player_age.text()
        genre = self.gender_choice.currentText()
        Joueur = Dresseur(pseudo, genre)
        
        self.player_profil = Window_Player_profil(Joueur)
        self.player_profil.show()
        self.close()
        
    
        

class Window_Player_profil (QMainWindow,Ui_Player_profil):
    def __init__(self, Joueur, parent=None):
        super(Window_Player_profil, self).__init__(parent)
        self.setupUi(self)
        self.Joueur= Joueur
        self.choix_pokemons.clicked.connect(self.afficher_inventaire)
        self.change_pokemon.clicked.connect(self.changement_combattants)
        self.close_window.clicked.connect(self.close)
        
        self.pokemons_combats=[] # Liste pour stocker les pokemons choisis
        print(self.Joueur.nom)
        print(self.Joueur.genre)

    def afficher_inventaire(self):
        self.inventaire_window = Window_Inventaire_Pokemon() # Ouvrir la fenêtre de l'inventaire des pokemons
        self.inventaire_window.tableWidget.cellClicked.connect(self.selectionner_pokemon)
        self.inventaire_window.show()

    def selectionner_pokemon(self, row, col):
        pokemon_selectionne = self.inventaire_window.tableWidget.cellWidget(row, col).layout().itemAt(1).widget().text()    # Récupérer le nom du pokemon sélectionné dans le tableau
        if len(self.pokemons_combats) == 3:
            print("La liste de vos pokemons est pleine")
        if pokemon_selectionne not in self.pokemons_combats: # Vérifier si le pokemon sélectionné n'est pas déjà dans la liste des pokemons choisis
            self.pokemons_combats.append(pokemon_selectionne) # Ajouter le pokemon sélectionné dans la liste des pokemons choisis
            # Mettre à jour les labels avec les pokemons choisis
            if len(self.pokemons_combats) == 1:
                self.pokemon_1.setPixmap(QtGui.QPixmap("../Images/Pokemon_images/" + pokemon_selectionne.replace("'","")+".png").scaled(141, 101))
            elif len(self.pokemons_combats) == 2:
                self.pokemon_2.setPixmap(QtGui.QPixmap("../Images/Pokemon_images/" + pokemon_selectionne.replace("'","")+".png").scaled(141, 101))
            elif len(self.pokemons_combats) == 3:
                self.pokemon_3.setPixmap(QtGui.QPixmap("../Images/Pokemon_images/" + pokemon_selectionne.replace("'","")+".png").scaled(141, 101))

    def changement_combattants(self):
        self.pokemons_combats = [] # Vider la liste de pokemon la liste de pokemon
        self.pokemon_1.setPixmap(QtGui.QPixmap(""))
        self.pokemon_1.setText("1er choix")
        self.pokemon_2.setPixmap(QtGui.QPixmap(""))
        self.pokemon_2.setText("2ème choix")
        self.pokemon_3.setPixmap(QtGui.QPixmap(""))
        self.pokemon_3.setText("3ème choix")

class Window_Inventaire_Pokemon (QMainWindow,Ui_Inventaire_Pokemon):
    def __init__(self, parent=None):
        super(Window_Inventaire_Pokemon, self).__init__(parent)
        self.setupUi()
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

             ########## Lancement ###########     OK Besoin de carte

##############################################################

class Window_Lancement_combat (QMainWindow,Ui_Lancement_combat):
    def __init__(self,Joueur= Dresseur("Sacha",'Masculin'),pokemon_adversaire =Pikachu(),liste_pokemons_combattants=["Nidoking", "Graveler", "Seadra"] , parent=None): #Joueur, pokemon_adversaire, liste_pokemons_combattants
        super(Window_Lancement_combat, self).__init__(parent)
        self.setupUi(self)
        self.joueur= Joueur
        self.pokemon_adversaire=pokemon_adversaire
        self.Combattants=liste_pokemons_combattants
        self.Zone_d_attente()
        self.acteur_combat()
        self.PASS.clicked.connect(self.change_window)
        
        
    def Zone_d_attente(self) :
        pokemon_1= Dresseur.dict_pokemons[self.Combattants[0]]
        pokemon_2= Dresseur.dict_pokemons[self.Combattants[1]]
        pokemon_3= Dresseur.dict_pokemons[self.Combattants[2]]
        self.pokemons_zone_attente =[ pokemon_1, pokemon_2, pokemon_3 ]
        
    def close_window(self): #ok
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
        self.Pokemon_1.clicked.connect(self.choix_pokemon_attaquant)

        
        self.Pokemon_2.clicked.connect(self.press_Pokemon_2)
        self.Pokemon_2.clicked.connect(self.choix_pokemon_attaquant)

        
        self.Pokemon_3.clicked.connect(self.press_Pokemon_3)
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
        
        self.acteur_combat()
        self.affichage_HP()
        
        self.fuir_etat=False
        self.Pokemon_1_etat= False
        self.Pokemon_2_etat= False
        self.Pokemon_3_etat= False
        self.Pokemon_1.clicked.connect(self.press_Pokemon_1)
        self.Pokemon_2.clicked.connect(self.press_Pokemon_2)
        self.Pokemon_3.clicked.connect(self.press_Pokemon_3)
        self.Fuir.clicked.connect(self.fuite)
        self.Echange.clicked.connect(self.echange_pokemon)
        
        
    def acteur_combat(self):  #ok
        
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
        
        self.Adversaire.setPixmap(QtGui.QPixmap(self.pokemon_zone_adversaire.Image))
        
        self.Joueur.setPixmap(QtGui.QPixmap(self.joueur.Image))
        
        
    def affichage_HP(self):   # ok 
        self.PV_adversaire.setText(str(self.pokemon_zone_adversaire.HP_combat)+" / "+str(self.pokemon_zone_adversaire.HP))
        self.PV_attaquant.setText(str(self.pokemon_zone_combat.HP_combat)+" / "+str(self.pokemon_zone_combat.HP))
            
        
    def press_Pokemon_1(self):
        self.Pokemon_1_etat =True
        
    def press_Pokemon_2(self):
        self.Pokemon_2_etat =True
        
    def press_Pokemon_3(self):
        self.Pokemon_3_etat =True

    def fuite(self): #ok
        self.fuir_etat= True 
        self.next_window=Window_Combat_perdu(self)
        self.next_window.show()
        
    def Victoire(self):   # ok  
        if self.pokemon_zone_adversaire.HP_combat==0:
            self.next_window=Window_Victoire_combat(self)
            self.next_window.show()
    
    
    def defaite(self): # ok
        if len(self.pokemons_zone_repos)==3:
            self.next_window=Window_Combat_perdu(self)
            self.next_window.show()
            self.hide()
        
   
    def echange_pokemon(self):  #ok
        
        for bouton in [self.Pokemon_1,self.Pokemon_2,self.Pokemon_3]:
            icon = bouton.icon().pixmap(bouton.icon().availableSizes()[0]).cacheKey()
            image =self.Pokemon_attaquant.pixmap().cacheKey()
            if icon == image:
                bouton.setStyleSheet("background-color: transparent")
                bouton.setEnabled(True)
                
        print(self.Pokemon_1_etat)
        print(self.Pokemon_2_etat)
        print(self.Pokemon_3_etat)
        if self.Pokemon_1_etat :
            self.Pokemon_zone_combat= self.pokemons_zone_attente[0]
            self.Pokemon_1.setEnabled(False)
            self.Pokemon_1.setStyleSheet("background-color: rgba(255, 77, 61, 0.3)")
            self.Pokemon_1_etat =False
            print(self.Pokemon_zone_combat.Image)
        
        elif self.Pokemon_2_etat :
            self.Pokemon_zone_combat= self.pokemons_zone_attente[1]
            self.Pokemon_2.setEnabled(False)
            self.Pokemon_2.setStyleSheet("background-color: rgba(255, 77, 61, 0.3)")
            self.Pokemon_2_etat =False
            print(self.Pokemon_zone_combat)

        
        elif self.Pokemon_3_etat :
            self.Pokemon_zone_combat= self.pokemons_zone_attente[2]
            self.Pokemon_3.setEnabled(False)
            self.Pokemon_3.setStyleSheet("background-color: rgba(255, 77, 61, 0.3)")
            self.Pokemon_3_etat =False
            print(self.Pokemon_zone_combat)
            
            
            
        self.Pokemon_attaquant.setPixmap(QtGui.QPixmap(self.pokemon_zone_combat.Image))
        self.affichage_HP()
        print(self.Pokemon_zone_combat.HP_combat)
        
    # def attaque_neutre():
    #     return 0
    
    # def attaque_elementaire():
    #     return 0
    
    def pokemon_KO(self):
        if self.pokemon_zone_combat.HP_combat == 0:
            for bouton in [self.Pokemon_1,self.Pokemon_2,self.Pokemon_3]:
                if bouton.icon() == self.Pokemon_attaquant.pixmap():
                    bouton.setEnabled(False)
                    
    def vitesse(self):  #ok
      
        if self.pokemon_zone_combat.Speed >= self.pokemon_zone_adversaire.Speed:
            return self.pokemon_zone_combat
        else:
            return self.pokemon_zone_adversaire
        
    def close_window(self): #ok
        self.close()

##############################################################

             ########## Resultat ###########

##############################################################

class Window_Combat_perdu (QMainWindow,Ui_Combat_perdu):
    def __init__(self, Zone_de_bataille, parent=None):
        super(Window_Combat_perdu, self).__init__(parent)
        self.setupUi(self)
        self.Bataille= Zone_de_bataille
        self.PASS.clicked.connect(self.change_window)
        
    def change_window(self):
        self.next_window = Window_Victoire_combat (self.Bataille)  
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

             ######### Capture ###########      OK

#############################################################

class Window_Capture_pokemon(QMainWindow,Ui_Capture_pokemon):
    def __init__(self, Bataille, parent=None):
        super(Window_Capture_pokemon, self).__init__(parent)
        self.setupUi(self)
        self.joueur= Bataille.joueur
        self.pokemon_adversaire =  Bataille.pokemon_zone_adversaire
        self.PASS.clicked.connect(self.change_window)
        self.Capture()
        
    def change_window(self):
        # self.next_window = Window_carte ()
        # self.next_window.show()
        self.close()
        
    def Capture(self):
        self.joueur.attrape_pokemon(self.pokemon_adversaire)
        self.Nom_pokemon.setText(self.pokemon_adversaire.nom)
        self.Pokemon_Attrape.setPixmap(QtGui.QPixmap(self.pokemon_adversaire.Image))
        
if __name__ == "__main__":
    
    def run_app():
        app = QApplication(sys.argv)
        # mainWin = Window_Zone_de_bataille(pokemon_attaquant =Seadra(),joueur= Dresseur("Sacha",'Masculin'),pokemons_zone_attente=[Nidoking(), Graveler(), Seadra()],adversaire =Pikachu())
        mainWin = Window_Lancement_combat()
        mainWin.show()
        app.exec_()
    fenetre=run_app()
    
    