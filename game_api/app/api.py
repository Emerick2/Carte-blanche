from fastapi import FastAPI, HTTPException
from app.routers.player import router as players_router
from app.routers.question import router as question_router
from app.services.données_services import aubtenir_un_identifiant_de_partie
import json
from pathlib import Path

app = FastAPI(
    title='API du cauchemar de Python',
    description='API du jeu dans lequel nous jouons à programmer en Python.',
    version='1.0.0'
)

app.include_router(players_router)
app.include_router(question_router)

@app.get("/")
def début() :
    return aubtenir_un_identifiant_de_partie()


# Je ne divise pas l'histoire puisque son API est en cours de réalisation, il faudras revenir pour le faire ulterieurement :

CHEMIN_HISTOIRE = Path("app/data/histoire.json")

@app.get("/histoire")
def obtenir_histoire():
    with open(CHEMIN_HISTOIRE, "r", encoding="utf-8") as fichier:
        return json.load(fichier)
    
@app.get("/histoire/{id_histoire}")
def obtenir_chapitre(id_histoire: int):
    histoire = obtenir_histoire()

    for chapitre in histoire:
        if chapitre["id"] == id_histoire:
            return chapitre
    raise HTTPException(status_code=404, detail="Cette histoire n'existe pas")

@app.get("/histoire/{id_histoire}/sortie")
def obtenir_sortie(id_histoire: int):
    chapitre = obtenir_chapitre(id_histoire)
    return {
        "id": chapitre["id"],
        "texte_sortie": chapitre["texte_sortie"]
    }