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

déjà_vu = {
    "salle-1" : [],
    "salle-2" : [],
    "salle-3" : []
}

players = []
id_global = 0

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

def identifiant_position_player(id_chercher : int):
    for i in range(len(players)):
        if players[i]["id"] == id_chercher :
            return i
    return -1

@app.get("/players")
def get_players():
    return players

@app.get("/players/{player_id}")
def get_player(player_id: int):
    player_id = identifiant_position_player(player_id)
    if player_id != -1 :
        return players[player_id]
    return {"error": "Player not found"}

@app.get("/id/list")
def get_list_id():
    tableau = []
    for i in range(len(players)):
        tableau.append(players[i]["id"])
    return tableau

@app.post("/players")
def create_player(player: Player):
    global id_global, players
    new_player = player.model_dump()
    new_player["id"] = id_global
    id_global+=1
    players.append(new_player)
    return new_player

@app.delete("/players/{player_id}")
def delete_player(player_id: int):
    global players
    player_id = identifiant_position_player(player_id)

    if player_id != -1 :
        players.pop(player_id) 
        return {"message": f"Joueur à l'index {player_id} supprimé"}
    
    return {"error": "Joueur non trouvé"}, 404

@app.put("/players/score/{player_id}/{score}")
def put_players_score(player_id:int, score:int):
    player_id = identifiant_position_player(player_id)

    if player_id != -1 :
        players[player_id]["score"] = score
        return {"message": "Le score du joueur à été mis à jours !"}
                
    return {"error": "Joueur non trouvé"}, 404

@app.put("/players/level/{player_id}/{level}")
def put_player_level(player_id:int, level:int):
    player_id = identifiant_position_player(player_id)

    if player_id != -1 :
        players[player_id]["level"] = level
        return {"message": "Le niveau du joueur à été mis à jours !"}

    return {"error": "Joueur non trouvé"}, 404