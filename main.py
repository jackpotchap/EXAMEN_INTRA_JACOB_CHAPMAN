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

#######################################
###### DÉFINITIONS DES FONCTIONS ######
#######################################

def turn_str_to_date(p_date: str) -> datetime.date:
    """
    transformer une chaine de caracetre en type datetime.date
    si jamais le format est incorect il renveras la date de aujourd'hui
    :param p_date: la date de type str qui seras transformer
    :return: la dans en type datetime.date
    """

    # comme il sajit d'une function de plus je me suis selement permis de faire une gestion erreure pour le format
    try:

        date = p_date.split("-")

        year = int(date[0])
        month = int(date[1])
        day = int(date[2])

        return datetime.date(year, month, day)
    except:
        print("desoler le format est incorrect")
        return datetime.date.today()











########################################################
######  DÉFINITIONS DE LA CLASSE fenetre de list  ######
########################################################


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
