# -*- coding: utf-8 -*-
"""
Created on Wed May 15 14:33:17 2024

@author: Hp Probook i7
"""

# Import des interfaces
from Ensemble_Interfaces import *

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