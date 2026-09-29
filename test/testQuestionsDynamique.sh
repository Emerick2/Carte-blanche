#!/bin/sh

url="http://127.0.0.1:8000"

echo "--- ♦ Gestion dynamique des question ♦ ---"

echo "Vérifier que l'ajout dynamique de question fonctionne bien :"
texteJSON=$(printf '{"question": "La nouvelle question pour les tests","réponseA": "Réponse A","réponseB": "Réponse B","réponseC": "Réponse C","réponse": 1,"indice": "Un indice","salle": 1}')

code_http=$(curl --silent --show-error --fail  --output /dev/null --write-out "%{http_code}" -X POST "${url}/question" \
    -H "Content-Type: application/json" \
    -d "$texteJSON")

./messageErreur.sh $code_http 200

# -------------------------------------------------------

echo "Vérifier que l'on peut bien changer l'identifiant de réponse d'une question dynamiquement"
code_http=$(curl --silent --output /dev/null --write-out "%{http_code}" -X PUT "${url}/question/1/30/2")
./messageErreur.sh $code_http 200

# -------------------------------------------------------

echo "Vérifier que la suppresion dynamique de question fonctionne bien :"
code_http=$(curl --silent --show-error --fail --output /dev/null --write-out "%{http_code}" -X DELETE "${url}/question/1/30")
./messageErreur.sh $code_http 200
echo "--- ♦ Gestion dynamique des question ♦ ---"

echo "Vérifier que l'ajout dynamique de question fonctionne bien :"
texteJSON=$(printf '{"question": "La nouvelle question pour les tests","réponseA": "Réponse A","réponseB": "Réponse B","réponseC": "Réponse C","réponse": 1,"indice": "Un indice","salle": 1}')

code_http=$(curl --silent --show-error --fail  --output /dev/null --write-out "%{http_code}" -X POST "${url}/question" \
    -H "Content-Type: application/json" \
    -d "$texteJSON")

./messageErreur.sh $code_http 200

# -------------------------------------------------------

echo "Vérifier que l'on peut bien changer l'identifiant de réponse d'une question dynamiquement"
code_http=$(curl --silent --output /dev/null --write-out "%{http_code}" -X PUT "${url}/question/1/30/2")
./messageErreur.sh $code_http 200

# -------------------------------------------------------

echo "Vérifier que la suppresion dynamique de question fonctionne bien :"
code_http=$(curl --silent --show-error --fail --output /dev/null --write-out "%{http_code}" -X DELETE "${url}/question/1/30")
./messageErreur.sh $code_http 200
