####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: EXAMEN INTRA - Interface graphique
###  Nom: Jacob Chapman
###  No étudiant: 2030490
###  No Groupe: 00001
###  Description du fichier: Classe fenetrePrincipale
####################################################################################

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot, QDate
import datetime

from PyQt5.uic.properties import QtCore

import fenetrelistview
import pythonconfirmation
import patient
from interface_UI import interface_principal
from main import ls_patients, turn_str_to_date


def refresh_text_broswer(object):
    output = ""
    for p in ls_patients:
        print(p)
        output += p.__str__()
        output += "\n"
    object.textBrowser_affichage_patients.setText(output)

def clear_input(object):
    print("object.textEdit_commentaire.setPlainText")
    object.lineEdit_nom.setText("")
    object.lineEdit_prenom.setText("")
    object.lineEdit_num.setText("")
    object.lineEdit_nbvisite.setText("")
    print("object.textEdit_commentaire.setPlainText")
    object.textEdit_commentaire.setPlainText("")

    object.dateEdit_naissance_patient.setSpecialValueText("2000-01-01")

def cacher_labels_erreur(objet):
    """
    Cacher les différents labels d'erreur
    """
    objet.label_erreure_troplong_nom.setVisible(False)
    objet.label_erreure_lettreonly_nom.setVisible(False)
    objet.label_erreure_chiffreonly_num.setVisible(False)
    objet.label_erreure_taille_num.setVisible(False)
    objet.label_erreure_lettreonly_prenom.setVisible(False)

    objet.label_erreure_troplong_prenom.setVisible(False)
    objet.label_erreure_pasnee_date.setVisible(False)
    objet.label_erreure_chiffreonly_nbvisite.setVisible(False)
    objet.label_erreure_positif_nbvisite.setVisible(False)
    objet.label_erreure_introuvable_ouvrire.setVisible(False)

    objet.label_erreure_generic_ouvrire.setVisible(False)


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
        clear_input(self)
        cacher_labels_erreur(self)



    #le bouton pour afficher la fentrelistview
    @pyqtSlot()
    def on_pushButton_afficherlist_clicked(self):

        dialog_list_avancer = fenetrelistview.Fenetrelistview()
        # Préparer la listview

        dialog_list_avancer.show()
        reply = dialog_list_avancer.exec_()

    @pyqtSlot()
    def on_pushButton_cree_clicked(self):
        """
        La fonction qui vas soccuper de verifier que tous les information rentrer son valid
        sinon elle vas montrer un message erreure.
        sinon elle vas cree et ajouter le patient a la list et l'afficher dans le text broswer
        :return:
        """

        cacher_labels_erreur(self)
        print()

        nouv_patient = patient.Patient(p_commentaire=self.textEdit_commentaire.toPlainText())

        print("allo2")

        is_valide = True
        #verification pour le num

        print("num")
        num = self.lineEdit_num.text()

        try:
            int(num)
        except:
            self.label_erreure_chiffreonly_num.setVisible(True)
            is_valide = False

        else:
            nouv_patient.NoPatient = num
            if nouv_patient.NoPatient == "":
                is_valide = False
                self.label_erreure_taille_num.setVisible(True)

        print("nom")
        nom = self.lineEdit_nom.text()
        nouv_patient.Nom = nom
        if nouv_patient.Nom == "":
            is_valide = False
            self.label_erreure_lettreonly_nom.setVisible(True)
            self.label_erreure_troplong_nom.setVisible(True)

        print("prenom")
        prenom = self.lineEdit_prenom.text()
        nouv_patient.Prenom = prenom
        if nouv_patient.Prenom == "":
            is_valide = False
            self.label_erreure_lettreonly_prenom.setVisible(True)
            self.label_erreure_troplong_prenom.setVisible(True)

        print("date_naiss")
        date_naiss = self.dateEdit_naissance_patient.date()
        print("date_naiss.date")

        #pour pouvoir fiare fonctionner lobjet date de qt et de la librarie datetime
        nouv_patient.Date_naiss = turn_str_to_date(f"{date_naiss.year()}-{date_naiss.month()}-{date_naiss.day()}")
        print("date_naiss.=")
        print(nouv_patient.Date_naiss)
        print(date_naiss)
        #   1-1-1                     dasdasdasd(1,1,1)
        if nouv_patient.Date_naiss == datetime.date(1,1,1):
            print("Date_naiss == datetime.date(0,0,0)")
            is_valide = False
            self.label_erreure_pasnee_date(True)


        print("nb_visite")

        nb_visite = self.lineEdit_nbvisite.text()
        print("nb_visite = self.lineEdit_nbvisite.text()")
        try:
            int(nb_visite)
        except:
            self.label_erreure_chiffreonly_nbvisite.setVisible(True)
            is_valide = False

        else:
            print("try nb_visite")
            nouv_patient.Nb_visite = int(nb_visite)
            print("nouv_patient.Nb_visite")
            if nouv_patient.Nb_visite == -1:
                is_valide = False
                self.label_erreure_positif_nbvisite.setVisible(True)


        print("allo")
        if is_valide == True:

            ls_patients.append(nouv_patient)
            print("allo")
            clear_input(self)
            print("clear input")
            refresh_text_broswer(self)


    @pyqtSlot()
    def on_pushButton_sauvegarder_clicked(self):
        #je fait le meme protocole pour vérifier si le num est valide nouv_patient = patient.Patient(p_commentaire=self.textEdit_commentaire.toPlainText())
        cacher_labels_erreur(self)
        nouv_patient = patient.Patient()


        is_valide = True
        #verification pour le num


        num = self.lineEdit_num.text()

        try:
            int(num)
        except:
            self.label_erreure_chiffreonly_num.setVisible(True)
            is_valide = False

        else:
            nouv_patient.NoPatient = num
            if nouv_patient.NoPatient == "":
                is_valide = False
                self.label_erreure_taille_num.setVisible(True)


        if is_valide:
            is_valide = False
            # je tente desormais de vérifier si le numeros est dans la liste
            for p in ls_patients:
                if p.NoPatient == num:
                    p.Sauvegarder()
                    is_valide = True

        pop_up = pythonconfirmation.Fenetreconfirmation()
        if is_valide:
            pop_up.label_titre_reussite.setVisible(True)
        else:
            pop_up.label_erreure_savwrong.setVisible(True)
        pop_up.show()
        pop_up.exec_()


