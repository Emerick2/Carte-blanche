import json
from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
def début() :
    return "Bonjour ! Bienvenu dans le jeu !"

@app.get("/question/{salle}/liste")
def salle_liste(salle : str) :
    fichier_json = 'question-salle-1.json'
    if salle == "salle-2" :
        fichier_json = 'question-salle-2.json'
    if salle == "salle-3" :
            fichier_json = 'question-salle-3.json'

    with open(fichier_json, 'r', encoding='utf-8') as fichier:
        donnees = json.load(fichier)
        return donnees

@app.get("/question/{salle}")
def salle_question(salle : str) :
    fichier_json = 'question-salle-1.json'
    if salle == "salle-2" :
        fichier_json = 'question-salle-2.json'
    if salle == "salle-3" :
        fichier_json = 'question-salle-3.json'
    
    with open(fichier_json, 'r', encoding='utf-8') as fichier:
        donnees = json.load(fichier)
        return donnees[random.randrange(0,len(donnees))]
    
@app.get("/question/{salle}/{question_id}")
def salle_question_id(salle : str, question_id : int) :
    fichier_json = 'question-salle-1.json'
    if salle == "salle-2" :
        fichier_json = 'question-salle-2.json'
    if salle == "salle-3" :
        fichier_json = 'question-salle-3.json'

    
    with open(fichier_json, 'r', encoding='utf-8') as fichier:
        donnees = json.load(fichier)
        if len(donnees) <= question_id :
            return ""
        return donnees[int(question_id)]

# --------------------------------------------------------------
