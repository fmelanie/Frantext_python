
[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/fmelanie/Frantext_python/master)

Comment faire lorsque l'on souhaite analyser les contextes de verbes extraits de Frantext ?
Comment analyser un même nombre d'occurrences pour chacun des verbes ?

Il s'agit :
- dans un premier temps de faire autant de requêtes CQL dans Frantext qu'on a de verbes concernés, 
et d'exporter chacune des requêtes dans un fichier indépendant,
- dans un second temps d'isoler les éléments qui se trouvent autour du pivot,
- dans un troisième temps de sélectionner aléatoirement un même nombre d'exemples pour chacun des verbes,
et de garder une trace quantitative de cette sélection.

# Extraire des exemples de Frantext :

- constituer un corpus de travail
(onglet "corpus")

Exemple : romans, 1900-1999

- faire des requêtes CQL
(onglet "recherche" > avancée)

Exemple :

[lemma="élucider"%cd & pos="V|VPP"]

[lemma="illustrer"%cd & pos="V|VPP"]

[lemma="montrer"%cd & pos="V|VPP"]


- exporter chacun des résultats dans un fichier 

Paramètre d'exportation :
    . 100 (caractères)
    . Auteur, Titre, Date
    . page
ATTENTION :
    . ne pas cocher "séparer les mots de la cible"
    (particulièrement si la requête CQL crée un pivot de plusieurs mots. Ce qui n'est pas le cas de notre exemple)
    . cocher "inclure les numéros de résultats"

exemple:
élucider.csv
illustrer.csv
montrer.csv
(à placer dans un dossier "export_frantext")

# Lancer le script python Frantext_ajoutCol.py

- En entrée, le script prend les fichiers dans le dossier "export_frantext".
Ils sont structurés en 8 colonnes :
id, auteur, titre, date, page, ctx gauche, pivot, ctx droit

- En sortie, le script génère des fichiers csv dans "export_frantext_ajoutCol".
Ils sont structurés en 13 colonnes :
id, auteur, titre, intervale tps, date, page, ctx gauche, mot gauche, ponct G, pivot, ponct D, mot droit, ctx droit

Il s'agit d'isoler ce qui entour le pivot :
- si le pivot est précédé ou suivi d'une ponctuation, cette dernière est isolée dans une colonne.
- le dernier mot du contexte gauche ainsi que le premier mot du contexte droit sont isolés dans leur colonne respective "mot gauche" et "mot droit".

Il s'agit aussi de définir des plages de 10 ans ("interval tps") à partir de la date de l'exemple. Permet de regrouper et travailler les exmples par décennie.

# Lancer le script python Frantext_selecAleatoire.py

- En entrée, le script prend les fichiers du dossier "export_frantext_ajoutCol".

- En sortie, le script crée :

1 fichier csv contenant 20 exemples maximum par verbe et par interval temporel, sélectionné aléatoirement parmi l'ensemble des exemples disponibles (verbes_choixAletoire.csv).
Dans ce fichier, un "ID select" est ajouté. Il s'agit de numéroter les exemples retenus dans l'ordre d'apparition alétaoire, pour pouvoir les manipuler et modifier les tris dans Excel, et ainsi  garder une trace de la sélection aléatoire. (L'Id provenant de l'extraction Frantext est renommé "id Frantext").

1 fichier csv qui regroupe l'ensemble des exmples non retenus dans le fichier précédent.
(verbes_pioche.csv)

1 fichier compte qui compte le nombtre d'exmples pour chacun des fichiers et par décennie.
(compte.csv)
