from Histoire import Histoire
import requests
from question import *

class GestionnaireDuJeu : 
    def __init__(self) :
        self._partie = 1 
        self._score1 = 0
        self._score2 = 0 
        self._score3 = 0
        self._total1 = 0
        self._total2 = 0 
        self._total3 = 0
        self._scoreTotal = 0 
        self._indices = 3
        self._idHistoire = 0 
        self._question :Question = None
        self._questions_posees = 0
        self._questions_par_salle = 4
        self.id_partie = ""
        self.baseURL = "http://127.0.0.1:8000"

    def nouvelle_question(self): 
        self.quest : Question = None
        if self._partie == 1 :
            self.quest = TypageSimple(self.id_partie, self._total1+1)
        elif self._partie == 2 :
            self.quest = TypageCompliquer(self.id_partie, self._total2+1)
        elif self._partie == 3 :
            self.quest = ErreurFonction(self.id_partie, self._total3+1)
        else : 
            print("Le numéro de la partie est invalide.")
            return

        if (self.quest != None) :
            self.quest.gestionnaire_du_jeu = self
            self._question = self.quest
            self.quest.afficher_la_question()
            self._questions_posees += 1
        else :
            print("La question était invalide.")

    def verification_reponse(self, reponse_joueur): 
        if self._partie == 1 :
            self._total1 += 1
        elif self._partie == 2 :
            self._total2 += 1 
        elif self._partie == 3 :
            self._total3 += 1
        
        if self._question.réponse_à_la_question(reponse_joueur) : 
            if self._partie == 1 :
                self._score1 += 1
            elif self._partie == 2 :
                self._score2 += 1 
            elif self._partie == 3 :
                self._score3 += 1

        self.nouvelle_question()

    def commencer_la_partie(self) : 
        self.id_partie = requests.get(f"{self.baseURL}/").json()
        hist = Histoire() 
        self.nouvelle_question()
        return hist.afficher_histoire(0) 

    def verification_salle(self) :
        hist = Histoire()
        if self._questions_posees == self._questions_par_salle :
            texte_sortie = hist.afficher_sortie(self._partie)
            self._partie += 1
            if self._partie == 4 :
                self._scoreTotal = self._score1 + self._score2 + self._score3
                return texte_sortie + str(self._scoreTotal)
            else :
                texte_entrée = hist.afficher_histoire(self._partie)
            self._questions_posees = 0 
            return texte_sortie + texte_entrée


g = GestionnaireDuJeu()
g.commencer_la_partie()