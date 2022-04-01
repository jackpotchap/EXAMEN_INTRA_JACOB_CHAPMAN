####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: EXAMEN INTRA - Interface graphique
###  Nom: Jacbo Chapman
###  No étudiant: 2030490
###  No Groupe: 00001
###  Description du fichier: Classe Patient
####################################################################################

#source commentaire Ex1_InterfaceGraphique

#pour la séréalisation
import json

#pour calculer l'age
import datetime

class Patient:
    """
         Classe Etudiant

        """

    ###################################
    #####  MÉTHODE CONSTRUCTEUR  #####
    ###################################

    def __init__(self, p_no_patient : str = "", p_nom : str = "", p_prenom:str = "", p_date_naiss:str = "", p_nb_visite : str = "" , p_commentaire : str = ""):
        """
        Constructeur avec paramètres et valeurs par défaut. Définition des attributs publics d'un étudiant
        :param p_no_patient: le numéro du patient
        :param p_nom: le nom du patient
        :param p_prenom: le prenom du patient
        :param p_date_naiss: la date de naissance du patient
        :param p_nb_visite: le nombres de visites du patient
        :param commentaire: commentaire sur le patient
        """

        self.__no_patient = p_no_patient
        self.__nom = p_nom
        self.__prenom= p_prenom
        self.__date_naiss = p_date_naiss
        self.__nb_visite = p_nb_visite

        self.Commentaire = p_commentaire

    #######################################
    ###### DÉFINITIONS DES MÉTHODES ######
    #######################################

    def __str__(self):
        output = ""
        output += "****************************************************\n"
        output += "\n"
        output += f"le numéro du patient: {self.__no_patient}\n"
        output += f"le nom du patient: {self.__nom}\n"
        output += f"l'age' du patient: {self.calculer_age()}\n"
        output += "\n"
        output += f"le nombre de visite du patient: {self.__nb_visite}\n"
        output += "\n"
        output += f"le courielle du patient: {self.Couriel}\n"
        output += "\n"
        output += "\n"
        output += f"Commentaire: {self.Commentaire}\n"
        output += "\n"
        output += "****************************************************\n"
        output += "\n"
        output += "\n"

        return output


    def
    # Propriété de no_patient
    def _get_no_patient(self):
        return self.__no_patient

    def _set_no_pattient(self, p_num):

        #doit etre composé de sept chiffres

        if len(p_num) == 7:
            self.__no_patient = p_num

    NoPatient = property(_get_no_patient, _set_no_pattient)

    # Propriété de nom

    def _get_nom(self):
        return self.__nom

    def _set_nom(self, p_nom):

        # doit avoir au maximum 30 caractères alphabétiques

        if len(p_nom) <= 30:
            if p_nom.isalpha():
                self.__nom = p_nom

    Nom = property(_get_nom, _set_nom)

    # Propriété de prenom

    def _get_prenom(self):
        return self.__prenom

    def _set_prenom(self, p_prenom):

        # doit avoir au maximum 30 caractères alphabétiques

        if len(p_prenom) <= 30:
            if p_prenom.isalpha():
                self.__prenom = p_prenom

    PreNom = property(_get_prenom, _set_prenom)

    # Propriété de date_naiss

    def _get_date_naiss(self):
        return self.__date_naiss

    def _set_date_naiss(self, p_date_naiss):

        # doit être inférieure ou égale à la date du jour

        pass

    Date_naiss = property(_get_date_naiss, _set_date_naiss)

    # Propriété de nb_visite

    def _get_nb_visite(self):
        return self.__nb_visite

    def _set_nb_visite(self, p_nb_visite: int):

        # doit etre positif
        if p_nb_visite >= 0:
            self.__nb_visite = p_nb_visite



    Nb_visite = property(_get_nb_visite, _set_nb_visite)

    # Propriété de couriel
    def _get_couriel(self):
        return f"{self.__nom}_{self.__prenom}@CabinetMedical.ca"

    Couriel = property(_get_couriel, )

