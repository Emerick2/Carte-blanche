#!/bin/sh

url="http://127.0.0.1:8000"
id_partie=$(curl --silent --show-error --fail "${url}/" | python -c 'import json, sys; print(json.load(sys.stdin))')

echo "--- ♦ Gestion des joueurs ♦ ---"

# -------------------------------------------------------
echo "Ajouter un joueur :"
texteJSON=$(printf '{"name":"LePrénomJ1","score_salle_1":0,"score_salle_2":0,"score_salle_3":0,"id_partie":"%s"}' "$id_partie")
joueur=$(curl --silent --show-error --fail -X POST "${url}/players" \
    -H "Content-Type: application/json" \
    -d "$texteJSON")
id_joueur=$(printf '%s' "$joueur" | python -c 'import json, sys; print(json.load(sys.stdin)["id"])')
code_http=200

./messageErreur.sh $code_http 200

# -------------------------------------------------------
echo "Voir la liste des joueurs :"
code_http=$(curl --silent --output /dev/null --write-out "%{http_code}" "${url}/players/${id_partie}")

./messageErreur.sh $code_http 200

# -------------------------------------------------------
echo "Voir un joeur en particulier :"
code_http=$(curl --silent --output /dev/null --write-out "%{http_code}" "${url}/players/${id_partie}/${id_joueur}")
# curl -X GET "${url}/players/${id_partie}/0"
./messageErreur.sh $code_http 200

# -------------------------------------------------------
echo "Voir la liste des joueurs existants :"
code_http=$(curl --silent --output /dev/null --write-out "%{http_code}" "${url}/id/list/${id_partie}")
# curl -X GET "${url}/id/list/${id_partie}"
./messageErreur.sh $code_http 200

# -------------------------------------------------------
echo "Modification du score du joueur"
code_http=$(curl --silent --output /dev/null --write-out "%{http_code}" -X PUT "${url}/players/${id_partie}/salle-1/${id_joueur}/10")
./messageErreur.sh $code_http 200

# -------------------------------------------------------
echo "Supprimer un joueur de la partie :"    
code_http=$(curl --silent --show-error --fail --output /dev/null --write-out "%{http_code}" -X DELETE "${url}/players/${id_partie}/${id_joueur}")

./messageErreur.sh $code_http 200

# curl -X DELETE "${url}/players/${id_partie}/1"

# curl -X GET "${url}/players/${id_partie}/${id_joueur}"

echo "Vérifier que la suppresion à bien fonctionné :"    

code_http=$(curl --silent --output /dev/null --write-out "%{http_code}" "${url}/players/${id_partie}/${id_joueur}")
./messageErreur.sh $code_http 404