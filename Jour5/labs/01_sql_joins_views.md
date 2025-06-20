# TP – SQL : Jointures & Vues

## Objectif
Comprendre les jointures en SQL et l'utilisation des vues pour simplifier les requêtes complexes.

## Étapes

1. Crée une table simplifiée `authors` :

```sql
CREATE TABLE authors (
    Author TEXT PRIMARY KEY,
    Nationality TEXT,
    Birth_Year INTEGER
);
```

2. Insère quelques données à la main dans `authors`.

3. Réalise une jointure :

```sql
SELECT b.Book_Name, a.Nationality
FROM books b
JOIN authors a ON b.Author = a.Author;
```

4. Crée une `VIEW` appelée `book_stats` affichant :
   - `Book_Name`, `Gross_Sales`, `Sale_Price`, `Units_Sold`, `Book_Average_Rating`

```sql
CREATE VIEW book_stats AS
SELECT Book_Name, Gross_Sales, Sale_Price, Units_Sold, Book_Average_Rating
FROM books;
```

5. Requête exemple sur la vue :

```sql
SELECT Book_Name, (Gross_Sales / Units_Sold) AS Average_Revenue
FROM book_stats
ORDER BY Average_Revenue DESC;
```