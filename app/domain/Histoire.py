
class Chapitre:
    """Le texte narratif d'UNE salle du cauchemar.

    Responsabilite : stocker les donnees d'une salle. Ne cherche rien, n'affiche rien.
    """

    def __init__(
        self,
        id_partie: int,
        titre: str,
        texte: str,
        texte_sortie: str = "",
    ) -> None:
        self.id_partie = id_partie
        self.titre = titre
        self.texte = texte          # texte joue a l'entree de la salle
        self.texte_sortie = texte_sortie  # texte joue quand la porte s'ouvre

    def resume(self) -> str:
        """Ligne courte pour les menus et les logs. Ex: '[1] Salle 1'."""
        return f"[{self.id_partie}] {self.titre}"

    def to_dict(self) -> dict:
       
        return {
            "id_partie": self.id_partie,
            "titre": self.titre,
            "texte": self.texte,
            "texte_sortie": self.texte_sortie,
        }

    def __repr__(self) -> str:
       
        return f"Chapitre({self.id_partie}, {self.titre!r})"


CHAPITRES_PAR_DEFAUT: list[Chapitre] = [
    Chapitre(
        id_partie=0,
        titre="Le reveil impossible",
        texte=(
            "Tu t'endors devant ton cours de Python... et tu ne te reveilles pas.\n"
            "Tu ouvres les yeux dans une piece sans fenetre. La porte est verrouillee.\n"
            "Une voix resonne : \"Reponds a mes questions, ou reste ici pour toujours.\""
        ),
        texte_sortie="Le verrou claque. La premiere porte s'ouvre lentement.",
    ),
    Chapitre(
        id_partie=1,
        titre="Salle 1 - Les fondations",
        texte=(
            "Salle 1. Des variables flottent dans l'air comme des lucioles.\n"
            "Les questions portent sur les bases du langage : types, syntaxe, valeurs."
        ),
        texte_sortie="Les lucioles s'eteignent. Un couloir sombre apparait vers la salle 2.",
    ),
    Chapitre(
        id_partie=2,
        titre="Salle 2 - Le typage",
        texte=(
            "Salle 2. Les murs sont couverts d'annotations : int, str, list[int], Optional.\n"
            "Ici, une erreur de type peut te couter ton reveil."
        ),
        texte_sortie="Les annotations se figent en vert. La derniere porte grince.",
    ),
    Chapitre(
        id_partie=3,
        titre="Salle 3 - La POO",
        texte=(
            "Salle 3, la derniere. Des classes geantes tournent autour de toi :\n"
            "heritage, polymorphisme, methodes abstraites. Le cauchemar joue sa derniere carte."
        ),
        texte_sortie=(
            "Tu ouvres les yeux. Ton clavier est encore chaud.\n"
            "Tu t'es reveille. Fin du cauchemar."
        ),
    ),
]


class Histoire:
    """Recueil des chapitres. Retrouve le bon texte a partir d'un id_partie.

    Responsabilite : chercher et formater. Ne stocke pas le contenu d'une salle
    (c'est le role de Chapitre).
    """

    def __init__(self, chapitres: list[Chapitre] | None = None) -> None:
      
        source = chapitres if chapitres is not None else CHAPITRES_PAR_DEFAUT

        self._chapitres: dict[int, Chapitre] = {c.id_partie: c for c in source}

    def trouver_chapitre(self, id_partie: int) -> Chapitre:
        """Renvoie le chapitre demande, ou leve ValueError s'il n'existe pas."""
        if id_partie not in self._chapitres:
            raise ValueError(f"Aucun chapitre pour id_partie={id_partie}")
        return self._chapitres[id_partie]

    def existe(self, id_partie: int) -> bool:
        """Test sans exception, quand on veut juste savoir si la salle existe."""
        return id_partie in self._chapitres


    def afficher_histoire(self, id_partie: int) -> str:
        """Texte d'entree de la salle demandee."""
        chapitre = self.trouver_chapitre(id_partie)
        return f"=== {chapitre.titre} ===\n{chapitre.texte}"

    def afficher_sortie(self, id_partie: int) -> str:
        """Texte joue quand le joueur a repondu a toutes les questions de la salle."""
        return self.trouver_chapitre(id_partie).texte_sortie

    def lister(self) -> list[str]:
        """Resumes de tous les chapitres, dans l'ordre des id."""
        resumes: list[str] = []
        for id_partie in sorted(self._chapitres):
            resumes.append(self._chapitres[id_partie].resume())
        return resumes

    def nombre_de_salles(self) -> int:
        return len(self._chapitres)

    def to_dict(self, id_partie: int) -> dict:
        """Chapitre au format JSON, pret pour un endpoint FastAPI."""
        return self.trouver_chapitre(id_partie).to_dict()


# ---------------------------------------------------------------------------
# Demonstration manuelle : python3 app/domain/histoire.py
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    histoire = Histoire()

    print(f"Nombre de salles : {histoire.nombre_de_salles()}\n")

    for ligne in histoire.lister():
        print(ligne)

    print()
    print(histoire.afficher_histoire(0))
    print()
    print(histoire.afficher_sortie(0))

    print("\n--- Cas d'erreur ---")
    try:
        histoire.afficher_histoire(99)
    except ValueError as erreur:
        print(f"ValueError attrapee : {erreur}")