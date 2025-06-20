# Atelier – Validation croisée de MER (Modèle Entité-Relation)

## 🧱 Composants d’un MER

| Élément      | Description                                                                 |
|--------------|-----------------------------------------------------------------------------|
| **Entité**   | Représente un objet ou un concept important (ex : Livre, Auteur, Client)   |
| **Attribut** | Caractéristique de l’entité (ex : nom, date de naissance, ISBN)            |
| **Relation** | Lien logique entre deux entités (ex : "écrit", "possède")                  |
| **Cardinalité** | Nombre minimum et maximum d’occurrences possibles dans une relation (ex : 1,n ; 0,1) |
| **Identifiant** | Attribut (ou combinaison) qui distingue de façon unique chaque entité (clé primaire) |



## 🎯 Objectif d’un MER

Le **Modèle Entité-Relation (MER)** a pour but de **traduire un besoin métier** en une **structure logique de données**, **sans encore penser aux tables ou aux contraintes techniques**.

---

Il sert de **point de départ** pour :

- 🗂️ construire les **tables SQL** ;
- 🔑 établir les **clés primaires et étrangères** ;
- 🔄 assurer une **base normalisée** et **évolutive**.


---
## Objectif de l'atelier
Comparer les schémas MER proposés par les binômes et repérer les incohérences ou optimisations.

---

## Étapes

1. Chaque binôme affiche son MER
2. Les autres analysent :
   - Clarté des entités
   - Respect des règles de normalisation
   - Cohérence des clés étrangères
3. Feedback collectif