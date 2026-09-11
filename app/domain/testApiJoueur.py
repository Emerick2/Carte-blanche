import requests

baseURL = "http://127.0.0.1:8000"
id_partie = requests.get(f"{baseURL}/").json()

def requête(url:str):
    url = f"{baseURL}{url}"
    response = requests.get(url)
    print(f"Réponse : {response.text}\n")


def ajouter_joueur(payload):
    url = f"{baseURL}/players/{id_partie}"
    response = requests.post(url, json=payload)
    print(f"Réponse : {response.text}\n")


def supprimer_joueur(player_id:int):
    url = f"{baseURL}/players/{id_partie}/{player_id}"
    response = requests.delete(url)
    print(f"Réponse : {response.text}\n")
    

def modifier_score_joueur(salle:str, player_id:int, player_score:int):
    url = f"{baseURL}/players/{id_partie}/{salle}/{player_id}/{player_score}"
    response = requests.put(url)
    print(f"Réponse : {response.text}\n")

# Pour le post :
# ajouter_joueur({"name": "Nom1", "score_salle_1": 0, "score_salle_2": 0, "score_salle_3": 0})
# ajouter_joueur({"name": "Nom2", "score_salle_1": 0, "score_salle_2": 0, "score_salle_3": 0})
# ajouter_joueur({"name": "Nom3", "score_salle_1": 0, "score_salle_2": 0, "score_salle_3": 0})

# # Pour le get :
print(requête(f"/players/{id_partie}/2"))
# print(requête(f"/players/{id_partie}/1"))
# print(requête(f"/players/{id_partie}"))
# print(requête(f"/id/list/{id_partie}"))




# # Pour le delete :
# supprimer_joueur(2)

# # Pour le put :
# modifier_score_joueur("salle-1",1,20)
