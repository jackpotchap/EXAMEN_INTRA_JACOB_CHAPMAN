####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: EXAMEN INTRA - Interface graphique
###  Nom: Jacob Chapman
###  No étudiant: 2030490
###  No Groupe: 00001
###  Description du fichier: Classe fenetrelistview
####################################################################################


######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot

from interface_UI import list_avance_pop_up_interface

def cacher_labels_erreur(objet):
    """
    Cacher les différents labels d'erreur
    """
    objet.label_erreure_taille_age_min.setVisible(False)
    objet.label_erreure_chiffreonly_num_age_min.setVisible(False)
    objet.label_erreure_chiffreonly_num_age_max.setVisible(False)
    objet.label_erreure_positif.setVisible(False)
    objet.label_erreure_chiffreonly_num_prix.setVisible(False)
    objet.label_erreure_taille_num_age_max.setVisible(False)






class Fenetrelistview(QtWidgets.QDialog, list_avance_pop_up_interface.Ui_Dialog):
    def __init__(self, parent=None):
        super(Fenetrelistview, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Liste des étudiant.e.s")
        cacher_labels_erreur(self)

    @pyqtSlot()
    def on_pushButton_hide_list_avance_clicked(self):
        self.close()