#!/bin/sh

if [ $# -eq 2 ]; then
    if [ $1 -eq $2 ]; then
        echo "✅ La requête fonctionne (Code $1)."
    else
        echo "❌ : La requête renvoie une erreur (Code $1)."
    fi
    echo ""
fi