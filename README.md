
# Dans Frantext :

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
    (si votre requête CQL crée un pivot de plusieurs mots, ce qui n'est pas le cas de notre exmple)
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

1 fichier csv contenant 20 exemples maximum par verbe et par interval temporel, sélectionné aléatoirement parmi l'ensemble des exemples disponibles.

1 fichier csv qui regroupe l'ensemble des exmples non retanus dans le fichier précédent.

1 fichier compte qui compte le nombtre d'exmples pour chacun des fichiers et par décennie.
