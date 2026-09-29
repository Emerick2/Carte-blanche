import requests

baseURL = "http://127.0.0.1:8000"

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

    def trouver_chapitre(self, id_partie: int) -> Chapitre:
        """Renvoie le chapitre demande, ou leve ValueError s'il n'existe pas."""
        url=baseURL+"/histoire/"+str(id_partie)
        réponse_http = requests.get(
            url
        )
        
        if réponse_http.status_code == 200:
            données = réponse_http.json()
            if (données == None) :
                raise ValueError(f"Aucun chapitre pour id_partie={id_partie}")
            else :
                return données

        raise ValueError("L'API n'as pas répondu.")

    def existe(self, id_partie: int) -> bool:
        """Test sans exception, quand on veut juste savoir si la salle existe."""
        url=baseURL+"/histoire/"+str(id_partie)
        réponse_http = requests.get(
            url
        )
                
        if réponse_http.status_code == 200:
            données = réponse_http.json()
            print(données)
            return données != None

        print(réponse_http)
        return False


    def afficher_histoire(self, id_partie: int) -> str:
        """Texte d'entree de la salle demandee."""
        chapitre = self.trouver_chapitre(id_partie)
        if (chapitre != None) :
            return f"=== {chapitre["titre"]} ===\n{chapitre["texte"]}"
        return "Erreur du texte de l'histoire."

    def afficher_sortie(self, id_partie: int) -> str:
        """Texte joue quand le joueur a repondu a toutes les questions de la salle."""
        return self.trouver_chapitre(id_partie)["texte_sortie"]

    def nombre_de_salles(self) -> int:
        url=baseURL+"/histoire"
        réponse_http = requests.get(
            url
        )
                        
        if réponse_http.status_code == 200:
            données = réponse_http.json()
            if (données != None) :
                return len(données)

        return 0

    def to_dict(self, id_partie: int) -> dict:
        """Chapitre au format JSON, pret pour un endpoint FastAPI."""
        return self.trouver_chapitre(id_partie).to_dict()

