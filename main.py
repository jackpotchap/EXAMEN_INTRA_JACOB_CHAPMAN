####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: EXAMEN INTRA - Interface graphique
###  Nom: Jacbo Chapman
###  No étudiant: 2030490
###  No Groupe: 00001
###  Description du fichier: Programme principal
####################################################################################


#######################################
###  IMPORTATIONS - Portée globale  ###
########+###############################

# Importer le module sys nécessaire à l'exécution.
import sys
# Pour la réinitialisation de la date dans le dateEdit
from PyQt5.QtCore import QDate

# Importer Pour le model de la listView
from PyQt5.QtGui import QStandardItemModel, QStandardItem

#importation de la classe patient
import patient

##########################################################
###  DÉCLARATIONS ET INITIALISATIONS - Portée globale  ###
##########################################################

#initialisation de la list de patient
ls_patients = []

#######################################
###### DÉFINITIONS DES FONCTIONS ######
#######################################

