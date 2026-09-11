# Carte-blanche
Il s’agit d’un jeu dans lequel nous incarnons une carte blanche qui doit trouver son chemin dans un étrange labyrinthe… Mais pour l’aider, elle a la possibilité de changer de face et cela fait radicalement changer le décor autour d’elle !  Parviendrez-vous à vous échapper de ce labyrinthe ?

# Lancer le projet :
Ouvrir l'API :
```bash
fastapi dev main.py
```

Ouvrir l'environnement de test :
```bash
python testQuestion.py
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

- @app.get("/question/{salle}/{question_id}")
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

- @app.delete("/players/{id_partie}/{player_id}")
> Supprimer un joueur de la partie.

- @app.put("/players/{id_partie}/{salle}/{player_id}/{score}")
> Modifier le score d'une salle du jeu.



















