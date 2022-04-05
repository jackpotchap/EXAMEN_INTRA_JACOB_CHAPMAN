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

#pour la gestion du temps
import datetime

from PyQt5.uic.properties import QtCore


#importation des fenetres
import fenetrelistview
import pythonconfirmation
from interface_UI import interface_principal

#la classe
import patient

from main import ls_patients

#bibliotheque de function qui seront
from logic import turn_str_to_date

def refresh_text_broswer(object):
    """
    Fonction permetant de supprimer le contenue du text_broswer et de réafficher son contenue.
    :param object:
    :return:
    """
    output = ""
    for p in ls_patients:

        output += p.__str__()
        output += "\n"
    object.textBrowser_affichage_patients.setText(output)

def clear_input(object):
    """
    Vider tous les line edit.
    :param object: la fenetre a clear les input de...
    :return:
    """

    object.lineEdit_nom.setText("")
    object.lineEdit_prenom.setText("")
    object.lineEdit_num.setText("")
    object.lineEdit_nbvisite.setText("")

    object.textEdit_commentaire.setPlainText("")

    object.dateEdit_naissance_patient.setSpecialValueText("2000-01-01")

def cacher_labels_erreur(objet):
    """
    Cacher les différents labels d'erreur.
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
    objet.label_erreure_generic_ouvrire.setVisible(False)

    objet.label_erreure_introuvable_sav.setVisible(False)
    objet.label_erreure_introuvable_ouvrire.setVisible(False)



#comme je réutulisais le même code 3 fois je l'ais mis dans une fonction.

def num_is_the_right_format(object, num):
    """
    Fonction qui permet de vérifier si le numéro est de type int et a 7 caratere.
    J'ai faite cette fonction puisque j'utilisait exactement cette logique 3 fois
    :param object:
    :param num: le numéraux a vérifier
    :return: TRUE or FALSE en fonction de si le numéro est affectable.
    """

    #Je crée un patient test pour faire sure qu'il serat attribué.

    cacher_labels_erreur(object)
    test_patient = patient.Patient()

    is_valide = True

    # Vérification pour le num si il est un int.
    try:
        int(num)
    except:
        object.label_erreure_chiffreonly_num.setVisible(True)
        is_valide = False

    else:
        test_patient.NoPatient = num

        #Vérifier si il a été affecté.
        if test_patient.NoPatient == "":
            is_valide = False
            object.label_erreure_taille_num.setVisible(True)

    return is_valide

########################################################
###### DÉFINITIONS DE LA CLASSE fenetre principale ######
########################################################

class FenetrePrincipale(QtWidgets.QMainWindow, interface_principal.Ui_MainWindow):
    #commentaire provenant de Ex_1_interfaceGraphique
    """
    Nome de la classe : FenetrePrincipale
    Héritages :
    - QtWidgets.QMainWindow : Type d'interface créé par QtDesigner
    - interface_principal.Ui_MainWindow : Ma classe générée avec QtDesigner
    """

    def __init__(self, parent=None):
        """
        Constructeur de la classe
        :param parent: QtWidgets.QMainWindow et interface_principal.Ui_MainWindow
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



    #Le bouton pour afficher la fentrelistview.
    @pyqtSlot()
    def on_pushButton_afficherlist_clicked(self):
        """
        Fonction qui se déclencheras lorsque le bouton pushButton_afficherlist seras pressé.
        :return:
        """

        #préparation de la fenêtre
        dialog_list_avancer = fenetrelistview.Fenetrelistview()


        dialog_list_avancer.show()
        reply = dialog_list_avancer.exec_()

    @pyqtSlot()
    def on_pushButton_cree_clicked(self):
        """
        La fonction qui vas s'occuper de verifier que tous les information rentré son valid
        sinon elle vas montrer un message erreure.
        sinon elle vas crée et ajouter le patient à la list et l'afficher dans le text broswer.
        :return:
        """

        cacher_labels_erreur(self)

        #valeur par défault qui seras vraie et si jamais un des valeur n'est pas le bon format le patient ne seras pas
        #ajouter dans la list.
        is_valide = True

        #création de la classe
        nouv_patient = patient.Patient(p_commentaire=self.textEdit_commentaire.toPlainText())


        # GESTION ERREURE POUR NOM
        num = self.lineEdit_num.text()
        is_valide = num_is_the_right_format(self, num)
        if is_valide:
            nouv_patient.NoPatient = num
        else:
            self.label_erreure_chiffreonly_num.setVisible(True)
            self.label_erreure_taille_num.setVisible(True)


        #GESTION ERREURE POUR NOM
        nom = self.lineEdit_nom.text()
        nouv_patient.Nom = nom
        if nouv_patient.Nom == "":
            is_valide = False
            self.label_erreure_lettreonly_nom.setVisible(True)
            self.label_erreure_troplong_nom.setVisible(True)

        # GESTION ERREURE POUR PRENOM
        prenom = self.lineEdit_prenom.text()
        nouv_patient.Prenom = prenom
        if nouv_patient.Prenom == "":
            is_valide = False
            self.label_erreure_lettreonly_prenom.setVisible(True)
            self.label_erreure_troplong_prenom.setVisible(True)

        # GESTION ERREURE POUR DATE DE NAISSANCE
        date_naiss = self.dateEdit_naissance_patient.date()
        #pour pouvoir faire fonctionner l'objet date de PyQt5 et de la librarie datetime
        nouv_patient.Date_naiss = turn_str_to_date(f"{date_naiss.year()}-{date_naiss.month()}-{date_naiss.day()}")
        if nouv_patient.Date_naiss == datetime.date(1,1,1):
            is_valide = False
            self.label_erreure_pasnee_date(True)

        # GESTION ERREURE POUR LE NOMBRE DE VISITES
        nb_visite = self.lineEdit_nbvisite.text()

        try:
            int(nb_visite)
        except:
            self.label_erreure_chiffreonly_nbvisite.setVisible(True)
            is_valide = False

        else:
            nouv_patient.Nb_visite = int(nb_visite)
            if nouv_patient.Nb_visite == -1:
                is_valide = False
                self.label_erreure_positif_nbvisite.setVisible(True)


        #si tous les parramètres son valide l'ajouter à la liste patient et raffraichir le text browser.
        if is_valide == True:

            ls_patients.append(nouv_patient)
            clear_input(self)
            refresh_text_broswer(self)


    @pyqtSlot()
    def on_pushButton_sauvegarder_clicked(self):
        """
        Fonction qui permetera de serialiser le patient correspondant aux numéros de patient correspondant

        :return:
        """

        cacher_labels_erreur(self)

        # verification pour le num
        num = self.lineEdit_num.text()
        is_valide = num_is_the_right_format(self, num)

        #si le numéros est du bon format je vérifie qu'il corespond a un patient de la list
        if is_valide:
            is_valide = False
            # je tente desormais de vérifier si le numeros est dans la liste
            for p in ls_patients:
                if p.NoPatient == num:
                    p.Sauvegarder()
                    is_valide = True

        pop_up = pythonconfirmation.Fenetreconfirmation()

        #si le patient a été trouver afficher la fenetre de confiramtion
        if is_valide:
            pop_up.label_titre_reussite.setVisible(True)
            pop_up.show()
            pop_up.exec_()
        else:
            self.label_erreure_introuvable_sav.setVisible(True)


    @pyqtSlot()
    def on_pushButton_ouvrir_clicked(self):
        """
        Fonction qui permet de déserialiser un patient
        :return:
        """

        # je fait le meme protocole pour vérifier si le num est valide
        cacher_labels_erreur(self)
        nouv_patient = patient.Patient()

        # verification pour le num
        num = self.lineEdit_num.text()

        is_valide = num_is_the_right_format(self, num)

        # si le numéros est du bon format et je vérifie que le fichier existe
        try:

            nouv_patient.Ouvrir(num)
        except:
            self.label_erreure_introuvable_ouvrire.setVisible(True)

            self.label_erreure_generic_ouvrire.setVisible(True)
        else:

            #verification pour ne pas ajouter deux fois le même patient
            is_already_there = False
            for p in ls_patients:
                if p.NoPatient == nouv_patient.NoPatient:
                    is_already_there = True

            if is_already_there != True:
                ls_patients.append(nouv_patient)
                refresh_text_broswer(self)
