import json
from pathlib import Path
from app.models.question import Question

RÉPERTOIRE_DU_PROJET = Path(__file__).resolve().parents[3]

def chemin_questions(salle: str | int) -> Path:
    numéro_salle = int(salle) if str(salle).isdigit() else int(str(salle).split("-")[-1])
    if numéro_salle < 1 or numéro_salle > 3:
        numéro_salle = 1
    return RÉPERTOIRE_DU_PROJET / f"question-salle-{numéro_salle}.json"


def ajout_question(question : Question) -> str:
    donnees = []
    with open(chemin_questions(question.salle), 'r', encoding='utf-8') as fichier:
        donnees = json.load(fichier)
        donnees.append(question.model_dump())

    with open(chemin_questions(question.salle), 'w', encoding='utf-8') as fichier:
        json.dump(donnees, fichier, indent=4, ensure_ascii=False)
    
    return ""

def suppresion_question(id_salle:int, id_question:int) -> str:
    if id_salle < 1 or id_salle > 3 :
        id_salle = 1

    fichierJSON = chemin_questions(id_salle)

    donnees = []
    with open(fichierJSON, 'r', encoding='utf-8') as fichier:
        donnees = json.load(fichier)
        if len(donnees) > id_question and id_question >= 0 :
            donnees.pop(id_question)
        else :
            return f"Cette identifiant est invalide et n'est pas dans la plage des [0, {len(donnees)}[ questions valides."

    with open(fichierJSON, 'w', encoding='utf-8') as fichier:
        json.dump(donnees, fichier, indent=4, ensure_ascii=False)

    return ""


def modification_reponse_question(id_salle:int, id_question:int, nouvelle_reponse:int) -> str :
    if id_salle < 1 or id_salle > 3 :
        id_salle = 1
        
    fichierJSON = chemin_questions(id_salle)
        
    donnees = []
    with open(fichierJSON, 'r', encoding='utf-8') as fichier:
        donnees = json.load(fichier)
        if len(donnees) > id_question and id_question >= 0 :
            donnees[id_question]["réponse"] = nouvelle_reponse
        else :
            return f"Cette identifiant est invalide et n'est pas dans la plage des [0, {len(donnees)}[ questions valides."
    with open(fichierJSON, 'w', encoding='utf-8') as fichier:
        json.dump(donnees, fichier, indent=4, ensure_ascii=False)

    return ""


