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
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from interface_UI import list_avance_pop_up_interface

from main import ls_patients
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

    @pyqtSlot()
    def on_pushButton_age_rechercher_clicked(self):
        #je commence par proceder a une vérification de donné
        #Pour l'age min , lage max et le prix
        valide = True

        age_min = self.lineEdit_age_min.text()

        try:
            int(age_min)
        except:
            self.label_erreure_chiffreonly_num_age_min.setVisible(True)
            valide = False
        else:
            if int(age_min) < 0:
                self.label_erreure_taille_age_min.setVisible((True))
                valide = False

        age_max = self.lineEdit_age_max.text()

        try:
            int(age_max)
        except:
            self.label_erreure_chiffreonly_num_age_max.setVisible(True)
            valide = False
        else:
            if int(age_max) < 0:
                self.label_erreure_taille_age_max.setVisible((True))
                valide = False

        prix = self.lineEdit_prix.text()

        try:
            float(prix)
        except:
            self.label_erreure_chiffreonly_num_prix.setVisible(True)
            valide = False
        else:
            if int(prix) < 0:
                self.label_erreure_positif.setVisible((True))
                valide = False

        if valide:
            #verifier si min est belle et bien plus petit que max
            if age_max < age_min:
                valide = False


                model = QStandardItemModel()

                #Pour afficher directement le message erreure dans listView_list_patient_avanc
                self.listView_list_patient_avance.setModel(model)

                #on peut utiliser du css pour modifier la couleur du text
                self.listView_list_patient_avance.setStyleSheet("color: #D0312D;")

                message = QStandardItem("* l'age minimum doit absolument etre")
                model.appendRow(message)

                message = QStandardItem("  inférieure ou égale a l'age maximum")
                model.appendRow(message)

            else:


                model = QStandardItemModel()
                self.listView_list_patient_avance.setStyleSheet("color: #000000;")
                self.listView_list_patient_avance.setModel(model)

                for p in ls_patients:
                    age = p.calculer_age(p.Date_naiss)
                    print("age = p.calculer_age(p.Date_naiss)")
                    print(type(age))
                    if  int(age) <= int(age_max) and int(age) >= int(age_min):
                        print("age <= age_max and age > age_min")
                        item = QStandardItem(f"{p.NoPatient} –– {p.Prenom} {p.Nom} –– {int(age)} ––  {p.calculer_cout_total(float(prix)): .2f} $")
                        model.appendRow(item)

