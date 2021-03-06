####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: EXAMEN INTRA - Interface graphique
###  Nom: Jacob Chapman
###  No étudiant: 2030490
###  No Groupe: 00001
###  Description du fichier: Classe fenetreconfirmation
####################################################################################


######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################


from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot

from interface_UI import save_pop_up_interface

def cacher_labels_erreur(objet):
    """
    Cacher les différents labels d'erreur
    """
    objet.label_erreure_savwrong.setVisible(False)
    objet.label_titre_reussite.setVisible(False)


class Fenetreconfirmation(QtWidgets.QDialog, save_pop_up_interface.Ui_Dialog):
    def __init__(self, parent=None):
        """
        Nome de la classe : Fenetreconfirmation
        Héritages :
        - QtWidgets.QDialog : Type d'interface créé par QtDesigner
        - save_pop_up_interface.Ui_Dialog : Ma classe générée avec QtDesigner
        """
        super(Fenetreconfirmation, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Confirmation")

        cacher_labels_erreur(self)
    @pyqtSlot()
    def on_pushButton_hide_save_pop_up_clicked(self):
        """
        Fonction pour fermer la fenêtre de confirmation
        :return:
        """
        self.close()