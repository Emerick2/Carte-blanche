from fastapi import APIRouter, HTTPException
from app.models.player import Player
from app.services.données_services import données_du_jeu, identifiant_position_partie
from app.services.player_service import identifiant_position_player
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='api.log', encoding='utf-8', level=logging.DEBUG)

router = APIRouter(
    prefix='/players',
    tags=['players'],
)

@router.get("/{id_partie}")
def get_players(id_partie:str):
    global données_du_jeu
    id_partie = identifiant_position_partie(id_partie)
    if (id_partie != -1) :
        logger.info('La liste des joueurs de la partie à été envoyé')
        return données_du_jeu[id_partie]["players"]

    logger.warning("Données du jeu introuvable")
    raise HTTPException(status_code=404, detail="Données du jeu introuvable")

@router.get("/{id_partie}/{player_id}")
def get_player(id_partie:str, player_id: int):
    global données_du_jeu
    index_partie = identifiant_position_partie(id_partie)
    if (index_partie != -1) :
        index_player = identifiant_position_player(player_id, id_partie)
        if index_player != -1 :
            logger.info('Un joueur à été envoyé')
            return données_du_jeu[index_partie]["players"][index_player]
        logger.warning("Joueur non trouvé")
        raise HTTPException(status_code=404, detail="Joueur non trouvé")
    logger.warning("Données du jeu introuvable")
    raise HTTPException(status_code=404, detail="Données du jeu introuvable")

@router.get("/id/list/{id_partie}")
def get_list_id(id_partie:str):
    global données_du_jeu
    id_partie = identifiant_position_partie(id_partie)
    if (id_partie != -1) :
        tableau = []
        for i in range(len(données_du_jeu[id_partie]["players"])):
            tableau.append(données_du_jeu[id_partie]["players"][i]["id"])
        logger.info('La liste des identifiants de joueurs à été affiché')
        return tableau
    logger.warning("Données du jeu introuvable")
    raise HTTPException(status_code=404, detail="Données du jeu introuvable")

@router.post("")
def create_player(player: Player):
    global données_du_jeu
    new_player = player.model_dump()
    id_partie = new_player["id_partie"]
    id_partie = identifiant_position_partie(id_partie)
    if (id_partie != -1) :
        new_player["id"] = données_du_jeu[id_partie]["id_global"]
        données_du_jeu[id_partie]["id_global"]+=1
        données_du_jeu[id_partie]["players"].append(new_player)
        logger.info('Un joueur à été créé.')
        return new_player

    logger.warning("Données du jeu introuvable")
    raise HTTPException(status_code=404, detail="Données du jeu introuvable")

@router.delete("/{id_partie}/{player_id}")
def delete_player(id_partie:str,player_id: int):
    global données_du_jeu
    index_partie = identifiant_position_partie(id_partie)
    if (index_partie != -1) :
        index_player = identifiant_position_player(player_id, id_partie)

        if index_player != -1 :
            données_du_jeu[index_partie]["players"].pop(index_player)
            logger.info('Un joueur à été supprimé')
            return {"message": f"Joueur à l'index {index_player} supprimé"}

        logger.warning("Joueur non trouvé")
        raise HTTPException(status_code=404, detail="Joueur non trouvé")
    logger.warning("Données du jeu introuvable")
    raise HTTPException(status_code=404, detail="Données du jeu introuvable")

@router.put("/{id_partie}/{salle}/{player_id}/{score}")
def put_players_score(id_partie:str, salle : str, player_id:int, score:int):
    global données_du_jeu
    index_partie = identifiant_position_partie(id_partie)
    if (index_partie != -1) :
        nom_clef = 'score_salle_1'
        if salle == "salle-2" :
            nom_clef = 'score_salle_2'
        elif salle == "salle-3" :
            nom_clef = 'score_salle_3'
        else :
            salle = "salle-1"

        index_player = identifiant_position_player(player_id, id_partie)

        score = max(score, 0)

        if index_player != -1 :
            données_du_jeu[index_partie]["players"][index_player][nom_clef] = score
            logger.info("Le score d'un joueur à été modifié")
            return {"message": f"Le score de {nom_clef} du joueur {index_player} à été mis à jours !"}

        logger.warning("Joueur non trouvé")
        raise HTTPException(status_code=404, detail="Joueur non trouvé")
    logger.warning("Données du jeu introuvable")
    raise HTTPException(status_code=404, detail="Données du jeu introuvable")
