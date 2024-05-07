from abc import ABCMeta 
import numpy as np
import random as rd

##############################################################

       ########## Classe Parente pokemon ###########

##############################################################                


class Pokemon(metaclass=ABCMeta):

    # Dictionnaire associant un type a un numero 
    Types={'Steel': 0, 'Fighting': 1, 'Dragon': 2, 'Water': 3, 'Fire': 4, 'Electric': 5, 'Fairy': 6, 'Ice': 7, 'Bug': 8, 'Normal': 9, 'Grass': 10, 'Poison': 11, 'Psychic': 12, 'Ground': 13, 'Rock': 14, 'Ghost': 15, 'Darness': 16, 'Flying': 17}

    #Matrice de relations d'affinites des types des pokemons 
    Affinites = np.genfromtxt ('../data/Donnees_crees/Affinites.csv', delimiter =';',skip_header=1,usecols=range(1,19))

    #Constructeur
    def __init__(self, ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees ):
        self.ID=ID
        self.nom=nom
        self.type1=type1 
        self.type2=type2 
        self.Total= Total 
        self.HP=  HP
        self.Attack= Attack 
        self.Defense= Defense 
        self.Sp_Atk= Sp_Atk 
        self.Sp_Def= Sp_Def 
        self.Speed= Speed 
        self.Generation= Generation 
        self.Legendary= Legendary 
        self.Image= Image 
        self.Coordonnees= Coordonnees 


       ########## Methodes ###########

    def attaque_neutre(self,pokemon):
        """
        Fonction qui calcule et applique les dommages que reçoit un pokemon d'une attaque neutre

        Parameters
        ----------
        pokemon : sous-classe de pokemon
            Il s'agit du pokemon qui se fait attaquer.

        Returns
        -------
        Dommage : integer
            Nombre de points de vie retire.

        """
        Dommage=self.Attack-pokemon.Defense
        # Retour a 0 pour les dommages negatifs 
        if Dommage <0 :
            Dommage=0
            
        # Application des dommages
        pokemon.HP=pokemon.HP-Dommage
        
        # Retour a 0 pour les points de vie negatifs
        if pokemon.HP<0:
            pokemon.HP=0
        return Dommage

    def attaque_elementaire(self,pokemon,choix=False):
        """
        Fonction qui calcule et applique les dommages que reçoit un pokemon d'une attaque elementaire

        Parameters
        ----------
        pokemon : sous-classe de pokemon
            Il s'agit du pokemon qui se fait attaquer.

        Returns
        -------
        Dommage : integer
            Nombre de points de vie retire.

        """
        # Definition du type de l'attaque
        if choix==False or self.type2=='null':
            element=self.type1
        else:
            element=self.type2
            
        # Calcule du coefficient d'affinite de l'attaque elementaire sur un pokemon d'un seul type
        coeff =Pokemon.Affinites[Pokemon.Types[element],Pokemon.Types[pokemon.type1]]
        if pokemon.type2=='null':
            Dommage =self.Sp_Atk*coeff -pokemon.Sp_Def
        else:
            
            # Calcule du coefficient d'affinite de l'attaque elementaire sur un pokemon de type double
            coeff = coeff * Pokemon.Affinites[Pokemon.Types[element],Pokemon.Types[pokemon.type2]]
            Dommage =self.Sp_Atk*coeff -pokemon.Sp_Def
            
        # Retour a 0 pour les dommages negatifs 
        if Dommage <0 :
            Dommage=0
            
        # Application des dommages
        pokemon.HP=pokemon.HP-Dommage
        
        # Retour a 0 pour les points de vie negatifs
        if pokemon.HP<0:
            pokemon.HP=0
        return Dommage
    
    def pokemon_KO(self):
        """
        Fonction qui signale si un pokemon est hors d'etat de combattre

        Returns
        -------
        bool

        """
        if self.HP==0:
            return True
        

##############################################################

       ########## Sous-classes pokemons ###########

##############################################################


class Bulbasaur (Pokemon):
    def __init__(self, ID ='1',nom='Bulbasaur', type1='Grass', type2='Poison', Total=318,HP=45, Attack=49, Defense=49, Sp_Atk=65, Sp_Def=65, Speed=45, Generation='1', Legendary=False,Image='../data/Pokemon_images/Bulbasaur.PNG', Coordonnees=[31.445398005630054, 5.634905916753981]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Ivysaur (Pokemon):
    def __init__(self, ID ='2',nom='Ivysaur', type1='Grass', type2='Poison', Total=405,HP=60, Attack=62, Defense=63, Sp_Atk=80, Sp_Def=80, Speed=60, Generation='1', Legendary=False,Image='../data/Pokemon_images/Ivysaur.PNG', Coordonnees=[3.586566583915727, 1.8700806450660623]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Venusaur (Pokemon):
    def __init__(self, ID ='3',nom='Venusaur', type1='Grass', type2='Poison', Total=525,HP=80, Attack=82, Defense=83, Sp_Atk=100, Sp_Def=100, Speed=80, Generation='1', Legendary=False,Image='../data/Pokemon_images/Venusaur.PNG', Coordonnees=[1.6634107155798095, 5.776035778221535]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Charmander (Pokemon):
    def __init__(self, ID ='4',nom='Charmander', type1='Fire', type2='null', Total=309,HP=39, Attack=52, Defense=43, Sp_Atk=60, Sp_Def=50, Speed=65, Generation='1', Legendary=False,Image='../data/Pokemon_images/Charmander.PNG', Coordonnees=[0.2009863621576402, 9.941813707933967]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Charmeleon (Pokemon):
    def __init__(self, ID ='5',nom='Charmeleon', type1='Fire', type2='null', Total=405,HP=58, Attack=64, Defense=58, Sp_Atk=80, Sp_Def=65, Speed=80, Generation='1', Legendary=False,Image='../data/Pokemon_images/Charmeleon.PNG', Coordonnees=[26.972490904133043, 9.957007342171252]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Charizard (Pokemon):
    def __init__(self, ID ='6',nom='Charizard', type1='Fire', type2='Flying', Total=534,HP=78, Attack=84, Defense=78, Sp_Atk=109, Sp_Def=85, Speed=100, Generation='1', Legendary=False,Image='../data/Pokemon_images/Charizard.PNG', Coordonnees=[38.04000913626969, 8.57313267355103]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Squirtle (Pokemon):
    def __init__(self, ID ='7',nom='Squirtle', type1='Water', type2='null', Total=314,HP=44, Attack=48, Defense=65, Sp_Atk=50, Sp_Def=64, Speed=43, Generation='1', Legendary=False,Image='../data/Pokemon_images/Squirtle.PNG', Coordonnees=[21.983776955090324, 0.22512059009943575]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Wartortle (Pokemon):
    def __init__(self, ID ='8',nom='Wartortle', type1='Water', type2='null', Total=405,HP=59, Attack=63, Defense=80, Sp_Atk=65, Sp_Def=80, Speed=58, Generation='1', Legendary=False,Image='../data/Pokemon_images/Wartortle.PNG', Coordonnees=[35.29859641052892, 7.154676024593956]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Blastoise (Pokemon):
    def __init__(self, ID ='9',nom='Blastoise', type1='Water', type2='null', Total=530,HP=79, Attack=83, Defense=100, Sp_Atk=85, Sp_Def=105, Speed=78, Generation='1', Legendary=False,Image='../data/Pokemon_images/Blastoise.PNG', Coordonnees=[35.03967606802652, 1.2637612636906115]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Caterpie (Pokemon):
    def __init__(self, ID ='10',nom='Caterpie', type1='Bug', type2='null', Total=195,HP=45, Attack=30, Defense=35, Sp_Atk=20, Sp_Def=20, Speed=45, Generation='1', Legendary=False,Image='../data/Pokemon_images/Caterpie.PNG', Coordonnees=[10.284280337874856, 8.131837232960763]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Metapod (Pokemon):
    def __init__(self, ID ='11',nom='Metapod', type1='Bug', type2='null', Total=205,HP=50, Attack=20, Defense=55, Sp_Atk=25, Sp_Def=25, Speed=30, Generation='1', Legendary=False,Image='../data/Pokemon_images/Metapod.PNG', Coordonnees=[16.077224565073767, 7.457573382363931]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Butterfree (Pokemon):
    def __init__(self, ID ='12',nom='Butterfree', type1='Bug', type2='Flying', Total=395,HP=60, Attack=45, Defense=50, Sp_Atk=90, Sp_Def=80, Speed=70, Generation='1', Legendary=False,Image='../data/Pokemon_images/Butterfree.PNG', Coordonnees=[10.411488304598908, 6.341561499814487]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Weedle (Pokemon):
    def __init__(self, ID ='13',nom='Weedle', type1='Bug', type2='Poison', Total=195,HP=40, Attack=35, Defense=30, Sp_Atk=20, Sp_Def=20, Speed=50, Generation='1', Legendary=False,Image='../data/Pokemon_images/Weedle.PNG', Coordonnees=[14.004459662983972, 2.4462477042614728]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Kakuna (Pokemon):
    def __init__(self, ID ='14',nom='Kakuna', type1='Bug', type2='Poison', Total=205,HP=45, Attack=25, Defense=50, Sp_Atk=25, Sp_Def=25, Speed=35, Generation='1', Legendary=False,Image='../data/Pokemon_images/Kakuna.PNG', Coordonnees=[31.579489094509587, 0.36864263812350195]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Beedrill (Pokemon):
    def __init__(self, ID ='15',nom='Beedrill', type1='Bug', type2='Poison', Total=395,HP=65, Attack=90, Defense=40, Sp_Atk=45, Sp_Def=80, Speed=75, Generation='1', Legendary=False,Image='../data/Pokemon_images/Beedrill.PNG', Coordonnees=[30.221131463264527, 6.990202133741288]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Pidgey (Pokemon):
    def __init__(self, ID ='16',nom='Pidgey', type1='Normal', type2='Flying', Total=251,HP=40, Attack=45, Defense=40, Sp_Atk=35, Sp_Def=35, Speed=56, Generation='1', Legendary=False,Image='../data/Pokemon_images/Pidgey.PNG', Coordonnees=[1.3374632894703442, 8.839749473410937]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Pidgeotto (Pokemon):
    def __init__(self, ID ='17',nom='Pidgeotto', type1='Normal', type2='Flying', Total=349,HP=63, Attack=60, Defense=55, Sp_Atk=50, Sp_Def=50, Speed=71, Generation='1', Legendary=False,Image='../data/Pokemon_images/Pidgeotto.PNG', Coordonnees=[35.34973520494862, 1.5028971264479074]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Pidgeot (Pokemon):
    def __init__(self, ID ='18',nom='Pidgeot', type1='Normal', type2='Flying', Total=479,HP=83, Attack=80, Defense=75, Sp_Atk=70, Sp_Def=70, Speed=101, Generation='1', Legendary=False,Image='../data/Pokemon_images/Pidgeot.PNG', Coordonnees=[13.474982726384358, 8.047377473760394]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Rattata (Pokemon):
    def __init__(self, ID ='19',nom='Rattata', type1='Normal', type2='null', Total=253,HP=30, Attack=56, Defense=35, Sp_Atk=25, Sp_Def=35, Speed=72, Generation='1', Legendary=False,Image='../data/Pokemon_images/Rattata.PNG', Coordonnees=[9.719216127515317, 7.190498902165428]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Raticate (Pokemon):
    def __init__(self, ID ='20',nom='Raticate', type1='Normal', type2='null', Total=413,HP=55, Attack=81, Defense=60, Sp_Atk=50, Sp_Def=70, Speed=97, Generation='1', Legendary=False,Image='../data/Pokemon_images/Raticate.PNG', Coordonnees=[0.48215355998211695, 5.401009788016728]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Spearow (Pokemon):
    def __init__(self, ID ='21',nom='Spearow', type1='Normal', type2='Flying', Total=262,HP=40, Attack=60, Defense=30, Sp_Atk=31, Sp_Def=31, Speed=70, Generation='1', Legendary=False,Image='../data/Pokemon_images/Spearow.PNG', Coordonnees=[24.208457173765538, 1.9507721671594591]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Fearow (Pokemon):
    def __init__(self, ID ='22',nom='Fearow', type1='Normal', type2='Flying', Total=442,HP=65, Attack=90, Defense=65, Sp_Atk=61, Sp_Def=61, Speed=100, Generation='1', Legendary=False,Image='../data/Pokemon_images/Fearow.PNG', Coordonnees=[6.147366073506535, 4.507213079558712]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Ekans (Pokemon):
    def __init__(self, ID ='23',nom='Ekans', type1='Poison', type2='null', Total=288,HP=35, Attack=60, Defense=44, Sp_Atk=40, Sp_Def=54, Speed=55, Generation='1', Legendary=False,Image='../data/Pokemon_images/Ekans.PNG', Coordonnees=[33.77471424112477, 0.8911686696292909]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Arbok (Pokemon):
    def __init__(self, ID ='24',nom='Arbok', type1='Poison', type2='null', Total=438,HP=60, Attack=85, Defense=69, Sp_Atk=65, Sp_Def=79, Speed=80, Generation='1', Legendary=False,Image='../data/Pokemon_images/Arbok.PNG', Coordonnees=[39.77535103003635, 1.8132532779656674]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Pikachu (Pokemon):
    def __init__(self, ID ='25',nom='Pikachu', type1='Electric', type2='null', Total=320,HP=35, Attack=55, Defense=40, Sp_Atk=50, Sp_Def=50, Speed=90, Generation='1', Legendary=False,Image='../data/Pokemon_images/Pikachu.PNG', Coordonnees=[13.875446747283519, 6.14279531708128]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Raichu (Pokemon):
    def __init__(self, ID ='26',nom='Raichu', type1='Electric', type2='null', Total=485,HP=60, Attack=90, Defense=55, Sp_Atk=90, Sp_Def=80, Speed=110, Generation='1', Legendary=False,Image='../data/Pokemon_images/Raichu.PNG', Coordonnees=[29.900492519265775, 9.79318434728133]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Sandshrew (Pokemon):
    def __init__(self, ID ='27',nom='Sandshrew', type1='Ground', type2='null', Total=300,HP=50, Attack=75, Defense=85, Sp_Atk=20, Sp_Def=30, Speed=40, Generation='1', Legendary=False,Image='../data/Pokemon_images/Sandshrew.PNG', Coordonnees=[16.81057591430871, 7.800972002302769]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Sandslash (Pokemon):
    def __init__(self, ID ='28',nom='Sandslash', type1='Ground', type2='null', Total=450,HP=75, Attack=100, Defense=110, Sp_Atk=45, Sp_Def=55, Speed=65, Generation='1', Legendary=False,Image='../data/Pokemon_images/Sandslash.PNG', Coordonnees=[10.909187074734628, 2.8269522443474013]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Nidoran_male (Pokemon):
    def __init__(self, ID ='29',nom='Nidoran_male', type1='Poison', type2='null', Total=275,HP=55, Attack=47, Defense=52, Sp_Atk=40, Sp_Def=40, Speed=41, Generation='1', Legendary=False,Image='../data/Pokemon_images/Nidoran_male.PNG', Coordonnees=[13.433465891832995, 7.358845723340009]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Nidorina (Pokemon):
    def __init__(self, ID ='30',nom='Nidorina', type1='Poison', type2='null', Total=365,HP=70, Attack=62, Defense=67, Sp_Atk=55, Sp_Def=55, Speed=56, Generation='1', Legendary=False,Image='../data/Pokemon_images/Nidorina.PNG', Coordonnees=[23.251337152916754, 3.619901635461562]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Nidoqueen (Pokemon):
    def __init__(self, ID ='31',nom='Nidoqueen', type1='Poison', type2='Ground', Total=505,HP=90, Attack=92, Defense=87, Sp_Atk=75, Sp_Def=85, Speed=76, Generation='1', Legendary=False,Image='../data/Pokemon_images/Nidoqueen.PNG', Coordonnees=[39.814433030513385, 8.092220438401348]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Nidoran_female (Pokemon):
    def __init__(self, ID ='32',nom='Nidoran_female', type1='Poison', type2='null', Total=273,HP=46, Attack=57, Defense=40, Sp_Atk=40, Sp_Def=40, Speed=50, Generation='1', Legendary=False,Image='../data/Pokemon_images/Nidoran_female.PNG', Coordonnees=[10.44921273787959, 4.16222896960959]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Nidorino (Pokemon):
    def __init__(self, ID ='33',nom='Nidorino', type1='Poison', type2='null', Total=365,HP=61, Attack=72, Defense=57, Sp_Atk=55, Sp_Def=55, Speed=65, Generation='1', Legendary=False,Image='../data/Pokemon_images/Nidorino.PNG', Coordonnees=[33.6478912719958, 4.850265355979139]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Nidoking (Pokemon):
    def __init__(self, ID ='34',nom='Nidoking', type1='Poison', type2='Ground', Total=505,HP=81, Attack=102, Defense=77, Sp_Atk=85, Sp_Def=75, Speed=85, Generation='1', Legendary=False,Image='../data/Pokemon_images/Nidoking.PNG', Coordonnees=[2.1398148072313905, 9.843080207241306]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Clefairy (Pokemon):
    def __init__(self, ID ='35',nom='Clefairy', type1='Fairy', type2='null', Total=323,HP=70, Attack=45, Defense=48, Sp_Atk=60, Sp_Def=65, Speed=35, Generation='1', Legendary=False,Image='../data/Pokemon_images/Clefairy.PNG', Coordonnees=[7.289428040681618, 3.9257589063363896]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Clefable (Pokemon):
    def __init__(self, ID ='36',nom='Clefable', type1='Fairy', type2='null', Total=483,HP=95, Attack=70, Defense=73, Sp_Atk=95, Sp_Def=90, Speed=60, Generation='1', Legendary=False,Image='../data/Pokemon_images/Clefable.PNG', Coordonnees=[17.669733888499483, 6.124409475581105]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Vulpix (Pokemon):
    def __init__(self, ID ='37',nom='Vulpix', type1='Fire', type2='null', Total=299,HP=38, Attack=41, Defense=40, Sp_Atk=50, Sp_Def=65, Speed=65, Generation='1', Legendary=False,Image='../data/Pokemon_images/Vulpix.PNG', Coordonnees=[15.66571270709574, 5.220351901527827]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Ninetales (Pokemon):
    def __init__(self, ID ='38',nom='Ninetales', type1='Fire', type2='null', Total=505,HP=73, Attack=76, Defense=75, Sp_Atk=81, Sp_Def=100, Speed=100, Generation='1', Legendary=False,Image='../data/Pokemon_images/Ninetales.PNG', Coordonnees=[12.277596891059218, 4.205844868628205]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Jigglypuff (Pokemon):
    def __init__(self, ID ='39',nom='Jigglypuff', type1='Normal', type2='Fairy', Total=270,HP=115, Attack=45, Defense=20, Sp_Atk=45, Sp_Def=25, Speed=20, Generation='1', Legendary=False,Image='../data/Pokemon_images/Jigglypuff.PNG', Coordonnees=[35.73066085649331, 9.435276416643603]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Wigglytuff (Pokemon):
    def __init__(self, ID ='40',nom='Wigglytuff', type1='Normal', type2='Fairy', Total=435,HP=140, Attack=70, Defense=45, Sp_Atk=85, Sp_Def=50, Speed=45, Generation='1', Legendary=False,Image='../data/Pokemon_images/Wigglytuff.PNG', Coordonnees=[5.296557574930318, 1.0194403973036648]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Zubat (Pokemon):
    def __init__(self, ID ='41',nom='Zubat', type1='Poison', type2='Flying', Total=245,HP=40, Attack=45, Defense=35, Sp_Atk=30, Sp_Def=40, Speed=55, Generation='1', Legendary=False,Image='../data/Pokemon_images/Zubat.PNG', Coordonnees=[36.295269979466596, 3.2267556954207564]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Golbat (Pokemon):
    def __init__(self, ID ='42',nom='Golbat', type1='Poison', type2='Flying', Total=455,HP=75, Attack=80, Defense=70, Sp_Atk=65, Sp_Def=75, Speed=90, Generation='1', Legendary=False,Image='../data/Pokemon_images/Golbat.PNG', Coordonnees=[2.39300993148829, 2.749594918404709]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Oddish (Pokemon):
    def __init__(self, ID ='43',nom='Oddish', type1='Grass', type2='Poison', Total=320,HP=45, Attack=50, Defense=55, Sp_Atk=75, Sp_Def=65, Speed=30, Generation='1', Legendary=False,Image='../data/Pokemon_images/Oddish.PNG', Coordonnees=[17.622421037182896, 7.190637994271031]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Gloom (Pokemon):
    def __init__(self, ID ='44',nom='Gloom', type1='Grass', type2='Poison', Total=395,HP=60, Attack=65, Defense=70, Sp_Atk=85, Sp_Def=75, Speed=40, Generation='1', Legendary=False,Image='../data/Pokemon_images/Gloom.PNG', Coordonnees=[37.32178127627191, 1.196091868192628]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Vileplume (Pokemon):
    def __init__(self, ID ='45',nom='Vileplume', type1='Grass', type2='Poison', Total=490,HP=75, Attack=80, Defense=85, Sp_Atk=110, Sp_Def=90, Speed=50, Generation='1', Legendary=False,Image='../data/Pokemon_images/Vileplume.PNG', Coordonnees=[23.862572386780847, 6.6894285554637865]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Paras (Pokemon):
    def __init__(self, ID ='46',nom='Paras', type1='Bug', type2='Grass', Total=285,HP=35, Attack=70, Defense=55, Sp_Atk=45, Sp_Def=55, Speed=25, Generation='1', Legendary=False,Image='../data/Pokemon_images/Paras.PNG', Coordonnees=[7.480496673714816, 8.714285201572029]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Parasect (Pokemon):
    def __init__(self, ID ='47',nom='Parasect', type1='Bug', type2='Grass', Total=405,HP=60, Attack=95, Defense=80, Sp_Atk=60, Sp_Def=80, Speed=30, Generation='1', Legendary=False,Image='../data/Pokemon_images/Parasect.PNG', Coordonnees=[9.53331535350097, 9.104891976022861]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Venonat (Pokemon):
    def __init__(self, ID ='48',nom='Venonat', type1='Bug', type2='Poison', Total=305,HP=60, Attack=55, Defense=50, Sp_Atk=40, Sp_Def=55, Speed=45, Generation='1', Legendary=False,Image='../data/Pokemon_images/Venonat.PNG', Coordonnees=[31.706479319822375, 6.507066254871954]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Venomoth (Pokemon):
    def __init__(self, ID ='49',nom='Venomoth', type1='Bug', type2='Poison', Total=450,HP=70, Attack=65, Defense=60, Sp_Atk=90, Sp_Def=75, Speed=90, Generation='1', Legendary=False,Image='../data/Pokemon_images/Venomoth.PNG', Coordonnees=[39.17918683127157, 5.910503647901174]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Diglett (Pokemon):
    def __init__(self, ID ='50',nom='Diglett', type1='Ground', type2='null', Total=265,HP=10, Attack=55, Defense=25, Sp_Atk=35, Sp_Def=45, Speed=95, Generation='1', Legendary=False,Image='../data/Pokemon_images/Diglett.PNG', Coordonnees=[14.051430403076637, 0.8257353137796741]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Dugtrio (Pokemon):
    def __init__(self, ID ='51',nom='Dugtrio', type1='Ground', type2='null', Total=405,HP=35, Attack=80, Defense=50, Sp_Atk=50, Sp_Def=70, Speed=120, Generation='1', Legendary=False,Image='../data/Pokemon_images/Dugtrio.PNG', Coordonnees=[33.38495420232057, 1.8654655872836912]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Meowth (Pokemon):
    def __init__(self, ID ='52',nom='Meowth', type1='Normal', type2='null', Total=290,HP=40, Attack=45, Defense=35, Sp_Atk=40, Sp_Def=40, Speed=90, Generation='1', Legendary=False,Image='../data/Pokemon_images/Meowth.PNG', Coordonnees=[8.007563868803835, 2.310769532929281]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Persian (Pokemon):
    def __init__(self, ID ='53',nom='Persian', type1='Normal', type2='null', Total=440,HP=65, Attack=70, Defense=60, Sp_Atk=65, Sp_Def=65, Speed=115, Generation='1', Legendary=False,Image='../data/Pokemon_images/Persian.PNG', Coordonnees=[4.465292662252089, 7.9957265163824935]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Psyduck (Pokemon):
    def __init__(self, ID ='54',nom='Psyduck', type1='Water', type2='null', Total=320,HP=50, Attack=52, Defense=48, Sp_Atk=65, Sp_Def=50, Speed=55, Generation='1', Legendary=False,Image='../data/Pokemon_images/Psyduck.PNG', Coordonnees=[6.881980210047192, 1.165813917357117]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Golduck (Pokemon):
    def __init__(self, ID ='55',nom='Golduck', type1='Water', type2='null', Total=500,HP=80, Attack=82, Defense=78, Sp_Atk=95, Sp_Def=80, Speed=85, Generation='1', Legendary=False,Image='../data/Pokemon_images/Golduck.PNG', Coordonnees=[13.60539110758323, 7.08963064410972]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Mankey (Pokemon):
    def __init__(self, ID ='56',nom='Mankey', type1='Fighting', type2='null', Total=305,HP=40, Attack=80, Defense=35, Sp_Atk=35, Sp_Def=45, Speed=70, Generation='1', Legendary=False,Image='../data/Pokemon_images/Mankey.PNG', Coordonnees=[7.512217781240826, 3.5644020071792317]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Primeape (Pokemon):
    def __init__(self, ID ='57',nom='Primeape', type1='Fighting', type2='null', Total=455,HP=65, Attack=105, Defense=60, Sp_Atk=60, Sp_Def=70, Speed=95, Generation='1', Legendary=False,Image='../data/Pokemon_images/Primeape.PNG', Coordonnees=[16.06478902549337, 9.095765770397758]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Growlithe (Pokemon):
    def __init__(self, ID ='58',nom='Growlithe', type1='Fire', type2='null', Total=350,HP=55, Attack=70, Defense=45, Sp_Atk=70, Sp_Def=50, Speed=60, Generation='1', Legendary=False,Image='../data/Pokemon_images/Growlithe.PNG', Coordonnees=[8.689396080049828, 8.472031711235887]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Arcanine (Pokemon):
    def __init__(self, ID ='59',nom='Arcanine', type1='Fire', type2='null', Total=555,HP=90, Attack=110, Defense=80, Sp_Atk=100, Sp_Def=80, Speed=95, Generation='1', Legendary=False,Image='../data/Pokemon_images/Arcanine.PNG', Coordonnees=[10.846856015618433, 0.4500478397054053]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Poliwag (Pokemon):
    def __init__(self, ID ='60',nom='Poliwag', type1='Water', type2='null', Total=300,HP=40, Attack=50, Defense=40, Sp_Atk=40, Sp_Def=40, Speed=90, Generation='1', Legendary=False,Image='../data/Pokemon_images/Poliwag.PNG', Coordonnees=[14.152178176417367, 4.173121973346358]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Poliwhirl (Pokemon):
    def __init__(self, ID ='61',nom='Poliwhirl', type1='Water', type2='null', Total=385,HP=65, Attack=65, Defense=65, Sp_Atk=50, Sp_Def=50, Speed=90, Generation='1', Legendary=False,Image='../data/Pokemon_images/Poliwhirl.PNG', Coordonnees=[13.17806126754256, 0.16701855231640472]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Poliwrath (Pokemon):
    def __init__(self, ID ='62',nom='Poliwrath', type1='Water', type2='Fighting', Total=510,HP=90, Attack=95, Defense=95, Sp_Atk=70, Sp_Def=90, Speed=70, Generation='1', Legendary=False,Image='../data/Pokemon_images/Poliwrath.PNG', Coordonnees=[8.466679474373503, 1.6341283809330232]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Abra (Pokemon):
    def __init__(self, ID ='63',nom='Abra', type1='Psychic', type2='null', Total=310,HP=25, Attack=20, Defense=15, Sp_Atk=105, Sp_Def=55, Speed=90, Generation='1', Legendary=False,Image='../data/Pokemon_images/Abra.PNG', Coordonnees=[25.6237089762431, 0.5374595926338022]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Kadabra (Pokemon):
    def __init__(self, ID ='64',nom='Kadabra', type1='Psychic', type2='null', Total=400,HP=40, Attack=35, Defense=30, Sp_Atk=120, Sp_Def=70, Speed=105, Generation='1', Legendary=False,Image='../data/Pokemon_images/Kadabra.PNG', Coordonnees=[24.684430958705356, 1.7781908602464946]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Alakazam (Pokemon):
    def __init__(self, ID ='65',nom='Alakazam', type1='Psychic', type2='null', Total=500,HP=55, Attack=50, Defense=45, Sp_Atk=135, Sp_Def=95, Speed=120, Generation='1', Legendary=False,Image='../data/Pokemon_images/Alakazam.PNG', Coordonnees=[8.674186820173624, 6.186555786487258]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Machop (Pokemon):
    def __init__(self, ID ='66',nom='Machop', type1='Fighting', type2='null', Total=305,HP=70, Attack=80, Defense=50, Sp_Atk=35, Sp_Def=35, Speed=35, Generation='1', Legendary=False,Image='../data/Pokemon_images/Machop.PNG', Coordonnees=[20.475888165694904, 9.91080995809791]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Machoke (Pokemon):
    def __init__(self, ID ='67',nom='Machoke', type1='Fighting', type2='null', Total=405,HP=80, Attack=100, Defense=70, Sp_Atk=50, Sp_Def=60, Speed=45, Generation='1', Legendary=False,Image='../data/Pokemon_images/Machoke.PNG', Coordonnees=[20.49340030132818, 1.246037158688329]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Machamp (Pokemon):
    def __init__(self, ID ='68',nom='Machamp', type1='Fighting', type2='null', Total=505,HP=90, Attack=130, Defense=80, Sp_Atk=65, Sp_Def=85, Speed=55, Generation='1', Legendary=False,Image='../data/Pokemon_images/Machamp.PNG', Coordonnees=[33.54613592535061, 5.433269538648623]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Bellsprout (Pokemon):
    def __init__(self, ID ='69',nom='Bellsprout', type1='Grass', type2='Poison', Total=300,HP=50, Attack=75, Defense=35, Sp_Atk=70, Sp_Def=30, Speed=40, Generation='1', Legendary=False,Image='../data/Pokemon_images/Bellsprout.PNG', Coordonnees=[12.583249845434906, 5.694870091585561]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Weepinbell (Pokemon):
    def __init__(self, ID ='70',nom='Weepinbell', type1='Grass', type2='Poison', Total=390,HP=65, Attack=90, Defense=50, Sp_Atk=85, Sp_Def=45, Speed=55, Generation='1', Legendary=False,Image='../data/Pokemon_images/Weepinbell.PNG', Coordonnees=[34.129045801525855, 2.798387000335115]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Victreebel (Pokemon):
    def __init__(self, ID ='71',nom='Victreebel', type1='Grass', type2='Poison', Total=490,HP=80, Attack=105, Defense=65, Sp_Atk=100, Sp_Def=70, Speed=70, Generation='1', Legendary=False,Image='../data/Pokemon_images/Victreebel.PNG', Coordonnees=[32.818808419755975, 5.206447446526607]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Tentacool (Pokemon):
    def __init__(self, ID ='72',nom='Tentacool', type1='Water', type2='Poison', Total=335,HP=40, Attack=40, Defense=35, Sp_Atk=50, Sp_Def=100, Speed=70, Generation='1', Legendary=False,Image='../data/Pokemon_images/Tentacool.PNG', Coordonnees=[31.6368690105385, 2.38216302951054]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Tentacruel (Pokemon):
    def __init__(self, ID ='73',nom='Tentacruel', type1='Water', type2='Poison', Total=515,HP=80, Attack=70, Defense=65, Sp_Atk=80, Sp_Def=120, Speed=100, Generation='1', Legendary=False,Image='../data/Pokemon_images/Tentacruel.PNG', Coordonnees=[16.988860874737192, 8.428377083635244]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Geodude (Pokemon):
    def __init__(self, ID ='74',nom='Geodude', type1='Rock', type2='Ground', Total=300,HP=40, Attack=80, Defense=100, Sp_Atk=30, Sp_Def=30, Speed=20, Generation='1', Legendary=False,Image='../data/Pokemon_images/Geodude.PNG', Coordonnees=[5.763399129762443, 0.07827641743240799]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Graveler (Pokemon):
    def __init__(self, ID ='75',nom='Graveler', type1='Rock', type2='Ground', Total=390,HP=55, Attack=95, Defense=115, Sp_Atk=45, Sp_Def=45, Speed=35, Generation='1', Legendary=False,Image='../data/Pokemon_images/Graveler.PNG', Coordonnees=[9.957655320791874, 1.7799449721465366]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Golem (Pokemon):
    def __init__(self, ID ='76',nom='Golem', type1='Rock', type2='Ground', Total=495,HP=80, Attack=120, Defense=130, Sp_Atk=55, Sp_Def=65, Speed=45, Generation='1', Legendary=False,Image='../data/Pokemon_images/Golem.PNG', Coordonnees=[22.263898456901074, 8.325049930640706]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Ponyta (Pokemon):
    def __init__(self, ID ='77',nom='Ponyta', type1='Fire', type2='null', Total=410,HP=50, Attack=85, Defense=55, Sp_Atk=65, Sp_Def=65, Speed=90, Generation='1', Legendary=False,Image='../data/Pokemon_images/Ponyta.PNG', Coordonnees=[30.780980686031647, 1.4051806103711728]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Rapidash (Pokemon):
    def __init__(self, ID ='78',nom='Rapidash', type1='Fire', type2='null', Total=500,HP=65, Attack=100, Defense=70, Sp_Atk=80, Sp_Def=80, Speed=105, Generation='1', Legendary=False,Image='../data/Pokemon_images/Rapidash.PNG', Coordonnees=[38.736859673967075, 5.234939831016802]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Slowpoke (Pokemon):
    def __init__(self, ID ='79',nom='Slowpoke', type1='Water', type2='Psychic', Total=315,HP=90, Attack=65, Defense=65, Sp_Atk=40, Sp_Def=40, Speed=15, Generation='1', Legendary=False,Image='../data/Pokemon_images/Slowpoke.PNG', Coordonnees=[17.313788005383163, 0.6975282746547329]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Slowbro (Pokemon):
    def __init__(self, ID ='80',nom='Slowbro', type1='Water', type2='Psychic', Total=490,HP=95, Attack=75, Defense=110, Sp_Atk=100, Sp_Def=80, Speed=30, Generation='1', Legendary=False,Image='../data/Pokemon_images/Slowbro.PNG', Coordonnees=[10.259068781969232, 4.848847392864469]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Magnemite (Pokemon):
    def __init__(self, ID ='81',nom='Magnemite', type1='Electric', type2='Steel', Total=325,HP=25, Attack=35, Defense=70, Sp_Atk=95, Sp_Def=55, Speed=45, Generation='1', Legendary=False,Image='../data/Pokemon_images/Magnemite.PNG', Coordonnees=[34.746299826644346, 4.493251371178143]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Magneton (Pokemon):
    def __init__(self, ID ='82',nom='Magneton', type1='Electric', type2='Steel', Total=465,HP=50, Attack=60, Defense=95, Sp_Atk=120, Sp_Def=70, Speed=70, Generation='1', Legendary=False,Image='../data/Pokemon_images/Magneton.PNG', Coordonnees=[6.732950010472218, 0.7831075943573229]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Farfetchd (Pokemon):
    def __init__(self, ID ='83',nom='Farfetchd', type1='Normal', type2='Flying', Total=352,HP=52, Attack=65, Defense=55, Sp_Atk=58, Sp_Def=62, Speed=60, Generation='1', Legendary=False,Image='../data/Pokemon_images/Farfetchd.PNG', Coordonnees=[8.645924579578477, 1.5194197850333924]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Doduo (Pokemon):
    def __init__(self, ID ='84',nom='Doduo', type1='Normal', type2='Flying', Total=310,HP=35, Attack=85, Defense=45, Sp_Atk=35, Sp_Def=35, Speed=75, Generation='1', Legendary=False,Image='../data/Pokemon_images/Doduo.PNG', Coordonnees=[27.732297979508363, 0.5870790861998576]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Dodrio (Pokemon):
    def __init__(self, ID ='85',nom='Dodrio', type1='Normal', type2='Flying', Total=460,HP=60, Attack=110, Defense=70, Sp_Atk=60, Sp_Def=60, Speed=100, Generation='1', Legendary=False,Image='../data/Pokemon_images/Dodrio.PNG', Coordonnees=[4.432161651099369, 0.774702524487425]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Seel (Pokemon):
    def __init__(self, ID ='86',nom='Seel', type1='Water', type2='null', Total=325,HP=65, Attack=45, Defense=55, Sp_Atk=45, Sp_Def=70, Speed=45, Generation='1', Legendary=False,Image='../data/Pokemon_images/Seel.PNG', Coordonnees=[31.973897985652915, 5.484843962118474]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Dewgong (Pokemon):
    def __init__(self, ID ='87',nom='Dewgong', type1='Water', type2='Ice', Total=475,HP=90, Attack=70, Defense=80, Sp_Atk=70, Sp_Def=95, Speed=70, Generation='1', Legendary=False,Image='../data/Pokemon_images/Dewgong.PNG', Coordonnees=[26.20387284272665, 4.228670179382249]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Grimer (Pokemon):
    def __init__(self, ID ='88',nom='Grimer', type1='Poison', type2='null', Total=325,HP=80, Attack=80, Defense=50, Sp_Atk=40, Sp_Def=50, Speed=25, Generation='1', Legendary=False,Image='../data/Pokemon_images/Grimer.PNG', Coordonnees=[10.08017272472356, 6.756426289467359]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Muk (Pokemon):
    def __init__(self, ID ='89',nom='Muk', type1='Poison', type2='null', Total=500,HP=105, Attack=105, Defense=75, Sp_Atk=65, Sp_Def=100, Speed=50, Generation='1', Legendary=False,Image='../data/Pokemon_images/Muk.PNG', Coordonnees=[20.508515836027303, 6.388824551466178]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Shellder (Pokemon):
    def __init__(self, ID ='90',nom='Shellder', type1='Water', type2='null', Total=305,HP=30, Attack=65, Defense=100, Sp_Atk=45, Sp_Def=25, Speed=40, Generation='1', Legendary=False,Image='../data/Pokemon_images/Shellder.PNG', Coordonnees=[11.356706526313891, 3.3576805009185904]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Cloyster (Pokemon):
    def __init__(self, ID ='91',nom='Cloyster', type1='Water', type2='Ice', Total=525,HP=50, Attack=95, Defense=180, Sp_Atk=85, Sp_Def=45, Speed=70, Generation='1', Legendary=False,Image='../data/Pokemon_images/Cloyster.PNG', Coordonnees=[1.812707283842423, 2.751786088040824]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Gastly (Pokemon):
    def __init__(self, ID ='92',nom='Gastly', type1='Ghost', type2='Poison', Total=310,HP=30, Attack=35, Defense=30, Sp_Atk=100, Sp_Def=35, Speed=80, Generation='1', Legendary=False,Image='../data/Pokemon_images/Gastly.PNG', Coordonnees=[35.38357326560688, 8.064073660981443]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Haunter (Pokemon):
    def __init__(self, ID ='93',nom='Haunter', type1='Ghost', type2='Poison', Total=405,HP=45, Attack=50, Defense=45, Sp_Atk=115, Sp_Def=55, Speed=95, Generation='1', Legendary=False,Image='../data/Pokemon_images/Haunter.PNG', Coordonnees=[17.59110376364537, 9.276865319944427]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Gengar (Pokemon):
    def __init__(self, ID ='94',nom='Gengar', type1='Ghost', type2='Poison', Total=500,HP=60, Attack=65, Defense=60, Sp_Atk=130, Sp_Def=75, Speed=110, Generation='1', Legendary=False,Image='../data/Pokemon_images/Gengar.PNG', Coordonnees=[0.32310231154787594, 5.969818987815961]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Onix (Pokemon):
    def __init__(self, ID ='95',nom='Onix', type1='Rock', type2='Ground', Total=385,HP=35, Attack=45, Defense=160, Sp_Atk=30, Sp_Def=45, Speed=70, Generation='1', Legendary=False,Image='../data/Pokemon_images/Onix.PNG', Coordonnees=[25.186762385949816, 5.04620786244375]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Drowzee (Pokemon):
    def __init__(self, ID ='96',nom='Drowzee', type1='Psychic', type2='null', Total=328,HP=60, Attack=48, Defense=45, Sp_Atk=43, Sp_Def=90, Speed=42, Generation='1', Legendary=False,Image='../data/Pokemon_images/Drowzee.PNG', Coordonnees=[15.590391412223351, 9.040247459971383]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Hypno (Pokemon):
    def __init__(self, ID ='97',nom='Hypno', type1='Psychic', type2='null', Total=483,HP=85, Attack=73, Defense=70, Sp_Atk=73, Sp_Def=115, Speed=67, Generation='1', Legendary=False,Image='../data/Pokemon_images/Hypno.PNG', Coordonnees=[8.980789530059763, 5.977470012778239]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Krabby (Pokemon):
    def __init__(self, ID ='98',nom='Krabby', type1='Water', type2='null', Total=325,HP=30, Attack=105, Defense=90, Sp_Atk=25, Sp_Def=25, Speed=50, Generation='1', Legendary=False,Image='../data/Pokemon_images/Krabby.PNG', Coordonnees=[8.272675208279384, 7.6147106173838335]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Kingler (Pokemon):
    def __init__(self, ID ='99',nom='Kingler', type1='Water', type2='null', Total=475,HP=55, Attack=130, Defense=115, Sp_Atk=50, Sp_Def=50, Speed=75, Generation='1', Legendary=False,Image='../data/Pokemon_images/Kingler.PNG', Coordonnees=[26.917474360710855, 3.1630261658856593]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Voltorb (Pokemon):
    def __init__(self, ID ='100',nom='Voltorb', type1='Electric', type2='null', Total=330,HP=40, Attack=30, Defense=50, Sp_Atk=55, Sp_Def=55, Speed=100, Generation='1', Legendary=False,Image='../data/Pokemon_images/Voltorb.PNG', Coordonnees=[21.34454228242063, 0.2716765767561735]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Electrode (Pokemon):
    def __init__(self, ID ='101',nom='Electrode', type1='Electric', type2='null', Total=480,HP=60, Attack=50, Defense=70, Sp_Atk=80, Sp_Def=80, Speed=140, Generation='1', Legendary=False,Image='../data/Pokemon_images/Electrode.PNG', Coordonnees=[34.016191518908904, 7.921182306279575]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Exeggcute (Pokemon):
    def __init__(self, ID ='102',nom='Exeggcute', type1='Grass', type2='Psychic', Total=325,HP=60, Attack=40, Defense=80, Sp_Atk=60, Sp_Def=45, Speed=40, Generation='1', Legendary=False,Image='../data/Pokemon_images/Exeggcute.PNG', Coordonnees=[30.361486724278755, 0.35811810421043533]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Exeggutor (Pokemon):
    def __init__(self, ID ='103',nom='Exeggutor', type1='Grass', type2='Psychic', Total=520,HP=95, Attack=95, Defense=85, Sp_Atk=125, Sp_Def=65, Speed=55, Generation='1', Legendary=False,Image='../data/Pokemon_images/Exeggutor.PNG', Coordonnees=[25.483871225957067, 1.2928621825026199]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Cubone (Pokemon):
    def __init__(self, ID ='104',nom='Cubone', type1='Ground', type2='null', Total=320,HP=50, Attack=50, Defense=95, Sp_Atk=40, Sp_Def=50, Speed=35, Generation='1', Legendary=False,Image='../data/Pokemon_images/Cubone.PNG', Coordonnees=[29.40257925698465, 9.907045669444493]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Marowak (Pokemon):
    def __init__(self, ID ='105',nom='Marowak', type1='Ground', type2='null', Total=425,HP=60, Attack=80, Defense=110, Sp_Atk=50, Sp_Def=80, Speed=45, Generation='1', Legendary=False,Image='../data/Pokemon_images/Marowak.PNG', Coordonnees=[0.35984404110565027, 5.8619423404574365]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Hitmonlee (Pokemon):
    def __init__(self, ID ='106',nom='Hitmonlee', type1='Fighting', type2='null', Total=455,HP=50, Attack=120, Defense=53, Sp_Atk=35, Sp_Def=110, Speed=87, Generation='1', Legendary=False,Image='../data/Pokemon_images/Hitmonlee.PNG', Coordonnees=[5.226345484986132, 6.156254037942206]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Hitmonchan (Pokemon):
    def __init__(self, ID ='107',nom='Hitmonchan', type1='Fighting', type2='null', Total=455,HP=50, Attack=105, Defense=79, Sp_Atk=35, Sp_Def=110, Speed=76, Generation='1', Legendary=False,Image='../data/Pokemon_images/Hitmonchan.PNG', Coordonnees=[25.429567860061454, 9.196848609746311]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Lickitung (Pokemon):
    def __init__(self, ID ='108',nom='Lickitung', type1='Normal', type2='null', Total=385,HP=90, Attack=55, Defense=75, Sp_Atk=60, Sp_Def=75, Speed=30, Generation='1', Legendary=False,Image='../data/Pokemon_images/Lickitung.PNG', Coordonnees=[25.94738223729371, 6.844958759104486]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Koffing (Pokemon):
    def __init__(self, ID ='109',nom='Koffing', type1='Poison', type2='null', Total=340,HP=40, Attack=65, Defense=95, Sp_Atk=60, Sp_Def=45, Speed=35, Generation='1', Legendary=False,Image='../data/Pokemon_images/Koffing.PNG', Coordonnees=[1.138031517478293, 4.788449000779057]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Weezing (Pokemon):
    def __init__(self, ID ='110',nom='Weezing', type1='Poison', type2='null', Total=490,HP=65, Attack=90, Defense=120, Sp_Atk=85, Sp_Def=70, Speed=60, Generation='1', Legendary=False,Image='../data/Pokemon_images/Weezing.PNG', Coordonnees=[37.822736590251374, 5.280428604189095]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Rhyhorn (Pokemon):
    def __init__(self, ID ='111',nom='Rhyhorn', type1='Ground', type2='Rock', Total=345,HP=80, Attack=85, Defense=95, Sp_Atk=30, Sp_Def=30, Speed=25, Generation='1', Legendary=False,Image='../data/Pokemon_images/Rhyhorn.PNG', Coordonnees=[2.2599681440582975, 5.0165152097739165]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Rhydon (Pokemon):
    def __init__(self, ID ='112',nom='Rhydon', type1='Ground', type2='Rock', Total=485,HP=105, Attack=130, Defense=120, Sp_Atk=45, Sp_Def=45, Speed=40, Generation='1', Legendary=False,Image='../data/Pokemon_images/Rhydon.PNG', Coordonnees=[24.950080396068092, 9.136818645232013]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Chansey (Pokemon):
    def __init__(self, ID ='113',nom='Chansey', type1='Normal', type2='null', Total=450,HP=250, Attack=5, Defense=5, Sp_Atk=35, Sp_Def=105, Speed=50, Generation='1', Legendary=False,Image='../data/Pokemon_images/Chansey.PNG', Coordonnees=[11.363339748090372, 1.3073823629664683]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Tangela (Pokemon):
    def __init__(self, ID ='114',nom='Tangela', type1='Grass', type2='null', Total=435,HP=65, Attack=55, Defense=115, Sp_Atk=100, Sp_Def=40, Speed=60, Generation='1', Legendary=False,Image='../data/Pokemon_images/Tangela.PNG', Coordonnees=[22.763216136880718, 0.5816475753381745]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Kangaskhan (Pokemon):
    def __init__(self, ID ='115',nom='Kangaskhan', type1='Normal', type2='null', Total=490,HP=105, Attack=95, Defense=80, Sp_Atk=40, Sp_Def=80, Speed=90, Generation='1', Legendary=False,Image='../data/Pokemon_images/Kangaskhan.PNG', Coordonnees=[26.336047733221875, 1.4597120085232262]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Horsea (Pokemon):
    def __init__(self, ID ='116',nom='Horsea', type1='Water', type2='null', Total=295,HP=30, Attack=40, Defense=70, Sp_Atk=70, Sp_Def=25, Speed=60, Generation='1', Legendary=False,Image='../data/Pokemon_images/Horsea.PNG', Coordonnees=[6.4584154327647525, 8.55877201171029]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Seadra (Pokemon):
    def __init__(self, ID ='117',nom='Seadra', type1='Water', type2='null', Total=440,HP=55, Attack=65, Defense=95, Sp_Atk=95, Sp_Def=45, Speed=85, Generation='1', Legendary=False,Image='../data/Pokemon_images/Seadra.PNG', Coordonnees=[10.757671739452363, 6.935780593360695]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Goldeen (Pokemon):
    def __init__(self, ID ='118',nom='Goldeen', type1='Water', type2='null', Total=320,HP=45, Attack=67, Defense=60, Sp_Atk=35, Sp_Def=50, Speed=63, Generation='1', Legendary=False,Image='../data/Pokemon_images/Goldeen.PNG', Coordonnees=[32.58347161448271, 8.98601337229347]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Seaking (Pokemon):
    def __init__(self, ID ='119',nom='Seaking', type1='Water', type2='null', Total=450,HP=80, Attack=92, Defense=65, Sp_Atk=65, Sp_Def=80, Speed=68, Generation='1', Legendary=False,Image='../data/Pokemon_images/Seaking.PNG', Coordonnees=[0.6866283139286722, 0.891467016709403]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Staryu (Pokemon):
    def __init__(self, ID ='120',nom='Staryu', type1='Water', type2='null', Total=340,HP=30, Attack=45, Defense=55, Sp_Atk=70, Sp_Def=55, Speed=85, Generation='1', Legendary=False,Image='../data/Pokemon_images/Staryu.PNG', Coordonnees=[23.16598957832367, 5.391677590978713]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Starmie (Pokemon):
    def __init__(self, ID ='121',nom='Starmie', type1='Water', type2='Psychic', Total=520,HP=60, Attack=75, Defense=85, Sp_Atk=100, Sp_Def=85, Speed=115, Generation='1', Legendary=False,Image='../data/Pokemon_images/Starmie.PNG', Coordonnees=[32.024340524779745, 1.9592907458932163]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Mr_Mime (Pokemon):
    def __init__(self, ID ='122',nom='Mr_Mime', type1='Psychic', type2='Fairy', Total=460,HP=40, Attack=45, Defense=65, Sp_Atk=100, Sp_Def=120, Speed=90, Generation='1', Legendary=False,Image='../data/Pokemon_images/Mr_Mime.PNG', Coordonnees=[31.343599031300467, 2.0451965379226236]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Scyther (Pokemon):
    def __init__(self, ID ='123',nom='Scyther', type1='Bug', type2='Flying', Total=500,HP=70, Attack=110, Defense=80, Sp_Atk=55, Sp_Def=80, Speed=105, Generation='1', Legendary=False,Image='../data/Pokemon_images/Scyther.PNG', Coordonnees=[0.37643904084805335, 1.7229072567102366]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Jynx (Pokemon):
    def __init__(self, ID ='124',nom='Jynx', type1='Ice', type2='Psychic', Total=455,HP=65, Attack=50, Defense=35, Sp_Atk=115, Sp_Def=95, Speed=95, Generation='1', Legendary=False,Image='../data/Pokemon_images/Jynx.PNG', Coordonnees=[39.959151788451024, 2.141117145583703]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Electabuzz (Pokemon):
    def __init__(self, ID ='125',nom='Electabuzz', type1='Electric', type2='null', Total=490,HP=65, Attack=83, Defense=57, Sp_Atk=95, Sp_Def=85, Speed=105, Generation='1', Legendary=False,Image='../data/Pokemon_images/Electabuzz.PNG', Coordonnees=[1.6701894808154805, 8.752556688776673]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Magmar (Pokemon):
    def __init__(self, ID ='126',nom='Magmar', type1='Fire', type2='null', Total=495,HP=65, Attack=95, Defense=57, Sp_Atk=100, Sp_Def=85, Speed=93, Generation='1', Legendary=False,Image='../data/Pokemon_images/Magmar.PNG', Coordonnees=[25.43694616602974, 8.66287871104866]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Pinsir (Pokemon):
    def __init__(self, ID ='127',nom='Pinsir', type1='Bug', type2='null', Total=500,HP=65, Attack=125, Defense=100, Sp_Atk=55, Sp_Def=70, Speed=85, Generation='1', Legendary=False,Image='../data/Pokemon_images/Pinsir.PNG', Coordonnees=[4.787685079099844, 7.2382842411877935]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Tauros (Pokemon):
    def __init__(self, ID ='128',nom='Tauros', type1='Normal', type2='null', Total=490,HP=75, Attack=100, Defense=95, Sp_Atk=40, Sp_Def=70, Speed=110, Generation='1', Legendary=False,Image='../data/Pokemon_images/Tauros.PNG', Coordonnees=[35.90711800752034, 6.241716153641189]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Magikarp (Pokemon):
    def __init__(self, ID ='129',nom='Magikarp', type1='Water', type2='null', Total=200,HP=20, Attack=10, Defense=55, Sp_Atk=15, Sp_Def=20, Speed=80, Generation='1', Legendary=False,Image='../data/Pokemon_images/Magikarp.PNG', Coordonnees=[18.538550585681225, 9.881911887906282]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Gyarados (Pokemon):
    def __init__(self, ID ='130',nom='Gyarados', type1='Water', type2='Flying', Total=540,HP=95, Attack=125, Defense=79, Sp_Atk=60, Sp_Def=100, Speed=81, Generation='1', Legendary=False,Image='../data/Pokemon_images/Gyarados.PNG', Coordonnees=[3.6498555093793517, 5.948141157124798]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Lapras (Pokemon):
    def __init__(self, ID ='131',nom='Lapras', type1='Water', type2='Ice', Total=535,HP=130, Attack=85, Defense=80, Sp_Atk=85, Sp_Def=95, Speed=60, Generation='1', Legendary=False,Image='../data/Pokemon_images/Lapras.PNG', Coordonnees=[27.76021400873266, 1.27309415151164]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Ditto (Pokemon):
    def __init__(self, ID ='132',nom='Ditto', type1='Normal', type2='null', Total=288,HP=48, Attack=48, Defense=48, Sp_Atk=48, Sp_Def=48, Speed=48, Generation='1', Legendary=False,Image='../data/Pokemon_images/Ditto.PNG', Coordonnees=[31.905301517456554, 7.881894067343965]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Eevee (Pokemon):
    def __init__(self, ID ='133',nom='Eevee', type1='Normal', type2='null', Total=325,HP=55, Attack=55, Defense=50, Sp_Atk=45, Sp_Def=65, Speed=55, Generation='1', Legendary=False,Image='../data/Pokemon_images/Eevee.PNG', Coordonnees=[6.662468619644337, 5.64268167282325]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Vaporeon (Pokemon):
    def __init__(self, ID ='134',nom='Vaporeon', type1='Water', type2='null', Total=525,HP=130, Attack=65, Defense=60, Sp_Atk=110, Sp_Def=95, Speed=65, Generation='1', Legendary=False,Image='../data/Pokemon_images/Vaporeon.PNG', Coordonnees=[37.65011164061983, 7.853948221593856]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Jolteon (Pokemon):
    def __init__(self, ID ='135',nom='Jolteon', type1='Electric', type2='null', Total=525,HP=65, Attack=65, Defense=60, Sp_Atk=110, Sp_Def=95, Speed=130, Generation='1', Legendary=False,Image='../data/Pokemon_images/Jolteon.PNG', Coordonnees=[2.698446413975457, 0.04812852150032021]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Flareon (Pokemon):
    def __init__(self, ID ='136',nom='Flareon', type1='Fire', type2='null', Total=525,HP=65, Attack=130, Defense=60, Sp_Atk=95, Sp_Def=110, Speed=65, Generation='1', Legendary=False,Image='../data/Pokemon_images/Flareon.PNG', Coordonnees=[4.15453694627411, 5.819244697610185]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Porygon (Pokemon):
    def __init__(self, ID ='137',nom='Porygon', type1='Normal', type2='null', Total=395,HP=65, Attack=60, Defense=70, Sp_Atk=85, Sp_Def=75, Speed=40, Generation='1', Legendary=False,Image='../data/Pokemon_images/Porygon.PNG', Coordonnees=[6.184260034193216, 8.55360093868772]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Omanyte (Pokemon):
    def __init__(self, ID ='138',nom='Omanyte', type1='Rock', type2='Water', Total=355,HP=35, Attack=40, Defense=100, Sp_Atk=90, Sp_Def=55, Speed=35, Generation='1', Legendary=False,Image='../data/Pokemon_images/Omanyte.PNG', Coordonnees=[6.053868298494498, 5.999575908015645]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Omastar (Pokemon):
    def __init__(self, ID ='139',nom='Omastar', type1='Rock', type2='Water', Total=495,HP=70, Attack=60, Defense=125, Sp_Atk=115, Sp_Def=70, Speed=55, Generation='1', Legendary=False,Image='../data/Pokemon_images/Omastar.PNG', Coordonnees=[34.59977746697469, 9.457286153521828]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Kabuto (Pokemon):
    def __init__(self, ID ='140',nom='Kabuto', type1='Rock', type2='Water', Total=355,HP=30, Attack=80, Defense=90, Sp_Atk=55, Sp_Def=45, Speed=55, Generation='1', Legendary=False,Image='../data/Pokemon_images/Kabuto.PNG', Coordonnees=[8.694706051455112, 5.278580573388246]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Kabutops (Pokemon):
    def __init__(self, ID ='141',nom='Kabutops', type1='Rock', type2='Water', Total=495,HP=60, Attack=115, Defense=105, Sp_Atk=65, Sp_Def=70, Speed=80, Generation='1', Legendary=False,Image='../data/Pokemon_images/Kabutops.PNG', Coordonnees=[30.88886156012109, 8.522410369327613]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Aerodactyl (Pokemon):
    def __init__(self, ID ='142',nom='Aerodactyl', type1='Rock', type2='Flying', Total=515,HP=80, Attack=105, Defense=65, Sp_Atk=60, Sp_Def=75, Speed=130, Generation='1', Legendary=False,Image='../data/Pokemon_images/Aerodactyl.PNG', Coordonnees=[19.868549768587943, 8.155710621931844]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Snorlax (Pokemon):
    def __init__(self, ID ='143',nom='Snorlax', type1='Normal', type2='null', Total=540,HP=160, Attack=110, Defense=65, Sp_Atk=65, Sp_Def=110, Speed=30, Generation='1', Legendary=False,Image='../data/Pokemon_images/Snorlax.PNG', Coordonnees=[16.221013085792034, 1.5189970381060958]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Articuno (Pokemon):
    def __init__(self, ID ='144',nom='Articuno', type1='Ice', type2='Flying', Total=580,HP=90, Attack=85, Defense=100, Sp_Atk=95, Sp_Def=125, Speed=85, Generation='1', Legendary=True,Image='../data/Pokemon_images/Articuno.PNG', Coordonnees=[4.3031467064433615, 6.745773774780339]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Zapdos (Pokemon):
    def __init__(self, ID ='145',nom='Zapdos', type1='Electric', type2='Flying', Total=580,HP=90, Attack=90, Defense=85, Sp_Atk=125, Sp_Def=90, Speed=100, Generation='1', Legendary=True,Image='../data/Pokemon_images/Zapdos.PNG', Coordonnees=[6.0907670355848875, 0.1301166889211791]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Moltres (Pokemon):
    def __init__(self, ID ='146',nom='Moltres', type1='Fire', type2='Flying', Total=580,HP=90, Attack=100, Defense=90, Sp_Atk=125, Sp_Def=85, Speed=90, Generation='1', Legendary=True,Image='../data/Pokemon_images/Moltres.PNG', Coordonnees=[7.263334513550195, 4.207299807446344]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Dratini (Pokemon):
    def __init__(self, ID ='147',nom='Dratini', type1='Dragon', type2='null', Total=300,HP=41, Attack=64, Defense=45, Sp_Atk=50, Sp_Def=50, Speed=50, Generation='1', Legendary=False,Image='../data/Pokemon_images/Dratini.PNG', Coordonnees=[35.426160157144196, 7.509966362336878]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Dragonair (Pokemon):
    def __init__(self, ID ='148',nom='Dragonair', type1='Dragon', type2='null', Total=420,HP=61, Attack=84, Defense=65, Sp_Atk=70, Sp_Def=70, Speed=70, Generation='1', Legendary=False,Image='../data/Pokemon_images/Dragonair.PNG', Coordonnees=[14.082682553226938, 8.329930683582488]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Dragonite (Pokemon):
    def __init__(self, ID ='149',nom='Dragonite', type1='Dragon', type2='Flying', Total=600,HP=91, Attack=134, Defense=95, Sp_Atk=100, Sp_Def=100, Speed=80, Generation='1', Legendary=False,Image='../data/Pokemon_images/Dragonite.PNG', Coordonnees=[0.06328498514706293, 1.6189169866591158]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Mewtwo (Pokemon):
    def __init__(self, ID ='150',nom='Mewtwo', type1='Psychic', type2='null', Total=680,HP=106, Attack=110, Defense=90, Sp_Atk=154, Sp_Def=90, Speed=130, Generation='1', Legendary=True,Image='../data/Pokemon_images/Mewtwo.PNG', Coordonnees=[6.974622282327214, 2.312707264725665]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

class Mew (Pokemon):
    def __init__(self, ID ='151',nom='Mew', type1='Psychic', type2='null', Total=600,HP=100, Attack=100, Defense=100, Sp_Atk=100, Sp_Def=100, Speed=100, Generation='1', Legendary=False,Image='../data/Pokemon_images/Mew.PNG', Coordonnees=[23.864233784028617, 5.207541521755]):
        super().__init__( ID, nom, type1, type2, Total, HP, Attack, Defense , Sp_Atk , Sp_Def , Speed , Generation , Legendary, Image, Coordonnees )

##############################################################

       ########## Classe Dresseur ###########

############################################################## 

class Dresseur():
    Pokemons_depart=3
    
    #Constructeur
    def __init__(self, nom):
        
        self.nom=nom
        self.inventaire={}
        self.pokemons_attrappes=[]
        self.ID_pokemons_attrappees=[]
        self.pokemons_a_trouver=list_pokemons.copy()
        
        for i in range(Dresseur.Pokemons_depart):
            nom_pokemon=rd.choice(list_pokemons)
            Choix=dict_pokemons[nom_pokemon]
            
            self.inventaire[nom_pokemon]=Choix
            self.pokemons_attrappes.append(nom_pokemon+" ("+Choix.ID+")")
            self.ID_pokemons_attrappees.append(Choix.ID)
            self.pokemons_a_trouver.remove(nom_pokemon)
            if Choix.ID in pokemons_13totals_croissants:
                pokemons_13totals_croissants.remove(str(Choix.ID))
        
 
##############################################################

            ########## Methodes ###########

##############################################################
             
    def choix_pokemons_combattants(self):
        """
        Fonction qui renvoie les troix pokemons que le joueur utilisera
        en combat avec leurs noms et leurs identifiants

        """
        self.pokemons_combats={}
        self.nom_pokemons_combattants=[]
        self.ID_pokemons_combats=[]
        if len(self)==3:
            self.pokemons_combats=self.inventaire.copy()
            self.nom_pokemons_combattants=self.pokemons_attrappes.copy()
            self.ID_pokemons_combats=self.ID_pokemons_attrappees
        else:
            possibilites=self.pokemons_attrappes.copy()
            ID_possibilites=self.ID_pokemons_attrappees.copy()
            for choix in range(Dresseur.Pokemons_depart):
                
                nom,pokemon,ID_nom= choix_pokemon(possibilites, ID_possibilites)
                self.pokemons_combats[nom]= pokemon
                self.nom_pokemons_combattants.append(pokemon)
                self.ID_pokemons_combats.append(ID_nom)
                possibilites.remove(nom+" ("+ID_nom+")")
                
        self.pokemon_zone_attente=self.pokemons_combats.copy()
                

    def vitesse(self,pokemon):
        """
        Fonction qui renvoie le nom du pokemon qui commence le combat
        entre le pokemon choisi par le joueur et un pokemon a trouver

        Parameters
        ----------
        pokemon : Sous-classe pokemon
            Pokemon rencontre.

        Returns
        -------
        Choix.nom / Pokemon.nom    :  String
            Nom du pokemon attaquant.

        """
        self.pokemon_zone_combat={}
        pokemon_nom,choix,ID_nom= choix_pokemon(self.nom_pokemons_combattants,self.ID_pokemons_combats)
        
        self.pokemon_zone_combat[pokemon_nom]=choix
        del self.pokemon_zone_attente[pokemon_nom]
        if choix.Speed >= pokemon.Speed:
            return choix.nom
        else:
            return pokemon.nom
        
    def echange_pokemon(self):
        choix_pokemon(self., liste2)
        
        
        return 0
    
    def fuir(): 
        return 0
        
    def tour():
        return 0
    
    
    def ajout_pokemon_sauvages(self):
        nom_pokemon=rd.choice(self.pokemons_a_trouver)[-5]
        self.pokemons_sauvages.append(nom_pokemon)
        
        
    def attrape_pokemon(self,pokemon):
        """
        Fonction qui ajoute un pokemon battu a l'inventaire du pokemon
        et le retiredes pokemons a trouver

        Parameters
        ----------
        pokemon : Sous-classe pokemon
            Pokemon vaincu.

        """
        self.inventaire[pokemon.nom]=pokemon
        self.pokemons_attrappes.append(pokemon.nom+" ("+pokemon.ID+")")
        self.ID_pokemons_attrappees.append(pokemon.ID)
        self.pokemons_a_trouver.remove(pokemon.nom)
        if pokemon in self.pokemons_libres:
            self.pokemons_libres.remove(pokemon)
        if pokemon in self.pokemons_sauvages:
            self.pokemons_sauvages.remove(pokemon)
        
        
    def pokemons_on_map(self):
        """
        Fonctions qui repartie les pokemons a trouver
        en pokemons sauvages et libres

        """
        p_l=10  # Nombre de pokemons libres
        p_s=20  # Nombre de pokemons sauvages
        
        self.pokemons_libres=[] # Liste de pokemons libres
        self.pokemons_sauvages=[] # Liste de pokemons sauvages
        for numero in range(p_s+p_l):
            
            # Recupere les dix pokemons a trouver aux plus hauts totaux
            if numero <p_l:
                nom = ID_pokemons[pokemons_13totals_croissants[0]]
                ID_nom=pokemons_13totals_croissants[0]
                self.pokemons_libres.append(nom)
                self.pokemons_a_trouver.remove(nom)
                pokemons_13totals_croissants.remove(ID_nom)
                
            else:
                
                # Recupere les 20 pokemons a trouver comme pokemons sauvages
                nom=rd.choice(self.pokemons_a_trouver)[-5]
                self.pokemons_sauvages.append(nom)
                ID_nom=dict_pokemons[nom].ID
                self.pokemons_a_trouver.remove(nom)
                                
##############################################################

             ########## Surcharge ###########

##############################################################
    
    # Surcharge len()
    def __len__(self):
        return len(self.inventaire)
    
    # Surcharge X[nom]=valeur
    def __getitem__(self,nom):
        for pokemon in self.inventaire:
            if (pokemon.__name__)== nom :
                return pokemon       
            
    # Surcharge in      
    def __contains__(self, nom):
        if nom in list_pokemons:
            return True
        
    # Surcharge del
    def __delitem__(conteneur,nom):
        for pokemon in conteneur:
            if pokemon.name == nom:
                del conteneur[pokemon.name]
                
    # Surcharge print()
    def __str__(self):
        txt=("- - - - - - - - - - - - - - - - - - - - - - - - - - - - \nNom : "
             +str(self.nom) +"\nNombre de pokemons : "+str(len(self))
             +"\nPokemons combattants : "+str(list(self.pokemons_combats.keys())).replace("'","").replace("[","").replace("]","")
             + "\nPokemons capturés : "+str(self.pokemons_attrappes).replace("'","").replace("[","").replace("]","") + "\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
        return txt

        

    
    
# class  Jeu():
#     def __ini

def jeu():
    Joueur= Dresseur(input("Veillez entrer votre Pseudo"))
    while len(Joueur)!=151:
        if len(Joueur)==151:
            print("Félicitation vous avez achevé votre aventure")
        
if __name__=='__main__':

##############################################################

           ########## Donnees utiles ###########

##############################################################                

    dict_pokemons={ 'Bulbasaur' : Bulbasaur(), 'Ivysaur' : Ivysaur(), 'Venusaur' : Venusaur(), 'Charmander' : Charmander(), 'Charmeleon' : Charmeleon(), 'Charizard' : Charizard(), 'Squirtle' : Squirtle(), 'Wartortle' : Wartortle(), 'Blastoise' : Blastoise(), 'Caterpie' : Caterpie(), 'Metapod' : Metapod(), 'Butterfree' : Butterfree(), 'Weedle' : Weedle(), 'Kakuna' : Kakuna(), 'Beedrill' : Beedrill(), 'Pidgey' : Pidgey(), 'Pidgeotto' : Pidgeotto(), 'Pidgeot' : Pidgeot(), 'Rattata' : Rattata(), 'Raticate' : Raticate(), 'Spearow' : Spearow(), 'Fearow' : Fearow(), 'Ekans' : Ekans(), 'Arbok' : Arbok(), 'Pikachu' : Pikachu(), 'Raichu' : Raichu(), 'Sandshrew' : Sandshrew(), 'Sandslash' : Sandslash(), 'Nidoran_male' : Nidoran_male(), 'Nidorina' : Nidorina(), 'Nidoqueen' : Nidoqueen(), 'Nidoran_female' : Nidoran_female(), 'Nidorino' : Nidorino(), 'Nidoking' : Nidoking(), 'Clefairy' : Clefairy(), 'Clefable' : Clefable(), 'Vulpix' : Vulpix(), 'Ninetales' : Ninetales(), 'Jigglypuff' : Jigglypuff(), 'Wigglytuff' : Wigglytuff(), 'Zubat' : Zubat(), 'Golbat' : Golbat(), 'Oddish' : Oddish(), 'Gloom' : Gloom(), 'Vileplume' : Vileplume(), 'Paras' : Paras(), 'Parasect' : Parasect(), 'Venonat' : Venonat(), 'Venomoth' : Venomoth(), 'Diglett' : Diglett(), 'Dugtrio' : Dugtrio(), 'Meowth' : Meowth(), 'Persian' : Persian(), 'Psyduck' : Psyduck(), 'Golduck' : Golduck(), 'Mankey' : Mankey(), 'Primeape' : Primeape(), 'Growlithe' : Growlithe(), 'Arcanine' : Arcanine(), 'Poliwag' : Poliwag(), 'Poliwhirl' : Poliwhirl(), 'Poliwrath' : Poliwrath(), 'Abra' : Abra(), 'Kadabra' : Kadabra(), 'Alakazam' : Alakazam(), 'Machop' : Machop(), 'Machoke' : Machoke(), 'Machamp' : Machamp(), 'Bellsprout' : Bellsprout(), 'Weepinbell' : Weepinbell(), 'Victreebel' : Victreebel(), 'Tentacool' : Tentacool(), 'Tentacruel' : Tentacruel(), 'Geodude' : Geodude(), 'Graveler' : Graveler(), 'Golem' : Golem(), 'Ponyta' : Ponyta(), 'Rapidash' : Rapidash(), 'Slowpoke' : Slowpoke(), 'Slowbro' : Slowbro(), 'Magnemite' : Magnemite(), 'Magneton' : Magneton(), 'Farfetchd' : Farfetchd(), 'Doduo' : Doduo(), 'Dodrio' : Dodrio(), 'Seel' : Seel(), 'Dewgong' : Dewgong(), 'Grimer' : Grimer(), 'Muk' : Muk(), 'Shellder' : Shellder(), 'Cloyster' : Cloyster(), 'Gastly' : Gastly(), 'Haunter' : Haunter(), 'Gengar' : Gengar(), 'Onix' : Onix(), 'Drowzee' : Drowzee(), 'Hypno' : Hypno(), 'Krabby' : Krabby(), 'Kingler' : Kingler(), 'Voltorb' : Voltorb(), 'Electrode' : Electrode(), 'Exeggcute' : Exeggcute(), 'Exeggutor' : Exeggutor(), 'Cubone' : Cubone(), 'Marowak' : Marowak(), 'Hitmonlee' : Hitmonlee(), 'Hitmonchan' : Hitmonchan(), 'Lickitung' : Lickitung(), 'Koffing' : Koffing(), 'Weezing' : Weezing(), 'Rhyhorn' : Rhyhorn(), 'Rhydon' : Rhydon(), 'Chansey' : Chansey(), 'Tangela' : Tangela(), 'Kangaskhan' : Kangaskhan(), 'Horsea' : Horsea(), 'Seadra' : Seadra(), 'Goldeen' : Goldeen(), 'Seaking' : Seaking(), 'Staryu' : Staryu(), 'Starmie' : Starmie(), 'Mr_Mime' : Mr_Mime(), 'Scyther' : Scyther(), 'Jynx' : Jynx(), 'Electabuzz' : Electabuzz(), 'Magmar' : Magmar(), 'Pinsir' : Pinsir(), 'Tauros' : Tauros(), 'Magikarp' : Magikarp(), 'Gyarados' : Gyarados(), 'Lapras' : Lapras(), 'Ditto' : Ditto(), 'Eevee' : Eevee(), 'Vaporeon' : Vaporeon(), 'Jolteon' : Jolteon(), 'Flareon' : Flareon(), 'Porygon' : Porygon(), 'Omanyte' : Omanyte(), 'Omastar' : Omastar(), 'Kabuto' : Kabuto(), 'Kabutops' : Kabutops(), 'Aerodactyl' : Aerodactyl(), 'Snorlax' : Snorlax(), 'Articuno' : Articuno(), 'Zapdos' : Zapdos(), 'Moltres' : Moltres(), 'Dratini' : Dratini(), 'Dragonair' : Dragonair(), 'Dragonite' : Dragonite(), 'Mewtwo' : Mewtwo(), 'Mew' : Mew(), }

    list_pokemons= list(dict_pokemons.keys()) 

    ID_pokemons= { '1' : 'Bulbasaur', '2' : 'Ivysaur', '3' : 'Venusaur', '4' : 'Charmander', '5' : 'Charmeleon', '6' : 'Charizard', '7' : 'Squirtle', '8' : 'Wartortle', '9' : 'Blastoise', '10' : 'Caterpie', '11' : 'Metapod', '12' : 'Butterfree', '13' : 'Weedle', '14' : 'Kakuna', '15' : 'Beedrill', '16' : 'Pidgey', '17' : 'Pidgeotto', '18' : 'Pidgeot', '19' : 'Rattata', '20' : 'Raticate', '21' : 'Spearow', '22' : 'Fearow', '23' : 'Ekans', '24' : 'Arbok', '25' : 'Pikachu', '26' : 'Raichu', '27' : 'Sandshrew', '28' : 'Sandslash', '29' : 'Nidoran_male', '30' : 'Nidorina', '31' : 'Nidoqueen', '32' : 'Nidoran_female', '33' : 'Nidorino', '34' : 'Nidoking', '35' : 'Clefairy', '36' : 'Clefable', '37' : 'Vulpix', '38' : 'Ninetales', '39' : 'Jigglypuff', '40' : 'Wigglytuff', '41' : 'Zubat', '42' : 'Golbat', '43' : 'Oddish', '44' : 'Gloom', '45' : 'Vileplume', '46' : 'Paras', '47' : 'Parasect', '48' : 'Venonat', '49' : 'Venomoth', '50' : 'Diglett', '51' : 'Dugtrio', '52' : 'Meowth', '53' : 'Persian', '54' : 'Psyduck', '55' : 'Golduck', '56' : 'Mankey', '57' : 'Primeape', '58' : 'Growlithe', '59' : 'Arcanine', '60' : 'Poliwag', '61' : 'Poliwhirl', '62' : 'Poliwrath', '63' : 'Abra', '64' : 'Kadabra', '65' : 'Alakazam', '66' : 'Machop', '67' : 'Machoke', '68' : 'Machamp', '69' : 'Bellsprout', '70' : 'Weepinbell', '71' : 'Victreebel', '72' : 'Tentacool', '73' : 'Tentacruel', '74' : 'Geodude', '75' : 'Graveler', '76' : 'Golem', '77' : 'Ponyta', '78' : 'Rapidash', '79' : 'Slowpoke', '80' : 'Slowbro', '81' : 'Magnemite', '82' : 'Magneton', '83' : 'Farfetchd', '84' : 'Doduo', '85' : 'Dodrio', '86' : 'Seel', '87' : 'Dewgong', '88' : 'Grimer', '89' : 'Muk', '90' : 'Shellder', '91' : 'Cloyster', '92' : 'Gastly', '93' : 'Haunter', '94' : 'Gengar', '95' : 'Onix', '96' : 'Drowzee', '97' : 'Hypno', '98' : 'Krabby', '99' : 'Kingler', '100' : 'Voltorb', '101' : 'Electrode', '102' : 'Exeggcute', '103' : 'Exeggutor', '104' : 'Cubone', '105' : 'Marowak', '106' : 'Hitmonlee', '107' : 'Hitmonchan', '108' : 'Lickitung', '109' : 'Koffing', '110' : 'Weezing', '111' : 'Rhyhorn', '112' : 'Rhydon', '113' : 'Chansey', '114' : 'Tangela', '115' : 'Kangaskhan', '116' : 'Horsea', '117' : 'Seadra', '118' : 'Goldeen', '119' : 'Seaking', '120' : 'Staryu', '121' : 'Starmie', '122' : 'Mr_Mime', '123' : 'Scyther', '124' : 'Jynx', '125' : 'Electabuzz', '126' : 'Magmar', '127' : 'Pinsir', '128' : 'Tauros', '129' : 'Magikarp', '130' : 'Gyarados', '131' : 'Lapras', '132' : 'Ditto', '133' : 'Eevee', '134' : 'Vaporeon', '135' : 'Jolteon', '136' : 'Flareon', '137' : 'Porygon', '138' : 'Omanyte', '139' : 'Omastar', '140' : 'Kabuto', '141' : 'Kabutops', '142' : 'Aerodactyl', '143' : 'Snorlax', '144' : 'Articuno', '145' : 'Zapdos', '146' : 'Moltres', '147' : 'Dratini', '148' : 'Dragonair', '149' : 'Dragonite', '150' : 'Mewtwo', '151' : 'Mew', }

    pokemons_13totals_croissants=['150', '149', '151', '144', '145', '146', '59', '130', '143', '131', '6', '9', '3']
    
    def choix_pokemon(liste1,liste2):
        """
        
        Fonction qui permet de choisir un pokemon en choisissant son identifiant
        
        Parameters
        ----------
        liste1 : list
            Liste de noms de pokemon avec leur identifiants entre parentheses.
        liste2 : list
            Liste d'identifiants de pokemon.

        Returns
        -------
        nom : string
            DESCRIPTION.
        pokemon : sous-classe de pokemon
            Pokemon selectionne.
        ID_nom : string
            Identifiant du pokemon selectionne.

        """
        possibilites= liste1.copy()
        selection= str(input("Choississez l'identifiant du pokemon : " +str(possibilites).replace("'","").replace("[","").replace("]","")+"\n➡️ "))
        while selection not in liste2:
            print("Le choix n'est pas valide")
            selection =str(input("Choississez l'identifiant du pokemon : " +str(possibilites).replace("'","").replace("[","").replace("]","")+"\n➡️ "))
        nom=ID_pokemons[selection]
        pokemon=dict_pokemons[nom]
        ID_nom=selection
        return nom,pokemon,ID_nom
    
##############################################################

               ########## Test ###########

##############################################################                

    pi=Pikachu()
    Mewtou=Mew()
    Drac=Drowzee()
    o=Pokemon.Affinites.copy()
    
    # print(Mewtou.attaque_neutre(pi))
    
    Drac=Drowzee()
    pika=dict_pokemons["Pikachu"]
    
    # print(Pokemon.Affinites[Pokemon.Types[pika.type1],Pokemon.Types[pika.type1]])
    
    
    
    Sacha = Dresseur("Sacha")
    
    # Sacha.attrape_pokemon(pika)
    Sacha.choix_pokemons_combattants()
    # print(Sacha.get_nom_pokemon(25))
    # print(Sacha.vitesse(Drac))
    print(Sacha)
    
    # Sacha.pokemons_on_map()
    # <>