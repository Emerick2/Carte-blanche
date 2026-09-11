import json
from fastapi import FastAPI
import random
from pydantic import BaseModel, Field

app = FastAPI()

class Player(BaseModel):
    name: str = Field(min_length=3)
    score_salle_1: int = Field(ge=0)
    score_salle_2: int = Field(ge=0)
    score_salle_3: int = Field(ge=0)

données_du_jeu = []

données_départ = {
    "id" : 0,
    "déjà_vu" : {
        "salle-1" : [],
        "salle-2" : [],
        "salle-3" : []
    },

    "players" : [],
    "id_global" : 0
}

id_global_partie = 0

def identifiant_position_player(id_chercher : int, id_partie:int):
    global données_du_jeu
    id_partie = identifiant_position_partie(id_partie)
    if (id_partie != -1) :
        for i in range(len(données_du_jeu[id_partie]["players"])):
            if données_du_jeu[id_partie]["players"][i]["id"] == id_chercher :
                return i
    return -1

def identifiant_position_partie(id_chercher : int):
    for i in range(len(données_du_jeu)):
        if données_du_jeu[i]["id"] == id_chercher :
            return i
    return -1

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
    global id_global_partie
    données_du_jeu.append(données_départ)
    id_global_partie += 1
    return id_global_partie-1


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

@app.get("/question/{id_partie}/{salle}")
def salle_question(id_partie:int, salle : str) :
    global données_du_jeu
    id_partie = identifiant_position_partie(id_partie)
    if (id_partie != -1) :
        fichier_json = 'question-salle-1.json'
        if salle == "salle-2" :
            fichier_json = 'question-salle-2.json'
        elif salle == "salle-3" :
            fichier_json = 'question-salle-3.json'
        else :
            salle = "salle-1"
        
        with open(fichier_json, 'r', encoding='utf-8') as fichier:
            donnees = json.load(fichier)

            if données_du_jeu[id_partie]["déjà_vu"][salle] == None or len(données_du_jeu[id_partie]["déjà_vu"][salle]) >= len(donnees)-1:
                données_du_jeu[id_partie]["déjà_vu"][salle] = []

            identifiant_aléatoire = nombre_aléatoire_avec_liste_à_ignorer(donnees, données_du_jeu[id_partie]["déjà_vu"][salle])
            données_du_jeu[id_partie]["déjà_vu"][salle].append(identifiant_aléatoire)

            return donnees[identifiant_aléatoire]
    return {"error": "Données du jeu introuvable"}, 404
    
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


@app.get("/players/{id_partie}")
def get_players(id_partie:int):
    global données_du_jeu
    id_partie = identifiant_position_partie(id_partie)
    if (id_partie != -1) :
        return données_du_jeu[id_partie]["players"]
    return {"error": "Données du jeu introuvable"}, 404

@app.get("/players/{id_partie}/{player_id}")
def get_player(id_partie:int, player_id: int):
    global données_du_jeu
    id_partie = identifiant_position_partie(id_partie)
    if (id_partie != -1) :
        player_id = identifiant_position_player(player_id)
        if player_id != -1 :
            return données_du_jeu[id_partie]["players"][player_id]
        return {"error": "Player not found"}
    return {"error": "Données du jeu introuvable"}, 404

@app.get("/id/list/{id_partie}")
def get_list_id(id_partie:int):
    global données_du_jeu
    id_partie = identifiant_position_partie(id_partie)
    if (id_partie != -1) :
        tableau = []
        for i in range(len(données_du_jeu[id_partie]["players"])):
            tableau.append(données_du_jeu[id_partie]["players"][i]["id"])
        return tableau
    return {"error": "Données du jeu introuvable"}, 404

@app.post("/players/{id_partie}")
def create_player(player: Player, id_partie:int):
    global données_du_jeu
    id_partie = identifiant_position_partie(id_partie)
    if (id_partie != -1) :
        new_player = player.model_dump()
        new_player["id"] = id_partie["id_global"]
        id_partie["id_global"]+=1
        id_partie["players"].append(new_player)
        return new_player
    
    return {"error": "Données du jeu introuvable"}, 404

@app.delete("/players/{id_partie}/{player_id}")
def delete_player(id_partie:int,player_id: int):
    global données_du_jeu
    id_partie = identifiant_position_partie(id_partie)
    if (id_partie != -1) :
        player_id = identifiant_position_player(player_id)

        if player_id != -1 :
            données_du_jeu[id_partie]["players"].pop(player_id) 
            return {"message": f"Joueur à l'index {player_id} supprimé"}
        
        return {"error": "Joueur non trouvé"}, 404
    return {"error": "Partie non trouvé"}, 404

@app.put("/players/{id_partie}/{salle}/{player_id}/{score}")
def put_players_score(id_partie:int, salle : str, player_id:int, score:int):
    global données_du_jeu
    id_partie = identifiant_position_partie(id_partie)
    if (id_partie != -1) :
        nom_clef = 'score_salle_1'
        if salle == "salle-2" :
            nom_clef = 'score_salle_2'
        elif salle == "salle-3" :
            nom_clef = 'score_salle_3'
        else :
            salle = "salle-1"

        player_id = identifiant_position_player(player_id)

        score = max(score, 0)

        if player_id != -1 :
            données_du_jeu[id_partie]["players"][player_id][nom_clef] = score
            return {"message": f"Le score de {nom_clef} du joueur {player_id} à été mis à jours !"}

        return {"error": "Joueur non trouvé"}, 404
    return {"error": "Partie non trouvé"}, 404
