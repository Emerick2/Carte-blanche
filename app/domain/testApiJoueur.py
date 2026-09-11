import requests

baseURL = "http://127.0.0.1:8000"

def requête(url:str):
    url = f"{baseURL}{url}"
    response = requests.get(url)
    print(f"Réponse : {response.text}\n")


def ajouter_joueur(payload):
    url = f"{baseURL}/players"
    response = requests.post(url, json=payload)
    print(f"Réponse : {response.text}\n")


def supprimer_joueur(player_id:int):
    url = f"{baseURL}/players/{player_id}"
    response = requests.delete(url)
    print(f"Réponse : {response.text}\n")
    

def modifier_score_joueur(salle:str, player_id:int, player_score:int):
    url = f"{baseURL}/players/{salle}/{player_id}/{player_score}"
    response = requests.put(url)
    print(f"Réponse : {response.text}\n")

# Pour le post :
ajouter_joueur({"name": "Nom1", "score_salle_1": 0, "score_salle_2": 0, "score_salle_3": 0})
ajouter_joueur({"name": "Nom2", "score_salle_1": 0, "score_salle_2": 0, "score_salle_3": 0})
ajouter_joueur({"name": "Nom3", "score_salle_1": 0, "score_salle_2": 0, "score_salle_3": 0})

# Pour le get :
print(requête("/players/2"))
print(requête("/players/1"))
print(requête("/players"))
print(requête("/id/list"))




# Pour le delete :
supprimer_joueur(2)

# Pour le put :
modifier_score_joueur("salle-1",1,20)
