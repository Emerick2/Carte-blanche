import requests

baseURL = "http://127.0.0.1:8000"
débug = False

id_partie = requests.get(f"{baseURL}/").json()
if débug == True :
    print("Ma clef : "+id_partie)

def requête(url:str):
    url = f"{baseURL}{url}"
    response = requests.get(url)
    if débug == True :
        print(f"Réponse : {response.text}\n")


def ajouter_joueur(payload):
    url = f"{baseURL}/players"
    response = requests.post(url, json=payload)
    if débug == True :
        print(f"Réponse : {response.text}\n")


def supprimer_joueur(player_id:int):
    global id_partie
    url = f"{baseURL}/players/{id_partie}/{player_id}"
    response = requests.delete(url)
    if débug == True :
        print(f"Réponse : {response.text}\n")
    

def modifier_score_joueur(salle:str, player_id:int, player_score:int):
    global id_partie
    url = f"{baseURL}/players/{id_partie}/{salle}/{player_id}/{player_score}"
    response = requests.put(url)
    if débug == True :
        print(f"Réponse : {response.text}\n")

# Pour le post :
# ajouter_joueur({"name": "Nom1", "score_salle_1": 0, "score_salle_2": 0, "score_salle_3": 0, "id_partie" : id_partie})
# ajouter_joueur({"name": "Nom2", "score_salle_1": 0, "score_salle_2": 0, "score_salle_3": 0, "id_partie" : id_partie})
# ajouter_joueur({"name": "Nom3", "score_salle_1": 0, "score_salle_2": 0, "score_salle_3": 0, "id_partie" : id_partie})

# # Pour le get :
# print(requête(f"/players/{id_partie}/2"))
# print(requête(f"/players/{id_partie}"))
# print(requête(f"/players/{id_partie}/1"))
# print(requête(f"/id/list/{id_partie}"))




# # Pour le delete :
# supprimer_joueur(2)

# # Pour le put :
# modifier_score_joueur("salle-1",1,20)

url = f"{baseURL}/question"
payload = {
    "question": "A SUPRIMER",
    "réponseA": "C'est le 1",
    "réponseB": "Comme la réponse A",
    "réponseC": "Réponse = 3%2 ☺",
    "réponse": 1,
    "indice": "C'est UN nombre, UN !",
    "salle":1
},
response = requests.post(url, json=payload)
print(response.json())

def ajouter_joueur_action():
    print("||   ♫ Bienvenu ! ♪   ||")
    print("[?]  Combien de joueur vons jouer ? [1 - 50]")
    nombre = 0
    while (nombre <= 0 or nombre > 50):
        nombre = int(input("> "))
    print("\n • - • - • - • - • - • - • - • \n")
    for i in range(1, nombre+1):
        print(f"Bienvenu joueur {nombre} ! \n[?]  Comment te nomme tu ?")
        nom = ""
        while (len(nom) < 3 or len(nom) > 20):
            nom = input("> ")
        ajouter_joueur({"name": nom, "score_salle_1": 0, "score_salle_2": 0, "score_salle_3": 0, "id_partie" : id_partie})
        print("\n • - • - • - • - • - • - • - • \n")

ajouter_joueur_action()