import requests

class Question:
    def __init__(self):
        self._la_question = ""
        self._réponseA = "" 
        self._réponseB = ""
        self._réponseC = ""
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

        baseURL = "http://127.0.0.1:8000"

        url=baseURL+url

        réponse_http = requests.get(
            url
        )

        if réponse_http.status_code == 200:
            données = réponse_http.json()
            if données != None :
                self._la_question = données["question"]
                self._réponseA = données["réponseA"]
                self._réponseB = données["réponseB"]
                self._réponseC = données["réponseC"]
                self._numéro_réponse_attendu = données["réponse"]
                self._indice = données["indice"]

    def afficher_la_question(self):
        # idRéponse = self.gestionnaire_du_jeu.nombre_de_bonne_réponse
        idRéponse = 1
        t = "\n"
        t += "==============\n"
        t +=f"  QUESTION {idRéponse} \n"
        t += "==============\n\n"
        t +=f" | Question : {self._la_question}\n\n"
        t += "Quel est le numéro de la bonne réponse ?\n"
        t +=f" > 1 - {self._réponseA}\n"
        t +=f" > 2 - {self._réponseB}\n"
        t +=f" > 3 - {self._réponseC}\n"

        # if self.gestionnaire_du_jeu.droit_à_indice > 0
        t += "\n > 0 - Voir un indice !\n"
        print(t)
        self.en_attente_de_la_réponse_du_joeur(3, True)

    def en_attente_de_la_réponse_du_joeur(self, nombreMaximum, peut_voir_indice) :
        choix = -1
        nombreMinimum = 1
        # if self.gestionnaire_du_jeu.droit_à_indice > 0:
        if peut_voir_indice :
            nombreMinimum = 0

        while choix < nombreMinimum or choix > nombreMaximum :
            choix = int(input("Votre choix : "))

        if choix != 0 :
            self.réponse_à_la_question(choix)

        # else self.gestionnaire_du_jeu.droit_à_indice > 0:
        if choix == 0 and peut_voir_indice :
            self.afficher_indice()

    def réponse_à_la_question(self, réponse:int):
        if réponse == self._numéro_réponse_attendu:
            print("\n Bravo ! C'est la bonne réponse !")
        else :
            print("\n Eh non ! Se n'est pas la bonne réponse...\nMais ne désespère pas, tu finiras par y arrivé !")

    def afficher_indice(self):
        # if self.gestionnaire_du_jeu.droit_à_indice > 0:
        #     print("\nVous ne pouvez pas voir d'indice, et oui, même en trichant, ça ne fonctionneras pas, ah ah !")
        print(f"\n | Indice : {self._indice}\n")
        self.en_attente_de_la_réponse_du_joeur(3, False)


    def __str__(self):
        t = "\nInformation sur la question :"
        t += f"\n\tQuestion : {self._la_question}"
        t += f"\n\tRéponseA : {self._réponseA}"
        t += f"\n\tRéponseB : {self._réponseB}"
        t += f"\n\tRéponseC : {self._réponseC}"
        t += f"\n\tRéponse : {self._numéro_réponse_attendu}"
        t += f"\n\tIndice : {self._indice}"
        return t


question = Question()
question.trouver_question(1)
# print(question)
question.afficher_la_question()