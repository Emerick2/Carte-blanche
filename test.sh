#!/bin/bash

url="http://127.0.0.1:8000"
echo "Début des tests"


function messageErreur() 
{
    if [ $1 -eq $2 ]; then
        echo "✅ La requête fonctionne (Code $1)."
    else
        echo "❌ : La requête renvoie une erreur (Code $1)."
    fi
    echo ""
}


echo "Ouverture de la partie :"
id_partie=$(curl --silent --show-error --fail "${url}/" | python -c 'import json, sys; print(json.load(sys.stdin))')
echo "Identifiant de la partie : $id_partie"

# -------------------------------------------------------

echo "Test sur les questions de la salle 1 :"
# curl -X GET ${url}/question/salle-1/liste
code_http=$(curl --silent --output /dev/null --write-out "%{http_code}" "${url}/question/salle-1/liste")

messageErreur $code_http 200

echo "Test sur les questions de la salle 2 :"
# curl -X GET ${url}/question/salle-2/liste
code_http=$(curl --silent --output /dev/null --write-out "%{http_code}" "${url}/question/salle-2/liste")

messageErreur $code_http 200

echo "Test sur les questions de la salle 3 :"
# curl -X GET ${url}/question/salle-3/liste
code_http=$(curl --silent --output /dev/null --write-out "%{http_code}" "${url}/question/salle-3/liste")

messageErreur $code_http 200


# -------------------------------------------------------
echo "Voir une question aléatoire :"
q1=$(curl --silent --show-error --fail ${url}/question/${id_partie}/salle-1)
q2=$(curl --silent --show-error --fail ${url}/question/${id_partie}/salle-1)
curl ${q1}
echo ""
if [ $q1 != $q2 ]; then
    echo "✅ : Les deux question généré ne sont pas identique !"
else
    echo "❌ : ERREUR : Les deux question généré sont identique"
fi

# -------------------------------------------------------
echo "Voir une question spécifique :"
code_http=$(curl --silent --output /dev/null --write-out "%{http_code}" "${url}/question-spécifique/salle-1/1")

messageErreur $code_http 200

# -------------------------------------------------------
echo "Ajouter un joueur :"
texteJSON=$(printf '{"name":"LePrénom","score_salle_1":0,"score_salle_2":0,"score_salle_3":0,"id_partie":"%s"}' "$id_partie")
# curl --silent --show-error --fail -X POST "${url}/players" \
#     -H "Content-Type: application/json" \
#     -d "$texteJSON"

code_http=$(curl --silent --show-error --fail  --output /dev/null --write-out "%{http_code}" -X POST "${url}/players" \
    -H "Content-Type: application/json" \
    -d "$texteJSON")

messageErreur $code_http 200

# -------------------------------------------------------
echo "Voir la liste des joueurs :"
code_http=$(curl --silent --output /dev/null --write-out "%{http_code}" "${url}/players/${id_partie}")

messageErreur $code_http 200

# -------------------------------------------------------
echo "Voir un joeur en particulier :"
code_http=$(curl --silent --output /dev/null --write-out "%{http_code}" "${url}/players/${id_partie}/0")
# curl -X GET "${url}/players/${id_partie}/0"
messageErreur $code_http 200

# -------------------------------------------------------
echo "Voir la liste des joueurs existants :"
code_http=$(curl --silent --output /dev/null --write-out "%{http_code}" "${url}/id/list/${id_partie}")
# curl -X GET "${url}/id/list/${id_partie}"
messageErreur $code_http 200

# -------------------------------------------------------
echo "Supprimer un joueur de la partie :"    
code_http=$(curl --silent --show-error --fail  --output /dev/null --write-out "%{http_code}" -X DELETE "${url}/players/${id_partie}/0")

messageErreur $code_http 200

# curl -X DELETE "${url}/players/${id_partie}/1"

curl -X GET "${url}/players/${id_partie}/0"

echo "Vérifier que la suppresion à bien fonctionné :"    

code_http=$(curl --silent --output /dev/null --write-out "%{http_code}" "${url}/players/${id_partie}/0")
echo $code_http
messageErreur $code_http 404
