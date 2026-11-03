# Mini-analyste pandas : arménien classique (HYE)

L'objectif est de répondre aux questions sur le corpus d'arménien (HYE)exclusivement à l'aide de scripts Python utilisant pandas.


## Règles
<!-- TODO : 3 ou 4 règles, une par ligne. Pensez à :
     - comment lancer Python ;
     - d'où doivent venir les chiffres ;
     - ce que l'agent n'a pas le droit de lire. -->
- Exécuter Python uniquement avec `uv run python`.
- Toutes les données et statistiques doivent provenir exclusivement des fichiers du dossier `data/`.
- Ne pas consulter de sources externes ni de fichiers situés hors du dossier `data/` pour produire des résultats.

## Rôles
<!-- TODO : quel agent fait quoi. -->
- L'agent `analyste` écrit et exécute `scripts/analyser.py` pour répondre aux questions.

## Repères
- Données : `data/HYE_train.tsv`, `data/HYE_test_in-domain.tsv`, `data/HYE_test_out-of-domain.tsv`, colonnes `text_form form lemma pos`.
- Tagset : `data/HYE_tagset.txt` (étiquette, tabulation, définition).