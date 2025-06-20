-- init_books.sql
------------------------------------------------------------
-- 1) Créer la table ----------------------------------------
DROP TABLE IF EXISTS books;

CREATE TABLE books (
    Publishing_Year       INTEGER,
    Book_Name             TEXT,
    Author                TEXT,
    Language_Code         TEXT,
    Author_Rating         TEXT,
    Book_Average_Rating   REAL,
    Book_Ratings_Count    INTEGER,
    Genre                 TEXT,
    Gross_Sales           REAL,
    Publisher_Revenue     REAL,
    Sale_Price            REAL,
    Sale_Rank             INTEGER,
    Publisher             TEXT,
    Units_Sold            INTEGER
);

------------------------------------------------------------
-- 2) Importer les données CSV ------------------------------
-- Les commandes .mode et .import sont des directives SQLite,
-- elles ne font PAS partie du SQL standard ; gardez-les
-- dans le même fichier ou tapez-les manuellement dans le shell.

.mode csv
.separator ","
.import publications.csv books

------------------------------------------------------------
-- 3) Vérification rapide -----------------------------------
-- (facultatif : garde ces requêtes ou exécute-les ensuite)

-- Nombre de lignes importées
SELECT COUNT(*) AS Nb_Rows FROM books;

-- Aperçu des 5 premiers enregistrements
SELECT * FROM books LIMIT 5;
