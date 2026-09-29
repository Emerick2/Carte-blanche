#!/bin/sh

url="http://127.0.0.1:8000"

echo "--- ♦ Gestion de l'histoire ♦ ---"

echo "Lire tout le dossier de l'hisoire :"
code_http=$(curl --silent --output /dev/null --write-out "%{http_code}" "${url}/histoire")
./messageErreur.sh $code_http 200

echo "Lire un chapitre de l'histoire en fonction de son identifiant :"
code_http=$(curl --silent --output /dev/null --write-out "%{http_code}" "${url}/histoire/1")
./messageErreur.sh $code_http 200

echo "Lire la fin du chapitre de l'histoire en fonction de l'identifiant de son chapitre."
code_http=$(curl --silent --output /dev/null --write-out "%{http_code}" "${url}/histoire/1/sortie")
./messageErreur.sh $code_http 200

