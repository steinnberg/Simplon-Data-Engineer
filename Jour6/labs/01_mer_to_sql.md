# TP – MER → SQL

## Objectif
Passer d’un besoin fonctionnel à une base de données relationnelle via un MER.

---

## Scénario

Une bibliothèque souhaite stocker les informations suivantes :
- Livres : titre, ISBN, prix, date de publication
- Auteurs : nom, pays, année de naissance
- Éditeurs : nom, adresse, site web
- Un livre peut avoir plusieurs auteurs, un éditeur
- Un auteur peut écrire plusieurs livres

---

## Étapes

1. Dessine le MER (Entité, Relations, Cardinalités)
2. Déduis les tables SQL correspondantes
3. Applique les 3 formes normales (1NF → 3NF)
4. Écris les requêtes `CREATE TABLE` correspondantes
5. Identifie les `PRIMARY KEY` et `FOREIGN KEY`

---

## Bonus

- Insère quelques données test
- Crée une vue `livre_auteur_editeur`

## 🛠 Exemple simple
Un auteur peut écrire plusieurs livres, et chaque livre a un ou plusieurs auteurs.

```
[Auteur] ——⟶[Écrit]⟶—— [Livre]
  nom                titre
  pays               ISBN

  ```