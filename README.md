# PyCauchemar
PyCauchemar est un jeu réalisé en Python FastAPI dans lequel le joueur est coincé dans ses cauchemars. Il vous faudra donc réussir votre évaluation de Python pour parvenir à finir votre cauchemar et enfin passer une bonne nuit.

## Lancer le projet :
Ouvrir l'API :
```bash
cd game_api/app/
fastapi dev api.py
```

Démarrer le jeu :
```bash
cd app/domain/
python ./GestionnaireDuJeu.py
```

## Lancer les tests :
```bash
cd test/
./test.sh
```

## Instalation nécessaire :
```bash
conda install fastapi
conda install requests
conda install random
conda install json
conda install abc
```


## Routes de l'API :
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

- @app.get("/players/id/list/{id_partie}")
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


### Routes liées à l'histoire :
- @app.get("/histoire")
> Lire tout le dossier de l'histoire.

- @app.get("/histoire/{id_histoire}")
> Lire un chapitre de l'histoire en fonction de son identifiant.

- @app.get("/histoire/{id_histoire}/sortie")
> Lire la fin du chapitre de l'histoire en fonction de l'identifiant de son chapitre.


## L'architecture du projet :
```
┌app 
  ├data
    ├histoire.json              # La base de données de l'histoire.
    ├question-salle-1.json      # La base de données des questions de la salle 1.
    ├question-salle-2.json      # La base de données des questions de la salle 2.
    ├question-salle-3.json      # La base de données des questions de la salle 3.
  ├domaine
    ├question
      ├Question.py              # La classe abstraite Question, elle permet de poser une question.
      ├TypageSimple.py          # La classe TypageSimple, elle hérite de Question. Elle permet de poser les questions de la salle 1.
      ├TypageCompliquer.py      # La classe TypageCompliquer, elle hérite de Question. Elle permet de poser les questions de la salle 2.
      ├ErreurFonction.py        # La classe ErreurFonction, elle hérite de Question. Elle permet de poser les questions de la salle 3.
    ├GestionnaireDuJeu.py       # Le GestionnaireDuJeu va faire la gestion de la partie du joueur. Il va permettre d'accompagner le joueur tout au long de la partie.
    ├Histoire.py                # La classe Histoire va permettre de faire les appels aux routes API de l'histoire pour afficher l'histoire du jeu.

├game_api
  ├models
    ├player.py                  # Contient les modèles utilisés par l'API pour les routes en /player.
    ├question.py                # Contient les modèles utilisés par l'API pour les routes en /question.
  ├routers
    ├histoire.py                # Toutes les routes de l'API en /histoire sont ici.
    ├player.py                  # Toutes les routes de l'API en /player sont ici.
    ├question.py                # Toutes les routes de l'API en /question sont ici.
  ├services
    ├données_services.py        # Les fonctions utilitaires générales de l'API utilisées par beaucoup de routes de l'API sont ici.
    ├player_service.py          # Les fonctions utilitaires des routes en /player de l'API sont ici.
    ├question_service.py        # Les fonctions utilitaires des routes en /question de l'API sont ici.
  ├api.py                       # Ce script permet d'ouvrir les différentes routes de l'API grâce à FastAPI.

├test
  ├test.sh                      # Ce script permet de lancer toutes les batteries de tests unitaires. Idéale pour tout tester d'un coup !
  ├messageErreur.sh             # Ce script permet d'afficher dans le terminal si le résultat du test correspond ou non à ce qui était attendu.
  ├testHistoire.sh              # Contient toutes les batteries de tests unitaires des routes en /histoire de l'API.
  ├testJoueurs.sh               # Contient toutes les batteries de tests unitaires des routes en /player de l'API.
  ├testQuestions.sh             # Contient toutes les batteries de tests unitaires des routes en /question de l'API, il est spécialisé sur les routes /question qui sont utilisées par les joueurs.
  ├testQuestionsDynamique.sh    # Contient toutes les batteries de tests unitaires des routes en /question de l'API, il est spécialisé sur les routes /question qui permettent de modifier dynamiquement les questions.
```


## Équipe
- Émerick PACAUD
- Armel ZION
- Paul-Elie KOUAKOU
