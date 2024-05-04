# -*- coding: utf-8 -*-
"""
Created on Fri May  3 11:59:02 2024

@author: Hp Probook i7
"""    

import csv

# modèle de pokemon
modele=("class {nom} (Pokemon):\n"+"    def __init__(self, nom='{nom}', type1='{type1}', type2='{type2}', Total={Total},HP={HP}, Attack={Attack}, Defense={Defense}, Sp_Atk={Sp_Atk}, Sp_Def={Sp_Def}, Speed={Speed}, Generation='{Generation}', Legendary={Legendary}):\n"
        +"        super().__init__( nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary )\n\n")


def generateur_pokemon(fichier):
    
    Classes_Pokemons=[]
    dict_pokemons="{ "
    
    with open(fichier,mode="r") as file:
        csvfile= csv.reader(file)
        next(csvfile)
        for ligne in csvfile:
            nom_pokemon=ligne[1]
            nom_pokemon = nom_pokemon.replace("h'd","hd").replace("Nidoranâ™€","Nidoran_male").replace(". ","_").replace("Nidoranâ™‚","Nidoranâ™").replace("Nidoranâ™","Nidoran_female")
            Classe= modele.format( nom=nom_pokemon, type1=ligne[2], type2=ligne[3], Total=ligne[4], HP=ligne[5], Attack=ligne[6], Defense=ligne[7], Sp_Atk=ligne[8], Sp_Def=ligne[9],Speed=ligne[10] , Generation=ligne[11] , Legendary=ligne[12])
            dict_pokemons+="'"+nom_pokemon+"' : "+nom_pokemon+"(), "
            #Fait en sorte que l'absence d'information soit retourné par null et non par le string None
            Classe = Classe.replace("''","'null'")
            Classes_Pokemons.append(Classe)
        dict_pokemons+="}"
        
        return Classes_Pokemons,dict_pokemons
        
if __name__=='__main__':
    Types={"Steel":0, "Fighting":1 ,"Dragon":2 ,"Water":3, "Fire":4 ,"Electrik":5, "Fairy":6, "Ice":7, "Bug":8 ,"Normal":9 ,"Grass":10, "Poison":11 ,"Psychic":12, "Ground":13, "Rock":14, "Ghost":15, "Darness":16, "Flying":17}
    
    
    fichier="../data/pokemon_first_gen.csv"
    Pokemons,dict_pokemons=generateur_pokemon(fichier)
    #Création du fichier sql de sortie
    Fichier_Classes_Pokemons = open("Pokemons.py", "w")
    #creation de la classe mere
    Classe_mere=("from abc import abstractmethod, ABCMeta \nimport numpy as np \n\n"+"class Pokemon(metaclass=ABCMeta):\n\n"
                   +"    Types="+str(Types)+"\n\n    Affinites = np.genfromtxt ('../data/Donnees_crees/Affinites.csv', delimiter =';',skip_header=1,usecols=range(1,19))\n"
                   +"\n    def __init__(self, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary ):\n"
                   +"        self.nom=nom\n"
                   +"        self.type1=type1 \n"
                   +"        self.type2=type2 \n"
                   +"        self.Total= Total \n"
                   +"        self.HP=  HP\n"
                   +"        self.Attack= Attack \n"
                   +"        self.Defense= Defense \n"
                   +"        self.Sp_Atk= Sp_Atk \n"
                   +"        self.Sp_Def= Sp_Def \n"
                   +"        self.Speed= Speed \n"
                   +"        self.Generation= Generation \n"
                   +"        self.Legendary= Legendary \n\n\n")
    
    Fichier_Classes_Pokemons.write(Classe_mere)
    for ligne in Pokemons :
        Fichier_Classes_Pokemons.write(ligne)
        
    Fichier_Classes_Pokemons.write("if __name__=='__main__':\n\n    dict_pokemons="+dict_pokemons+"\n    pi=Pikachu()\n    Mewtou=Mew()\n    Drac=Drowzee()")
    Fichier_Classes_Pokemons.close()