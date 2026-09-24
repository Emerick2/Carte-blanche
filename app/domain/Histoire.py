
import json
from pathlib import Path


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


class Histoire:
    """Recueil des chapitres. Retrouve le bon texte a partir d'un id_partie.

    Responsabilite : chercher et formater. Ne stocke pas le contenu d'une salle
    (c'est le role de Chapitre).
    """

    def __init__(self, chapitres: list[Chapitre] | None = None) -> None:
        if chapitres is None:
            chemin = Path(__file__).parents[1] / "data" / "histoire.json"
            with chemin.open(encoding="utf-8") as fichier:
                données = json.load(fichier)
            chapitres = [
                Chapitre(
                    id_partie=chapitre["id"],
                    titre=chapitre["titre"],
                    texte=chapitre["texte"],
                    texte_sortie=chapitre["texte_sortie"],
                )
                for chapitre in données
            ]

        self._chapitres: dict[int, Chapitre] = {c.id_partie: c for c in chapitres}

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

