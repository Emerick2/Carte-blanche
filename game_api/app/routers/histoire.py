from fastapi import APIRouter, HTTPException
import logging
import json
from pathlib import Path

logger = logging.getLogger(__name__)
logging.basicConfig(filename='api.log', encoding='utf-8', level=logging.DEBUG)

router = APIRouter(
    prefix='/histoire',
    tags=['histoire'],
)

CHEMIN_HISTOIRE = Path("../../../app/data/histoire.json")

@router.get("")
def obtenir_histoire():
    with open(CHEMIN_HISTOIRE, "r", encoding="utf-8") as fichier:
        return json.load(fichier)
    
@router.get("/{id_histoire}")
def obtenir_chapitre(id_histoire: int):
    histoire = obtenir_histoire()

    for chapitre in histoire:
        if chapitre["id"] == id_histoire:
            return chapitre
        
    raise HTTPException(status_code=404, detail="Cette histoire n'existe pas")

@router.get("/{id_histoire}/sortie")
def obtenir_sortie(id_histoire: int):
    chapitre = obtenir_chapitre(id_histoire)
    return {
        "id": chapitre["id"],
        "texte_sortie": chapitre["texte_sortie"]
    }