from question import *
import requests

# question = TypageSimple()
# print(question)
# question.afficher_la_question()


baseURL = "http://127.0.0.1:8000"

# def requête(url:str):
#     url = f"{baseURL}{url}"
#     response = requests.get(url)
#     print(f"Réponse : {response.text}\n")

# print(requête("/question/salle-2/liste"))


def requêtePost(url:str, ajout_question):
    url = f"{baseURL}{url}"
    response = requests.post(url, json=ajout_question)
    print(f"Réponse : {response.text}\n")

def requêteDelete(url:str):
    url = f"{baseURL}{url}"
    response = requests.delete(url)
    print(f"Réponse : {response.text}\n")

def requêtePut(url:str):
    url = f"{baseURL}{url}"
    response = requests.put(url)
    print(f"Réponse : {response.text}\n")


requêtePost("/question", {"question": "question titre", "réponseA": "réponse a", "réponseB": "réponse b", "réponseC": "réponse c", "réponse": 1, "indice": "texte indice", "salle": 1})
requêtePut("/question/1/30/3")
requêteDelete("/question/1/30")


