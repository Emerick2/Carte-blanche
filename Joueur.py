class Joueur:
    def __init__(self):
        self.gestionnaire_du_jeu = None
        self._position_x_joueur = 0
        self._position_y_joueur = 0

    @property
    def position_x_joueur(self) -> int:
        return self._position_x_joueur

    def set_position_x_joueur(self, valeur:int):
        self._position_x_joueur = valeur

    @property
    def position_y_joueur(self) -> int:
        return self._position_y_joueur
    
    def set_position_y_joueur(self, valeur:int):
        self._position_y_joueur = valeur

    def position_initiale(self, x:int, y:int):
        self.set_position_x_joueur(x)
        self.set_position_y_joueur(y)

    def déplacer_joueur(self, x:int, y:int):
        # if self.gestionnaire_du_jeu != None && self.gestionnaire_du_jeu.case_libre(self.position_x_joueur+x, self.position_y_joueur+y):
        self.set_position_x_joueur(self.position_x_joueur+x)
        self.set_position_y_joueur(self.position_y_joueur+y)

    def changer_couleur_joueur(self):
        # if self.gestionnaire_du_jeu != None :
        # self.intervertir_couleur()
        # Ici, on changeras la couleur du joueur
        pass

    def __str__(self) :
        return f"Position : ({self._position_x_joueur} ; {self._position_y_joueur})"


joueur = Joueur()
print(joueur)
joueur.position_initiale(5,20)
print(joueur)

joueur.déplacer_joueur(1,0)
print(joueur)
