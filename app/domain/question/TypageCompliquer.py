from .Question import Question

class TypageCompliquer(Question):
    def __init__(self) :
        super().__init__()
        self.trouver_question(2)

    def afficher_la_question(self):
        # idRéponse = self.gestionnaire_du_jeu.nombre_de_bonne_réponse
        idRéponse = 1
        t = "\n"
        t += "  *  *  *  *\n"
        t += "==============\n"
        t +=f"  QUESTION {idRéponse} \n"
        t += "==============\n\n"
        t += "  *  *  *  *\n"
        t +=f" | Question : {self._la_question}\n\n"
        t += "Quel est le numéro de la bonne réponse ?\n"
        t +=f" > 1 - {self._réponseA}\n"
        t +=f" > 2 - {self._réponseB}\n"
        t +=f" > 3 - {self._réponseC}\n"
    
        # if self.gestionnaire_du_jeu.droit_à_indice > 0
        t += "\n > 0 - Voir un indice !\n"
        print(t)
        self.en_attente_de_la_réponse_du_joeur(3, True)

    def __str__(self):
        return super().__str__() + "\n\tType : Typage compliquer."