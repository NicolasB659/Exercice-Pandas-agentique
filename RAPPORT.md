# Rapport du projet agentique

## Les 5 réponses, copiées depuis la sortie du script.

Q1
5 categories (pos) les plus frequentes dans HYE_train.tsv :
pos
V         1008
N+Com      786
I+Conj     745
I+Prep     310
A          295

Q2
Proportion de formes composees (@ dans pos) : 0.142
5 combinaisons les plus frequentes :
pos
N+Com@PRO+Dem           166
I+Prep@N+Com            164
I+Prep@N+Com@PRO+Dem     76
A@PRO+Dem                41
I+Prep@PRO+Dem           37

Q3
Mots du train dont le pos finit par @PRO+Dem (article suffixe) : 383
Mots du train dont le lemma commence par զ@ (preposition զ) : 339

Q4
Etiquettes du train absentes du tagset, avec leur effectif :
pos
PRO+Pos3    10
Total d'occurrences de ces etiquettes : 10

Q5
Score sur HYE_test_in_domain.tsv : 0.5667
Score sur HYE_test_out_domain.tsv : 0.5159
Baisse in-domain -> out-domain : 0.0507
En grec la baisse etait de 0,73 - 0,51 = 0,22.

## La consigne exacte donnée à l'agent.

Utilise le sous-agent analyste pour réaliser les cinq analyses demandées ci-dessous sur le corpus arménien classique HYE. Le script doit afficher cinq sections distinctes intitulées exactement Q1, Q2, Q3, Q4 et Q5 :
1. Quelles sont les 5 catégories (`pos`) les plus fréquentes dans le train ?
2. Quelle proportion des mots du train sont des formes composées (`@` dans `pos`) ? Quelles sont les 5 combinaisons les plus fréquentes ?
3. Combien de mots du train se terminent par l'article suffixé (`pos` qui finit par `@PRO+Dem`) ? Combien commencent par la préposition `զ` (`lemma` qui commence par `զ@`) ?
4. Quelles étiquettes du train **ne figurent pas** dans `HYE_tagset.txt`, et combien de fois chacune apparaît-elle ? Attention à deux pièges :
   - certains noms d'étiquettes du tagset se terminent par une espace ;
   - une étiquette composée est valide si chacune de ses parties l'est.
5. Refaites le **dictionnaire** de la partie 12 du notebook, avec le train arménien. Quel score obtient-il sur le test `in-domain`, puis sur le test `out-of-domain` ? Le score baisse-t-il autant qu'en grec (0,73 contre 0,51) ?

## **Une erreur de l'agent**

Les résultats paraisssent cohérents cependant j'ai eu besoin de faire un réel ravail pour résumer les informations dans les agents afin de ne pas m'égarer dans le contexte établis et donc risquer plus facilement les erreurs. 
Le script fournis avait aussi tendance à utiliser des fonctionnalités de pandas non listé dans le fichier SKILL

## Les fonctions que vous avez ajoutées à la skill `pandas-tuto`

| compter les valeurs vraies | `.sum()` |
| calculer une proportion | `.mean()` |
| vérifier le début d'une chaîne | `.str.startswith("texte")` |
| vérifier la fin d'une chaîne | `.str.endswith("texte")` |
| séparer une étiquette composée | `.str.split("@")` |
| transformer les éléments séparés en lignes | `.explode()` |

## qu'est-ce que l'agent apporte ici par rapport au notebook ? Qu'est-ce qu'il coûte ?

L'agent apporte la systématicité. On aura beau rajouté d'autres données dans le fichier data, le modèle va pouvoir adapter directement le code. Pour une tâche peu complexe comme ici le véritable apport est donc l'adaptabilité puisqu'il pourra aussi être utilisé pour d'autres langues. On peut voir que la baisse de score in-domain → out-of-domain est ici plus faible mais elle peut être du au changement de langue. 
Son coût est d'abord économique et énergique puisque l'utilisation d'un modèle utilise des tokens et est très gourmand en énergie. De plus, il y a un risque de tomber pour des modèles complexes dans une gestion de modèles boîte noire, en utilisant des scripts dont on ne peut expliquer le fonctionnement. 