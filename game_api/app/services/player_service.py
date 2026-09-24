from app.services.données_services import identifiant_position_partie
from app.services.données_services import données_du_jeu

def identifiant_position_player(id_chercher : int, id_partie:str):
    global données_du_jeu
    id_partie = identifiant_position_partie(id_partie)
    if (id_partie != -1) :
        for i in range(len(données_du_jeu[id_partie]["players"])):
            if données_du_jeu[id_partie]["players"][i]["id"] == id_chercher :
                return i
    return -1

