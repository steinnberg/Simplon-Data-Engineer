
## Script SQL
Voici le script SQL (compatible SQLite) pour créer la base et la table books, puis y importer le fichier CSV publications.csv.

## Excussion
Exécute-le depuis l’interface en ligne de commande sqlite3 :

```
bash
sqlite3 publications.db < init_books.sql
où init_books.sql est le fichier contenant les lignes ci-dessous ; place publications.csv dans le même dossier avant d’exécuter l’import.
```