# 🚀 Comprendre la fonction `lambda` en Python et ses usages en Data Analyse

---

## ✅ Qu’est-ce qu’une fonction `lambda` ?

En Python, une **fonction `lambda`** est une **fonction anonyme** — c’est-à-dire une fonction **sans nom** — qui s’écrit en **une seule ligne**.  
Elle est pratique pour créer des fonctions **rapides**, **légères** et **jetables**, souvent utilisées comme argument d’autres fonctions.

---

#### 📌 Syntaxe de base

```python
lambda arguments: expression
```


### ✅ Exemple simple

python
#### Version classique
```
def double(x):
    return x * 2
```

#### Version lambda équivalente

```
double = lambda x: x * 2

print(double(5))  # Affiche 10
```


#### ✅ Remarque : lambda fait la même chose qu’une def mais en version compacte.
Très pratique pour des fonctions à usage unique.

#### ✅ Pourquoi lambda est utile en Data Analyse ?
En analyse de données, lambda est souvent utilisée pour :

- Appliquer rapidement une fonction courte sur une liste ou une colonne.

- Écrire du code plus lisible sans créer une def séparée.

- Combiner lambda avec :

- map() pour appliquer une transformation.

- filter() pour filtrer une liste.

- apply() ou assign() pour traiter des colonnes avec Pandas.

#### ✅ 🔍 Usages concrets en Data Analyse
➜ A) map() — Appliquer une transformation

```
python
nombres = [1, 2, 3, 4, 5]

#### Doubler chaque élément
resultat = list(map(lambda x: x * 2, nombres))
print(resultat)  # [2, 4, 6, 8, 10]
```

#### ✅ map() applique la lambda à chaque élément.

➜ B) filter() — Filtrer une liste
```
python

# Garder seulement les nombres pairs
pairs = list(filter(lambda x: x % 2 == 0, nombres))
print(pairs)  # [2, 4]
```

### ✅ filter() conserve les éléments pour lesquels la lambda renvoie True.

➜ C) apply() et assign() avec Pandas

```
python

import pandas as pd

# DataFrame d'exemple
df = pd.DataFrame({
    "nom": ["Alice", "Bob", "Charlie"],
    "note": [12, 17, 9]
})

# Créer une colonne 'mention'
df = df.assign(
    mention=lambda d: d["note"].apply(lambda x: "Admis" if x >= 10 else "Ajourné")
)

print(df)
```

#### ✅ Résultat :

nom	note	mention
Alice	12	Admis
Bob	17	Admis
Charlie	9	Ajourné

#### Explication :

- .apply() applique une lambda à chaque valeur de note.

- .assign() crée une nouvelle colonne mention.

#### 🎯 Bonnes pratiques
✅ lambda est idéale pour des fonctions très simples.

⚠️ Pour des logiques plus longues ou complexes, mieux vaut utiliser une def.

⚠️ Une lambda ne peut pas contenir de logique multi-lignes.

#### ✅ Résumé
Avantage	Détail
Compacte	Déclaration en une seule ligne
Outils associés	map(), filter(), apply(), assign()
Usage typique	Nettoyage de données, calculs conditionnels, filtrage rapide

