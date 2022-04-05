####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: EXAMEN INTRA - Interface graphique
###  Nom: Jacbo Chapman
###  No étudiant: 2030490
###  No Groupe: 00001
###  Description du fichier: Programme principal
####################################################################################

#source commentaire Ex1_InterfaceGraphique

#######################################
###  IMPORTATIONS - Portée globale  ###
########+###############################

# Importer le module sys nécessaire à l'exécution.
import sys

# Pour la réinitialisation de la date dans le dateEdit
from PyQt5 import QtWidgets
import PyQt5

# Importer Pour le model de la listView
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QStandardItemModel, QStandardItem

#importation de la classe patient

#importation de la gestion du temps
import datetime

#importation des window
import fenetrePrincipale
from interface_UI import interface_principal

##########################################################
###  DÉCLARATIONS ET INITIALISATIONS - Portée globale  ###
##########################################################

#initialisation de la list de patient

ls_patients = []


#################################
###### PROGRAMME PRINCIPAL ######
#################################

# Créer le main qui lance la fenêtre de Qt


def main():
    """
    Méthode main : point d'entré du programme.
    Exécution de l'applicatin avec l'interface graphique.
    reply = Dialog.exec_()
    """
    # Instancier une application et une fenetre principale
    app = QtWidgets.QApplication(sys.argv)
    form = fenetrePrincipale.FenetrePrincipale()
    # Afficher la fenêtre principale
    form.show()
    # Lancer l'application
    app.exec()


if __name__ == "__main__":
    main()
