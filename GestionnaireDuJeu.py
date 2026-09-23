from Question import Question

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

    def nouvelle_question(self): 
        quest = Question() 
        self._question = quest.trouver_question(self._partie) 

    def verification_reponse(self, reponse_joueur): 
        if self._question.réponse_a_la_question(reponse_joueur) : 
            if self._partie == 1 :
                self._score1 += 1
            elif self._partie == 2 :
                self._score2 += 1 
            elif self._partie == 3 :
                self._score3 += 1

    def commencer_la_partie(self) : 
        self.nouvelle_question()



 
        

# _numéro_partie → _partie
# _nombre_bonne_réponse_total_partie_1 → _score_1
# _nombre_bonne_réponse_total_partie_2 → _score_2
# _nombre_bonne_réponse_total_partie_3 → _score_3
# _nombre_bonne_réponse → _score_total
# droit_à_indice → _indices
# question → _question
# id_partie_histoire → _id_histoire