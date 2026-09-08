import requests

class Question:
    def __init__(self):
        self._la_question = ""
        self.réponseA = "" 
        self.réponseB = ""
        self.réponseC = ""
        self._indice = ""
        self._numéro_réponse_attendu = 0
        self.gestionnaire_du_jeu = None

    def trouver_question(self, id_partie:int):
        url = "/question/salle-"
        if id_partie == 2 :
            url += "2"
        elif id_partie == 3 :
            url += "3"
        else :
           url += "1"

        requests = requests.get("http://127.0.0.1:8000"+url)
        if requests.status_code == 200:
            données = requests.json()
            if données != None :
                self._la_question = données["question"]
                self.réponseA = données["réponseA"]
                self.réponseB = données["réponseB"]
                self.réponseC = données["réponseC"]
                self._numéro_réponse_attendu = données["réponse"]
                self._indice = données["indice"]
