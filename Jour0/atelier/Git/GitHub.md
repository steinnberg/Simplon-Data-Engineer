# 🧩 Résolution de conflits Git

## 🎯 Objectifs de la leçon

Dans cette leçon, nous allons démontrer **comment créer et résoudre un conflit de fusion** (*merge conflict*).

---

## 🚦 Introduction

Quand on travaille à plusieurs sur un même projet, il arrive que l’on « marche sur les pieds » les uns des autres. Autrement dit, il peut arriver que plusieurs développeurs modifient **les mêmes lignes de code en parallèle**.  
Même en utilisant des branches pour isoler nos modifications, cela n’empêche pas qu’un même fichier soit édité en même temps.

Savoir **résoudre un conflit de fusion** simplement est crucial. Beaucoup de développeurs débutants ont peur de Git à cause de ça. Chez Simplon, on veut que tu développes un bon **Git-Fu** 💪 — donc autant affronter ça directement !

---

## 🧪 Création d’un conflit de fusion

Pour créer un conflit de merge :

1. Crée un fichier Python dans **PyCharm**, sur la branche principale (`main` ou `master`).
2. Crée une nouvelle branche et modifie le fichier sur cette branche.
3. Modifie aussi le même fichier sur la branche principale.
4. Tente de fusionner les branches.

---

## 📂 Ajouter un fichier au dépôt

1. Ouvre PyCharm et ton dossier de projet.
2. Ajoute un fichier Python `git-fu.py` dans `module-1`.

```bash
touch git-fu.py
```

Ajoute ce fichier au suivi de Git :

```bash
git add .
```