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


**Explication** : on ajoute tous les fichiers non suivis.

Dans ce fichier, écris une ligne simple :


```python
print("this is the original message")
```

## ✅ Commit & Push

```bash

git commit -am "ajout du fichier git-fu"
git push
```

## 🌿 Créer une nouvelle branche

```bash
git checkout -b conflict-branch
Explication : checkout -b crée et change de branche en une seule commande.
```

Dans la branche conflict-branch, modifie le fichier :

```python

print("this is the altered message")
Commit et push :
```
```bash

git commit -am "modification du fichier git-fu"
git push --set-upstream origin conflict-branch
```
## 🔀 Fusionner les branches
Reviens sur la branche master :

```bash
git checkout master
Fais une autre modification :
```

```python
print("this is the master message")
```
Commit et push :

```bash
git commit -am "mise à jour sur master"
git push
```

Ensuite, tente de fusionner :

```bash
git merge conflict-branch
```

Si tout se passe bien, Git merge tout seul. Mais ici, un conflit va se produire ! Git va te dire qu’il y a un merge conflict dans git-fu.py.

## 🧹 Résoudre le conflit
Dans PyCharm, le fichier ressemblera à ça :

```plaintext

print("this is the master message")
```

Choisis la version à garder. 


Exemple : garde seulement la ligne du master.

```python
print("this is the master message")
```

Ensuite, termine le merge :

```bash
git commit -am "résolution du conflit"
git push
```

## ⏪ Annuler un merge
Si le conflit est trop compliqué :

```bash

git status  # Vérifie l’état
git merge --abort  # Annule le merge, revient à l’état d’avant
```

## 🎭 Forcer avec ours ou theirs
Tu peux forcer Git à choisir notre version ou leur version :

```bash

git checkout --ours -- ./module-1/git-fu.py

## 🔗 Conflits avec Pull Request
```

Quand tu crées une pull request (PR) sur GitHub :

1. Pousse les branches.

2. Crée la PR.

3. GitHub détecte les conflits.

4. Clique sur Resolve conflicts.

5. Modifie le fichier directement dans l’UI GitHub.

6. Valide le conflit résolu, merge la PR.


## ✅ Conclusion
Tu sais maintenant :

* Créer un conflit de merge.

* Le résoudre manuellement.

* Utiliser ours et theirs.

* Annuler un merge.

* Résoudre un conflit dans une PR sur GitHub.

🚀 Bravo pour ton Git-Fu !




