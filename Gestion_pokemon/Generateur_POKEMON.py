# -*- coding: utf-8 -*-
"""
Created on Fri May  3 11:59:02 2024

@author: Hp Probook i7
"""    

import csv
import numpy as np

# Modele de creation de pokemon en str
modele=("class {nom} (Pokemon):\n"+"    def __init__(self, ID ='{ID}',nom='{nom}', type1='{type1}', type2='{type2}', Total={Total},HP={HP}, Attack={Attack}, Defense={Defense}, Sp_Atk={Sp_Atk}, Sp_Def={Sp_Def}, Speed={Speed}, Generation='{Generation}', Legendary={Legendary},Image='{Image}', Coordonnees={Coordonnees}):\n"
        +"        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )\n\n")

# Fonction qui creera une liste avec toutes les classes de pokemons
def generateur_pokemon(fichier):
    """
    Fonction qui ecrit les sous-classes pokemons, un dictionnaire renfermant des objets pokemons et un dictionnaire renfermant le nom de chaque pokemon associe a son identifiant
    Parameters
    ----------
    fichier : string
        Notre fichier de départ avec tous les pokemons et leurs attributs.

    Returns
    -------
    Classes_Pokemons : List
        Liste avec toutes les sous-classes de pokemons.
    dict_pokemons : dict
        Dictionnaire renfermant des objets pokemons.
    ID_pokemons : dict
        Dictionnaire renfermant le nom de chaque pokemon associe a son identifiant.

    """
    
    # Initialisation des resultats de la fonction
    Classes_Pokemons=[]
    dict_pokemons="{ "
    ID_pokemons="{ "
    
    # Ouverture et lecture de notre fichier CSV
    with open(fichier,mode="r") as file:
        csvfile= csv.reader(file)
        next(csvfile)
        
        # Lecture des lignes du CSV et remplissage de nos conteneurs
        for ligne in csvfile:
            
            nom_pokemon=ligne[1]
            
            # Gestion des differents carateres pouvant occasionnes des problemes
            nom_pokemon = nom_pokemon.replace("h'd","hd").replace("Nidoranâ™€","Nidoran_male").replace(". ","_").replace("Nidoranâ™‚","Nidoranâ™").replace("Nidoranâ™","Nidoran_female")
            
            # Indications des attributs des pokemons
            Classe= modele.format( ID = ligne[0],
                                  nom=nom_pokemon,
                                  type1=ligne[2],
                                  type2=ligne[3],
                                  Total=ligne[4],
                                  HP=ligne[5],
                                  Attack=ligne[6],
                                  Defense=ligne[7],
                                  Sp_Atk=ligne[8],                          #Attributs des pokemons récupérés dans le fichier csv
                                  Sp_Def=ligne[9],
                                  Speed=ligne[10],
                                  Generation=ligne[11] ,
                                  Legendary=ligne[12],
                                  Image="../Images/Pokemon_images/"+nom_pokemon+".png",
                                  Coordonnees=str(ligne[13])+","+str(ligne[14]))
            
            # Remplissage des dictionnaires
            dict_pokemons+="'"+nom_pokemon+"' : "+nom_pokemon+"(), "
            ID_pokemons+="'"+ligne[0]+"' : '"+nom_pokemon+"', "
            
            #Fait en sorte que l'absence d'information soit retourné par null et non par des vides
            Classe = Classe.replace("''","'null'")
            
            # Remplissage du conteneurs de classes
            Classes_Pokemons.append(Classe)
            
            # Fermeture des dictionnaires
        dict_pokemons+="}"
        ID_pokemons+="}"
        
        # Renvoie denos conteneurs
        return Classes_Pokemons,dict_pokemons,ID_pokemons
        
if __name__=='__main__':
    
    # Dictionnaire associant un type a un numero
    Types={"Steel":0, "Fighting":1 ,"Dragon":2 ,"Water":3, "Fire":4 ,"Electric":5, "Fairy":6, "Ice":7, "Bug":8 ,"Normal":9 ,"Grass":10, "Poison":11 ,"Psychic":12, "Ground":13, "Rock":14, "Ghost":15, "Darness":16, "Flying":17, "null": 18}
    
    # Listes des 13 pokemons ayant les plus hauts totaux
    pokemons_13totals_croissants=["150","149","151","144","145","146","59","130","143","131","6","9","3"]
    
    # Notre fichier de départ avec tous les pokemons et leurs attributs
    fichier="../data/Donnees_creees/fichier_pokemon.csv"
    
    Affinites = str(np.genfromtxt ('../data/Donnees_creees/Affinites.csv', delimiter =';',skip_header=1,usecols=range(1,19)).tolist())
    
    # Recuperation de nos conteneurs
    Pokemons,dict_pokemons,ID_pokemons=generateur_pokemon(fichier)
    
    #Création du fichier python d'ecriture
    Fichier_Classes_Pokemons = open("Pokemons2.py", "w")
    
    #Import des bibliotheques et creation de la classe mere en chaîne de caractère
    Classe_mere=("from abc import ABCMeta \nimport numpy as np \nimport random as rd\n\n"
                   +"##############################################################\n\n       ########## Classe Parente pokemon ###########\n\n"
                   +"##############################################################                \n\n\n"
                   +"class Pokemon(metaclass=ABCMeta):\n\n"
                   +"    # Dictionnaire associant un type a un numero \n    Types="+str(Types)+"\n\n    #Matrice de relations d'affinites des types des pokemons \n    Affinites = np.array("+Affinites+")\n"
                   +"\n    #Constructeur"
                   +"\n    def __init__(self, ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees ):\n"
                   +"        self.ID=ID\n"
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
                   +"        self.Legendary= Legendary \n"
                   +"        self.Image= Image \n"
                   +"        self.Coordonnees= Coordonnees \n\n\n       ########## Methodes ###########\n\n\n##############################################"
                   +"################\n\n       ########## Sous-classes pokemons ###########\n\n##############################################################                \n\n\n")
    
    # Ecriture de la classe parente dans le fichier python
    Fichier_Classes_Pokemons.write(Classe_mere)
    
    # Boucle d'ecriture des sous_classes pokemons
    for classe in Pokemons :
        Fichier_Classes_Pokemons.write(classe)
    
    # Ecriture de la zone de test et des conteneurs
    Fichier_Classes_Pokemons.write(("if __name__=='__main__':\n\n##############################################################\n\n       ########## Donnees utiles ###########"
                                    +"\n\n##############################################################                "
                                    +"\n\n    dict_pokemons="+dict_pokemons+"\n\n    list_pokemons= list(dict_pokemons.keys()) \n\n    ID_pokemons= "
                                    +ID_pokemons+"\n\n    pokemons_13totals_croissants="+str(pokemons_13totals_croissants)
                                    +"\n\n##############################################################\n\n       ########## Test ###########\n\n##############################################################                \n"
                                    +"\n    pi=Pikachu()\n    Mewtou=Mew()\n    Drac=Drowzee()"))
    
    # Fermeture du fichier python
    Fichier_Classes_Pokemons.close()