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

from logic import turn_str_to_date

class Patient:
    """
         Classe Etudiant

        """

    ###################################
    #####  MÉTHODE CONSTRUCTEUR  #####
    ###################################

    def __init__(self, p_no_patient : str = "", p_nom : str = "", p_prenom:str = "", p_date_naiss:str = "1-1-1", p_nb_visite :  int = -1, p_commentaire : str = ""):
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

    def __str__(self) -> str:

        output = ""
        output += "****************************************************\n"
        output += "\n"
        output += f"le numéro du patient: {self.NoPatient}\n"
        output += f"le nom du patient: {self.Nom}\n"
        output += f"le prenom du patient: {self.Prenom}\n"
        #j'utilise un int pour pas que on voit les decimale de l'age,
        # qui sont nessesaire pour verifier dans la fonction set age si l'age est supérieur a 0

        output += f"l'age' du patient: {int(self.calculer_age(turn_str_to_date(self.Date_naiss)))}\n"
        output += "\n"
        output += f"le nombre de visite du patient: {str(self.Nb_visite)}\n"
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

    def calculer_age(self, p_date_naiss: datetime.date) -> float:
        """
        Méthodes permetant de calculer le nombres de jours entre deux dates et de faire un conversion en années
        :param p_date_naiss: la date de naissance qui feras la soustrantion avec la date de aujourd'hui
        :return: retourne le nombres années écouler entre deux dates
        """

        nb_jour = (datetime.date.today() - p_date_naiss).days

        #il y a 365 jour et 1 de plus a chaque 4 ans donc on divise le total de jour par 365.25

        nb_annee = nb_jour/365.25

        return nb_annee

    def calculer_cout_total(self, cout:float) -> float:
        """
        Méthode permetant de calculer le cout total en fesant le nombres de visites * le cout
        :param cout: le montant qui seras multiplier par le nombre de visites
        :return: le nombres de visites par l'âge
        """
        return self.__nb_visite*cout


    #CODE PROVENANT DU DOCUMENT DISTRIBUER EN CLASSE
    def Sauvegarder(self):
        """
        Méthode permettant de sérialiser un objet de la classe Patient

        """
        with open(f"Fichiers_JSON/{self.__no_patient}", "w") as fichier:
            json.dump(self.__dict__, fichier)

    def Ouvrir(self, p_fichier):
        """
            Méthode permttant de désérialiser un objet de la classe Patient
            ::param p_fichier : Le nom du fichier qui contient l'objet sérialisé
                """

        with open(f"Fichiers_JSON/{p_fichier}" , "r") as fichier :

            self.__dict__ = json.load(fichier)

    #######################################
    ###### DÉFINITIONS DES PROPRIÉTÉS #####
    #######################################



    #Propriété de no_patient
    def _get_no_patient(self) -> str:
        """
        Accesseur de l'attribut privé  __no_patient

        """
        return self.__no_patient

    def _set_no_pattient(self, p_num : str):
        """
        Mutateur de l'attribur privé __no_patient
        """
        #doit etre composé de sept chiffres

        if len(p_num) == 7:
            self.__no_patient = p_num

    NoPatient = property(_get_no_patient, _set_no_pattient)

    #Propriété de nom

    def _get_nom(self)-> str:
        """
                Accesseur de l'attribut privé  __nom

                """
        return self.__nom

    def _set_nom(self, p_nom:str):
        """
                Mutateur de l'attribur privé __nom
                """
        # doit avoir au maximum 30 caractères alphabétiques

        if len(p_nom) <= 30:

            if p_nom.isalpha():

                self.__nom = p_nom

    Nom = property(_get_nom, _set_nom)

    # Propriété de prenom

    def _get_prenom(self)-> str:
        """
                        Accesseur de l'attribut privé  __prenom

                        """
        return self.__prenom

    def _set_prenom(self, p_prenom:str):
        """
                        Mutateur de l'attribur privé __prenom
                        """
        # doit avoir au maximum 30 caractères alphabétiques

        if len(p_prenom) <= 30:
            if p_prenom.isalpha():
                self.__prenom = p_prenom

    Prenom = property(_get_prenom, _set_prenom)

    # Propriété de date_naiss

    def _get_date_naiss(self) -> datetime.date:
        """
                        Accesseur de l'attribut privé  __date_naiss

                        """
        return self.__date_naiss

    def _set_date_naiss(self, p_date_naiss:datetime.date):
        """
                        Mutateur de l'attribur privé __date_naiss
                        """

        age = self.calculer_age(p_date_naiss)


        if age > 0:
            self.__date_naiss = str(p_date_naiss)



    Date_naiss = property(_get_date_naiss, _set_date_naiss)

    # Propriété de nb_visite

    def _get_nb_visite(self) -> int:
        """
                        Accesseur de l'attribut privé  __nb_visite

                        """
        return self.__nb_visite

    def _set_nb_visite(self, p_nb_visite: int):
        """
                        Mutateur de l'attribur privé __nb_visite
                        """
        # doit etre positif
        if p_nb_visite >= 0:
            self.__nb_visite = p_nb_visite



    Nb_visite = property(_get_nb_visite, _set_nb_visite)

    # Propriété de couriel
    def _get_couriel(self) -> str:
        """
                        Accesseur de l'attribut privé  __couriel
                        """
        return f"{self.__nom}_{self.__prenom}@CabinetMedical.ca"

    Couriel = property(_get_couriel, )






