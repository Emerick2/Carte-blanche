from app.domain.question.Question import Question
from app.domain.Histoire import Histoire

class GestionnaireDuJeu : 
    def __init__(self) :
        self._partie = 1 
        self._score1 = 0
        self._score2 = 0 
        self._score3 = 0
        self._scoreTotal = 0 
        self._indices = 3
        self._idHistoire = 0 
        self._question :Question = None
        self._questions_posees = 0
        self._questions_par_salle = 4

    def nouvelle_question(self): 
        quest = Question() 
        self._question = quest.trouver_question(self._partie) 
        self._questions_posees += 1

    def verification_reponse(self, reponse_joueur): 
        if self._question.réponse_à_la_question(reponse_joueur) : 
            if self._partie == 1 :
                self._score1 += 1
            elif self._partie == 2 :
                self._score2 += 1 
            elif self._partie == 3 :
                self._score3 += 1

    def commencer_la_partie(self) : 
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
