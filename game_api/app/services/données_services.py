import hashlib, hmac
import random

données_du_jeu = []

données_départ = {
    "id" : "",
    "déjà_vu" : {
        "salle-1" : [],
        "salle-2" : [],
        "salle-3" : []
    },

    "players" : [],
    "id_global" : 0,
}

id_global_partie = 0

def aubtenir_un_identifiant_de_partie() :
    global id_global_partie
    données_du_jeu.append(données_départ.copy())
    message_bytes = str(id_global_partie).encode("utf-8")
    mac1 = hmac.new(b"key", msg=message_bytes, digestmod=hashlib.sha512)
    token_hex = mac1.hexdigest()
    données_du_jeu[len(données_du_jeu) - 1]["id"] = token_hex
    id_global_partie += 1
    return token_hex

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
