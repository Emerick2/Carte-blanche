import json
from fastapi import APIRouter, HTTPException
from app.services.données_services import données_du_jeu, identifiant_position_partie, nombre_aléatoire_avec_liste_à_ignorer
from app.models.question import Question
from app.services.question_service import modification_reponse_question, suppresion_question, ajout_question, chemin_questions

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

@router.get("/chercher/{salle}/{question_id}")
def salle_question_id(salle : str, question_id : int) :
    with open(chemin_questions(salle), 'r', encoding='utf-8') as fichier:
        donnees = json.load(fichier)
        if len(donnees) <= question_id :
            return ""
        return donnees[int(question_id)]


# ○----------------------------- ♣ ÉDIT QUESTION ♣ -----------------------------○

@router.post("")
def post_question(question : Question):
    réponse_api : str = ajout_question(question)
    if réponse_api != "" :
        raise HTTPException(status_code=404, detail=réponse_api)
    
    return {"message": "Enregistrement réussi"}
    
@router.delete("/{id_salle}/{id_question}")
def delete_question(id_salle:int, id_question:int):
    réponse_api : str = suppresion_question(id_salle, id_question)
    if réponse_api != "" :
        raise HTTPException(status_code=404, detail=réponse_api)
    
    return {"message": "Supression réussi"}


@router.put("/{id_salle}/{id_question}/{nouvelle_reponse}")
def put_question_reponse(id_salle:int, id_question:int, nouvelle_reponse:int):
    if nouvelle_reponse < 1 or nouvelle_reponse > 3 :
        raise HTTPException(status_code=404, detail="La nouvelle réponse ne peut être que 1, 2 ou 3.")

    réponse_api : str = modification_reponse_question(id_salle, id_question, nouvelle_reponse)
    if réponse_api != "" :
        raise HTTPException(status_code=404, detail=réponse_api)
       
    return {"message": "Modification réussie réussi"}
