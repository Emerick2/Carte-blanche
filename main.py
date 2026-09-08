import json
from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
def début() :
    return "Bonjour ! Bienvenu dans le jeu !"

@app.get("/question/salle-1/liste")
def salle_1_liste() :
    with open('question-salle-1.json', 'r', encoding='utf-8') as fichier:
        donnees = json.load(fichier)
        return donnees

@app.get("/question/salle-1")
def salle_1_question() :
    with open('question-salle-1.json', 'r', encoding='utf-8') as fichier:
        donnees = json.load(fichier)
        return donnees[random.randrange(0,len(donnees))]
    
@app.get("/question/salle-1/{question_id}")
def salle_1_question_id(question_id) :
    with open('question-salle-1.json', 'r', encoding='utf-8') as fichier:
        donnees = json.load(fichier)
        if len(donnees) <= question_id :
            return ""
        return donnees[int(question_id)]

# --------------------------------------------------------------

@app.get("/question/salle-2/liste")
def salle_2_liste() :
    with open('question-salle-2.json', 'r', encoding='utf-8') as fichier:
        donnees = json.load(fichier)
        return donnees

@app.get("/question/salle-2")
def salle_2_question() :
    with open('question-salle-2.json', 'r', encoding='utf-8') as fichier:
        donnees = json.load(fichier)
        return donnees[random.randrange(0,len(donnees))]
    
@app.get("/question/salle-2/{question_id}")
def salle_2_question_id(question_id) :
    with open('question-salle-2.json', 'r', encoding='utf-8') as fichier:
        donnees = json.load(fichier)
        if len(donnees) <= question_id :
            return ""
        return donnees[int(question_id)]

# --------------------------------------------------------------

@app.get("/question/salle-3/liste")
def salle_3_liste() :
    with open('question-salle-3.json', 'r', encoding='utf-8') as fichier:
        donnees = json.load(fichier)
        return donnees

@app.get("/question/salle-3")
def salle_3_question() :
    with open('question-salle-3.json', 'r', encoding='utf-8') as fichier:
        donnees = json.load(fichier)
        return donnees[random.randrange(0,len(donnees))]
    
@app.get("/question/salle-3/{question_id}")
def salle_3_question_id(question_id) :
    with open('question-salle-3.json', 'r', encoding='utf-8') as fichier:
        donnees = json.load(fichier)
        if len(donnees) <= question_id :
            return ""
        return donnees[int(question_id)]

# --------------------------------------------------------------

