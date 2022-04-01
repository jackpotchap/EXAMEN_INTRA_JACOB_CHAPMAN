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
import datetime
import fenetrelistview
import patient
from interface_UI import interface_principal
from main import ls_patients

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
        cacher_labels_erreur(self)

    def clear_input(object):
        object.lineEdit_nom.setText("")
        object.lineEdit_prenom.setText("")
        object.lineEdit_num.setText("")
        object.textEdit_commentaire.setPlainText("")


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
        print("patient.Patient")
        nouv_patient = patient.Patient(p_commentaire=self.textEdit_commentaire.PlainText())

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



        if is_valide == True:
            ls_patients.append(nouv_patient)




