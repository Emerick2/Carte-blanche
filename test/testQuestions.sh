#!/bin/sh

url="http://127.0.0.1:8000"
id_partie=$(curl --silent --show-error --fail "${url}/" | python -c 'import json, sys; print(json.load(sys.stdin))')

echo "--- ♦ Gestion des questions ♦ ---"

echo "Test sur les questions de la salle 1 :"
# curl -X GET ${url}/question/salle-1/liste
code_http=$(curl --silent --output /dev/null --write-out "%{http_code}" "${url}/question/salle-1/liste")

./messageErreur.sh $code_http 200

echo "Test sur les questions de la salle 2 :"
# curl -X GET ${url}/question/salle-2/liste
code_http=$(curl --silent --output /dev/null --write-out "%{http_code}" "${url}/question/salle-2/liste")

./messageErreur.sh $code_http 200

echo "Test sur les questions de la salle 3 :"
# curl -X GET ${url}/question/salle-3/liste
code_http=$(curl --silent --output /dev/null --write-out "%{http_code}" "${url}/question/salle-3/liste")

./messageErreur.sh $code_http 200

# -------------------------------------------------------
echo "Voir une question aléatoire :"
q1=$(curl --silent --show-error --fail "${url}/question/${id_partie}/salle-1")
q2=$(curl --silent --show-error --fail "${url}/question/${id_partie}/salle-1")
# printf '%s\n' "$q1"
if [ "{$q1}" -eq "{$q2}" ]; then
    echo "❌ : ERREUR : Les deux question généré sont identique"
else
    echo "✅ : Les deux question généré ne sont pas identique !"
fi
echo ""

# -------------------------------------------------------
echo "Voir une question spécifique :"
code_http=$(curl --silent --output /dev/null --write-out "%{http_code}" "${url}/question/chercher/salle-1/1")
./messageErreur.sh $code_http 200
