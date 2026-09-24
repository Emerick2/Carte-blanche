import json
from pathlib import Path
from fastapi import APIRouter, HTTPException
from app.services.données_services import données_du_jeu, identifiant_position_partie, nombre_aléatoire_avec_liste_à_ignorer
from app.models.question import Question

RÉPERTOIRE_DU_PROJET = Path(__file__).resolve().parents[3]

def chemin_questions(salle: str | int) -> Path:
    numéro_salle = int(salle) if str(salle).isdigit() else int(str(salle).split("-")[-1])
    if numéro_salle < 1 or numéro_salle > 3:
        numéro_salle = 1
    return RÉPERTOIRE_DU_PROJET / f"question-salle-{numéro_salle}.json"

router = APIRouter(
    prefix='/question',
    tags=['question'],
)

@router.get("/{salle}/liste")
def salle_liste(salle : str) :
    with open(chemin_questions(salle), 'r', encoding='utf-8') as fichier:
        donnees = json.load(fichier)
        return donnees

@router.get("/{id_partie}/{salle}")
def salle_question(id_partie:str, salle : str) :
    global données_du_jeu
    id_partie = identifiant_position_partie(id_partie)
    if (id_partie != -1) :
        salle = salle if salle in ("salle-1", "salle-2", "salle-3") else "salle-1"

        with open(chemin_questions(salle), 'r', encoding='utf-8') as fichier:
            donnees = json.load(fichier)

            if données_du_jeu[id_partie]["déjà_vu"][salle] == None or len(données_du_jeu[id_partie]["déjà_vu"][salle]) >= len(donnees)-1:
                données_du_jeu[id_partie]["déjà_vu"][salle] = []

            identifiant_aléatoire = nombre_aléatoire_avec_liste_à_ignorer(donnees, données_du_jeu[id_partie]["déjà_vu"][salle])
            données_du_jeu[id_partie]["déjà_vu"][salle].append(identifiant_aléatoire)

            return donnees[identifiant_aléatoire]
    raise HTTPException(status_code=404, detail="Données du jeu introuvable")


# J'ai renommé ce chemain, à modifier plus tard.
@router.get("/chercher/{salle}/{question_id}")
def salle_question_id(salle : str, question_id : int) :
    with open(chemin_questions(salle), 'r', encoding='utf-8') as fichier:
        donnees = json.load(fichier)
        if len(donnees) <= question_id :
            return ""
        return donnees[int(question_id)]


# ○----------------------------- ♣ ÉDIT QUESTION ♣ -----------------------------○

@router.post("")
def ajout_question(question : Question):
    donnees = []
    with open(chemin_questions(question.salle), 'r', encoding='utf-8') as fichier:
        donnees = json.load(fichier)
        donnees.append(question.model_dump())

    with open(chemin_questions(question.salle), 'w', encoding='utf-8') as fichier:
        json.dump(donnees, fichier, indent=4, ensure_ascii=False)
    
    return {"message": "Enregistrement réussi"}
    
@router.delete("/{id_salle}/{id_question}")
def delete_question(id_salle:int, id_question:int):
    if id_salle < 1 or id_salle > 3 :
        id_salle = 1

    fichierJSON = chemin_questions(id_salle)

    donnees = []
    with open(fichierJSON, 'r', encoding='utf-8') as fichier:
        donnees = json.load(fichier)
        if len(donnees) > id_question and id_question >= 0 :
            donnees.pop(id_question)
        else :
            raise HTTPException(status_code=404, detail=f"Cette identifiant est invalide et n'est pas dans la plage des [0, {len(donnees)}[ questions valides.")

    with open(fichierJSON, 'w', encoding='utf-8') as fichier:
        json.dump(donnees, fichier, indent=4, ensure_ascii=False)
    
    return {"message": "Supression réussi"}


@router.put("/{id_salle}/{id_question}/{nouvelle_reponse}")
def put_question_reponse(id_salle:int, id_question:int, nouvelle_reponse:int):
    if nouvelle_reponse < 1 or nouvelle_reponse > 3 :
        raise HTTPException(status_code=404, detail="La nouvelle réponse ne peut être que 1, 2 ou 3.")

    
    if id_salle < 1 or id_salle > 3 :
        id_salle = 1
    
    fichierJSON = chemin_questions(id_salle)
    
    donnees = []
    with open(fichierJSON, 'r', encoding='utf-8') as fichier:
        donnees = json.load(fichier)
        if len(donnees) > id_question and id_question >= 0 :
            donnees[id_question]["réponse"] = nouvelle_reponse
        else :
            raise HTTPException(status_code=404, detail="Cette identifiant est invalide et n'est pas dans la plage des [0, {len(donnees)}[ questions valides.")
    with open(fichierJSON, 'w', encoding='utf-8') as fichier:
        json.dump(donnees, fichier, indent=4, ensure_ascii=False)
        
    return {"message": "Modification réussie réussi"}
