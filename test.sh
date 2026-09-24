#!/bin/sh

url="http://127.0.0.1:8000"
echo "Début des tests"

echo "Ouverture de la partie :"
id_partie=$(curl --silent --show-error --fail ${url}/)
echo "Identifiant de la partie : $id_partie"
echo ""

echo "Test sur les questions de la salle 1 :"
curl -X GET ${url}/question/salle-1/liste
echo ""
echo "Test sur les questions de la salle 2 :"
curl -X GET ${url}/question/salle-2/liste
echo ""
echo "Test sur les questions de la salle 3 :"
curl -X GET ${url}/question/salle-3/liste
echo ""

echo "Voir une question aléatoire :"
q1=$(curl --silent --show-error --fail ${url}/question/${id_partie}/salle-1)
q2=$(curl --silent --show-error --fail ${url}/question/${id_partie}/salle-1)
curl ${q1}
echo ""
