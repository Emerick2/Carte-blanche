import json
from fastapi import FastAPI
import random

app = FastAPI()

déjà_vu = {
    "salle-1" : [],
    "salle-2" : [],
    "salle-3" : []
}

def nombre_aléatoire_avec_liste_à_ignorer(liste_origine, liste_à_ignorer):
    liste = []
    for i in range (len(liste_origine)) :
        if ((liste_origine[i] in liste_à_ignorer) == False):
            liste.append(i)

    if len(liste) > 0 :
        return random.randrange(0,len(liste))
    else :
        print("/!\\ - La liste des numéros de question déjà posée n'as pas été remise à zéro suffisament vite !")
        return random.randrange(0,len(liste_origine))


@app.get("/")
def début() :
    return "Bonjour ! Bienvenu dans le jeu !"

@app.get("/question/{salle}/liste")
def salle_liste(salle : str) :
    fichier_json = 'question-salle-1.json'
    if salle == "salle-2" :
        fichier_json = 'question-salle-2.json'
    elif salle == "salle-3" :
        fichier_json = 'question-salle-3.json'
    else :
        salle = "salle-1"

    with open(fichier_json, 'r', encoding='utf-8') as fichier:
        donnees = json.load(fichier)
        return donnees

@app.get("/question/{salle}")
def salle_question(salle : str) :
    fichier_json = 'question-salle-1.json'
    if salle == "salle-2" :
        fichier_json = 'question-salle-2.json'
    elif salle == "salle-3" :
        fichier_json = 'question-salle-3.json'
    else :
        salle = "salle-1"
    
    with open(fichier_json, 'r', encoding='utf-8') as fichier:
        donnees = json.load(fichier)

        if déjà_vu[salle] == None or len(déjà_vu[salle]) >= len(donnees)-1:
            déjà_vu[salle] = []

        identifiant_aléatoire = nombre_aléatoire_avec_liste_à_ignorer(donnees, déjà_vu[salle])
        déjà_vu[salle].append(identifiant_aléatoire)

        return donnees[identifiant_aléatoire]
    
@app.get("/question/{salle}/{question_id}")
def salle_question_id(salle : str, question_id : int) :
    fichier_json = 'question-salle-1.json'
    if salle == "salle-2" :
        fichier_json = 'question-salle-2.json'
    elif salle == "salle-3" :
        fichier_json = 'question-salle-3.json'
    else :
        salle = "salle-1"

    
    with open(fichier_json, 'r', encoding='utf-8') as fichier:
        donnees = json.load(fichier)
        if len(donnees) <= question_id :
            return ""
        return donnees[int(question_id)]

# --------------------------------------------------------------
