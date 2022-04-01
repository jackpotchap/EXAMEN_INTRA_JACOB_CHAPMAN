####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: EXAMEN INTRA - Interface graphique
###  Nom: Jacob Chapman
###  No étudiant: 2030490
###  No Groupe: 00001
###  Description du fichier: Classe fenetrePrincipale
####################################################################################

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot

import fenetrelistview
from interface_UI import interface_principal
from main import cacher_labels_erreur


########################################################
###### DÉFINITIONS DE LA CLASSE fenetre principale ######
########################################################

class FenetrePrincipale(QtWidgets.QMainWindow, interface_principal.Ui_MainWindow):
    """
    Nome de la classe : fenetrePrincipale
    Héritages :
    - QtWidgets.QMainWindow : Type d'interface créé par QtDesigner
    - interface_principal.Ui_MainWindow : Ma classe générée avec QtDesigner
    """

    def __init__(self, parent=None):
        """
        Constructeur de la classe
        :param parent: QtWidgets.QMainWindow et iinterface_principal.Ui_MainWindow
        """
        # Appeler le constructeur parent avec ma classe en paramètre...
        super(FenetrePrincipale, self).__init__(parent)
        # Préparer l'interface utilisateur
        self.setupUi(self)
        # Donner un titre à la fenêtre principale
        self.setWindowTitle("Gestion de patient")
        # Cacher tous les labels d'erreur
        cacher_labels_erreur(self)


    #le bouton pour afficher la fentrelistview
    @pyqtSlot()
    def on_pushButton_afficherlist_clicked(self):

        dialog_list_avancer = fenetrelistview.Fenetrelistview()
        # Préparer la listview

        dialog_list_avancer.show()
        reply = dialog_list_avancer.exec_()
