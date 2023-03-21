"""Creer une base de donnee SQLite et l'exploiter"""


import sqlite3


CONNEXION = sqlite3.connect("test_connexion_de_donnee.db")
CURSEUR = CONNEXION.cursor()

def connexion_au_base():
    global CONNEXION, CURSEUR

    CONNEXION = sqlite3.connect("test_connexion_de_donnee.db")
    CURSEUR = CONNEXION.cursor()
##    print("Base de donnee cree ou connectee correctement a SQLite\n")


def deconnexion_au_base():
    global CONNEXION, CURSEUR

    CURSEUR.close()
    CONNEXION.close()
##    print("Base de donnee deconnectee correctement a SQLite\n")


def creer_une_table():
    global CONNEXION, CURSEUR
    connexion_au_base()

    requeteSQL = "\
        CREATE TABLE IF NOT EXISTS Formulaire\
            (\
                nom VARCHAR(15),\
                prenom VARCHAR(15),\
                score INT\
            );\
            "
    CURSEUR.execute(requeteSQL)
    deconnexion_au_base()


def remplir_la_table():
    """On prend les infos du joueur."""
    global CONNEXION, CURSEUR
    creer_une_table()
    
    connexion_au_base()

    score: int = 0

    motSecret: str = "toshiro"
    nom_user = input("Entrer votre nom\n")
    prenom_user = input("Entrer votre prenom\n")
    password = input("Entrer le mot Secret:\n")

    if password == "toshiro":
        score = 20
    else:
        score = 0
    print(f"Votre score est: {score} \n")
    value = (nom_user, prenom_user, score)

    requeteSQL = "INSERT INTO Formulaire (nom, prenom, score)\
        VALUES (?, ?, ?)"

    CURSEUR.execute(requeteSQL, value)

    CONNEXION.commit()

    deconnexion_au_base()


def afficher_base_de_donnee():
    """Afficher la base de donnee."""
    global CONNEXION, CURSEUR
    connexion_au_base()

    requeteSQL = "SELECT * FROM Formulaire"
    CURSEUR.execute(requeteSQL)

    resultats = CURSEUR.fetchall()
    
    print(f"Voici votre base de donnee SQLite:\n")
    
    print("NOM\t\t\t PRENOM\t\t\t SCORE\n")

    for i in range(len(resultats)):
        for j in range(3):
            print(f"{resultats[i][j]}")
            print("\n")

    deconnexion_au_base()


#main
print("\n\n_______MENU__________\n\n\
      1- Enregistrer une personne\n\
        2- Lister le formulaire\n")

choix = input("\nFaites un choix\n")

if choix == "1":
   remplir_la_table()
elif choix == "2":
    afficher_base_de_donnee()
else:
    print("Mauvais choix\n")
