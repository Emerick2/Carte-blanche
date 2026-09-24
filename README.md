# Carte-blanche

# Lancer le projet :
Ouvrir l'API :
```bash
fastapi dev api.py
```

Démarrer le jeu :
```bash
python ./app/domain/GestionnaireDuJeu.py
```

# Lancer les tests :
```bash
./test.sh
```

# Instalation nécessaire :
```bash
conda install fastapi
conda install requests
conda install random
conda install json
conda install abc
```


# Routes de l'API :
### Routes générales :
- @app.get("/")
> Permet de récupérer l'identifiant de partie

### Routes liée aux questions :
- @app.get("/question/{salle}/liste")
> Permet de voir toutes les questions d'une salle.

- @app.get("/question/{id_partie}/{salle}")
> Permet de voir une question pseudo-aléatoire d'une salle.

- @app.get("/question/chercher/{salle}/{question_id}")
> Permet de voir une question en particulier d'une salle.

### Routes liée à la gestion des joueurs :
- @app.get("/players/{id_partie}")
> Voir la liste de tous les joueur de la partie.

- @app.get("/players/{id_partie}/{player_id}")
> Voir un joueur en particulier de la partie.

- @app.get("/id/list/{id_partie}")
> Afficher la liste des identifiants des joueurs existants dans la partie.

- @app.post("/players")
> Ajouter un joueur dans la partie (prend en paramètre un objet de type "Player").
Structure d'un joueur (Player) :
```python
name: str = Field(min_length=3)
score_salle_1: int = Field(ge=0)
score_salle_2: int = Field(ge=0)
score_salle_3: int = Field(ge=0)
id_partie: str
```

- @app.delete("/players/{id_partie}/{player_id}")
> Supprimer un joueur de la partie.

- @app.put("/players/{id_partie}/{salle}/{player_id}/{score}")
> Modifier le score d'une salle du jeu.

### Routes liée à la gestion des gestion :
- @app.post("/question")
> Cela permet d'ajouter une question dans la liste des question.

Structure d'une question :
```python
question: str = Field(min_length=5)
réponseA: str = Field(min_length=3)
réponseB: str = Field(min_length=3)
réponseC: str = Field(min_length=3)
réponse: int = Field(ge=0)
indice: str = Field(min_length=5)
salle: int = Field(ge=1)
```

- @app.delete("/question/{id_salle}/{id_question}")
> Cela permet de supprimer la question sélectionné.

- @app.put("/question/{id_salle}/{id_question}/{nouvelle_reponse}")
> Cela permet de modifier le numéro de réponse à la question.


### Routes liée à l'histoire :
- @app.get("/histoire")
> Lire tout le dossier de l'histoire.

- @app.get("/histoire/{id_histoire}")
> Lire un chapitre de l'histoire en fonction de son identifiant.

- @app.get("/histoire/{id_histoire}/sortie")
> Lire la fin du chapitre de l'histoire en fonction de l'identifiant de son chapitre.



