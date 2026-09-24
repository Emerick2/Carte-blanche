from abc import ABC, abstractmethod
import hashlib, hmac
import requests
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..GestionnaireDuJeu import GestionnaireDuJeu

baseURL = "http://127.0.0.1:8000"

class Question(ABC):
    def __init__(self, id_partie:str, idRéponse:int):
        self._la_question = ""
        self._réponseA = "" 
        self._réponseB = ""
        self._réponseC = ""
        self._indice = ""
        self.__numéro_réponse_attendu = 0
        self._numéro_réponse_attendu_cripté = ""
        self.gestionnaire_du_jeu: "GestionnaireDuJeu | None" = None
        self.id_partie = id_partie
        self.idRéponse = idRéponse
        

    def trouver_question(self, id_salle:int):
        global baseURL

        url = f"/question/{self.id_partie}/salle-"
        if id_salle == 2 :
            url += "2"
        elif id_salle == 3 :
            url += "3"
        else :
           url += "1"

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

                self.__numéro_réponse_attendu = données["réponse"]
                message_cripté = str(self.__numéro_réponse_attendu).encode("utf-8")
                self._numéro_réponse_attendu_cripté = hmac.new(b"key", msg=message_cripté, digestmod=hashlib.sha512)
                
                self._indice = données["indice"]

    @abstractmethod
    def afficher_la_question(self):
        pass

    def en_attente_de_la_réponse_du_joeur(self, nombreMaximum, peut_voir_indice) :
        choix = -1
        nombreMinimum = 1
        # if self.gestionnaire_du_jeu.droit_à_indice > 0:
        if peut_voir_indice :
            nombreMinimum = 0

        while choix < nombreMinimum or choix > nombreMaximum :
            choix = int(input("Votre choix : "))

        if choix != 0 :
            if self.gestionnaire_du_jeu == None :
                print("Le gestionnaire du jeu n'est pas valide.")
                # self.réponse_à_la_question(choix)
            else :
                self.gestionnaire_du_jeu.verification_reponse(choix)

        # else self.gestionnaire_du_jeu.droit_à_indice > 0:
        if choix == 0 and peut_voir_indice :
            self.afficher_indice()

    def réponse_à_la_question(self, réponse:int):
        message_cripté = str(réponse).encode("utf-8")
        réponse_cripté = hmac.new(b"key", msg=message_cripté, digestmod=hashlib.sha512)
        if réponse_cripté.digest() == self._numéro_réponse_attendu_cripté.digest():
            print("\n Bravo ! C'est la bonne réponse !")
            return True
        else :
            print(f"\n Eh non ! Ce n'est pas la bonne réponse... C'était le {self.__numéro_réponse_attendu}.\nMais ne désespère pas, tu finiras par y arrivé !")
            return False

    def afficher_indice(self):
        # if self.gestionnaire_du_jeu.droit_à_indice > 0:
        #     print("\nVous ne pouvez pas voir d'indice, et oui, même en trichant, ça ne fonctionneras pas, ah ah !")
        print(f"\n | Indice : {self._indice}\n")
        self.en_attente_de_la_réponse_du_joeur(3, False)


    def __str__(self):
        t = "\nInformation sur la question :"
        t += f"\n\tQuestion : {self._la_question}"
        t += f"\n\tRéponse A : {self._réponseA}"
        t += f"\n\tRéponse B : {self._réponseB}"
        t += f"\n\tRéponse C : {self._réponseC}"
        t += f"\n\tRéponse : {self.__numéro_réponse_attendu}"
        t += f"\n\tIndice : {self._indice}"
        return t



















