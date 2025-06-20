## ⚙️ Explications rapides des commandes SQLite

| Étape                       | Commande / clause                 | Rôle                                                                 |
|----------------------------|----------------------------------|----------------------------------------------------------------------|
| Suppression préalable      | `DROP TABLE IF EXISTS books;`    | Supprime la table si elle existe déjà (permet de rejouer le script) |
| Déclaration de la structure| `CREATE TABLE`                   | Déclare la structure de la table `books` avec les types adaptés      |
| Mode d'import CSV          | `.mode csv` et `.separator ","` | Indiquent à SQLite que les données arrivent au format CSV, séparées par des virgules |
| Importation des données    | `.import publications.csv books` | Lit `publications.csv` et insère chaque ligne dans la table `books` |
| Vérification                | `SELECT …`                       | Vérifie le succès de l’import (ex. : `SELECT COUNT(*) FROM books;`) |


## Autre solution
Avec un script Python minimal (compatible Python 3.x) pour :
    -charger le fichier publications.csv avec pandas ;

    -créer une base de données SQLite nommée publications.db ;

    -enregistrer les données dans une table books.