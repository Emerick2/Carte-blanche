from fastapi import FastAPI
from app.routers.player import router as players_router
from app.routers.question import router as question_router
from app.routers.histoire import router as histoire_router
from app.services.données_services import aubtenir_un_identifiant_de_partie


app = FastAPI(
    title='API du cauchemar de Python',
    description='API du jeu dans lequel nous jouons à programmer en Python.',
    version='1.0.0'
)

app.include_router(players_router)
app.include_router(question_router)
app.include_router(histoire_router)

@app.get("/")
def début() :
    return aubtenir_un_identifiant_de_partie()
