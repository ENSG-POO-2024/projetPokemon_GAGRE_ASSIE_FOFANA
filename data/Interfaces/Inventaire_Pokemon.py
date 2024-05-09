from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_Inventaire_Pokemon(object):
    def setupUi(self):
        self.setWindowTitle("Liste des Pokemons")
        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QtWidgets.QVBoxLayout(self.central_widget)
        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.setRowCount(9)
        self.tableWidget.setColumnCount(17)
        self.setFixedSize(1809,959)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        folder_path = "../Images/Pokemon_images"  # Recupérer l'inventaire du joueur
        pokemons = []
        for filename in os.listdir(folder_path):
            if filename.endswith(".png"):
                file_path = os.path.join(folder_path, filename)
                pokemons.append(file_path)
        for i in range(len(pokemons)):  # Remplir l'inventaire du joueur
            row = i // 17
            col = i % 17
            widget = QtWidgets.QWidget()  # Créer un widget pour contenir l'image et le nom
            layout = QtWidgets.QVBoxLayout(widget)
            image_label = QtWidgets.QLabel()   # Ajouter l'image
            image_label.setPixmap(QtGui.QPixmap(pokemons[i]).scaled(50, 50))  # Redimensionner l'image
            layout.addWidget(image_label)
            name_label = QtWidgets.QLabel(os.path.splitext(os.path.basename(pokemons[i]))[0]) # Ajouter le nom de l'image
            layout.addWidget(name_label, alignment=QtCore.Qt.AlignHCenter)  # Centrer le nom
            self.tableWidget.setCellWidget(row, col, widget) # Ajouter le widget à la cellule du tableau
        self.layout.addWidget(self.tableWidget)

        self.valider_choix = QtWidgets.QPushButton("Valider vos choix") #Ajout du bouton valider
        self.layout.addWidget(self.valider_choix)
        self.valider_choix.clicked.connect(self.close)

        self.tableWidget.horizontalHeader().setDefaultSectionSize(105) # Augmenter la taille des cellules
        self.tableWidget.verticalHeader().setDefaultSectionSize(100)