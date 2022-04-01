####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: EXAMEN INTRA - Interface graphique
###  Nom: Jacbo Chapman
###  No étudiant: 2030490
###  No Groupe: 00001
###  Description du fichier: regroupement de fonction logic
####################################################################################

#importation de la gestion du temps
import datetime

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