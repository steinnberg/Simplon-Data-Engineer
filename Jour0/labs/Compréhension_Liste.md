
# Compréhension de Liste  
**Semaine 1 : Module 1**

## Jour 2

- Dictionnaires, Ensembles et Tuples
- **LAB | Dictionnaires, Ensembles et Tuples**
- Compréhension de Liste
- **LAB | Compréhension de Liste**

---

## Matériel du Jour

### Compréhension de Liste  
**LEÇON**

---

## Objectifs de la Leçon

- Comprendre le concept de combinaison du stockage avec l’itération.  
- Apprendre comment les compréhensions de liste combinent stockage et itération de façon efficace.  
- Apprendre à intégrer une logique conditionnelle dans les compréhensions de liste.  
- Savoir construire des compréhensions de liste avec plusieurs boucles `for`.  
- Ajouter une logique conditionnelle aux compréhensions multi-boucles.  
- Découvrir quelques cas d’utilisation des compréhensions de liste.

---

## Introduction

En continuant à améliorer vos compétences en Python, vous rencontrerez des moyens pratiques de combiner certains concepts de base appris précédemment. Dans cette leçon, nous allons découvrir la **compréhension de liste**. La compréhension de liste combine stockage dans des structures de données, itération, et même logique conditionnelle sous une forme efficace.

---

## Combiner Stockage et Itération

L’idée principale derrière la compréhension de liste est le **stockage itératif**. Dans certaines leçons précédentes, nous avons vu des situations où il fallait créer une liste vide et utiliser une boucle `for` pour y ajouter une valeur à chaque itération.

```python
lst = []

for i in range(10):
    lst.append(i)

print(lst)
```

**Explication du code :**  
Dans cet exemple, nous créons une liste vide, puis pour chaque nombre dans l’intervalle donné, nous l’ajoutons à la liste.

---

## Compréhension de Liste

Une compréhension de liste permet de simplifier cette logique en une seule ligne de code Python. Au lieu de créer une liste vide et de la remplir avec `append`, les crochets de la compréhension de liste rassemblent directement les résultats dans une liste.

```python
lst = [i for i in range(10)]
print(lst)
```

**Explication du code :**  
On obtient le même résultat avec moins de lignes de code, ce qui est généralement positif. À l’intérieur des crochets, on demande la valeur pour chaque élément de l’intervalle.

---

## Ajouter des Conditions aux Compréhensions de Liste

On peut aussi ajouter des conditions aux compréhensions de liste. Les conditions viennent après la boucle `for` pour exclure les résultats qui ne remplissent pas la condition. L’exemple ci-dessous renvoie chaque valeur de l’intervalle mais seulement si elle est supérieure ou égale à 5.

```python
lst = [i for i in range(20) if i >= 5]
print(lst)
```

**Explication du code :**  
Ici, seuls les nombres supérieurs ou égaux à 5 sont inclus dans la liste.

---

## Ajouter de la Logique Conditionnelle Complexe

Les compréhensions de liste peuvent gérer une certaine complexité. Par exemple, imaginons qu’on ait une liste de listes comme ci-dessous, et qu’on veuille extraire les nombres pairs qui apparaissent dans des sous-listes de longueur inférieure à 4. On peut y parvenir avec deux boucles `for` et deux conditions.

```python
lst_lst = [[1,2,3,4,5], [6,7,8], [9,10]]

lst = [y for x in lst_lst if len(x) < 4 for y in x if y % 2 == 0]
print(lst)
```

**Explication du code :**  
On récupère chaque sous-liste dont la longueur est inférieure à 4, puis chaque élément `y` pair de cette sous-liste.

---

## Plusieurs Boucles `for` dans une Compréhension de Liste

Parfois, on doit gérer des situations plus complexes avec plusieurs boucles. Par exemple, pour aplatir des listes imbriquées en une seule liste :

**Sans compréhension de liste :**

```python
lst_lst = [[1,2,3], [4,5,6], [7,8,9]]

lst = []

for x in lst_lst:
    for y in x:
        lst.append(y)

print(lst)
```

**Explication du code :**  
On parcourt chaque sous-liste, puis chaque élément de chaque sous-liste, qu’on ajoute à la liste finale.

---

**Avec compréhension de liste :**

```python
lst_lst = [[1,2,3], [4,5,6], [7,8,9]]

lst = [y for x in lst_lst for y in x]
print(lst)
```

**Explication du code :**  
Le résultat est le même mais avec une syntaxe beaucoup plus compacte. L’ordre des boucles `for` doit être le même que dans la version classique.

---

## Cas Pratiques

### Lire Plusieurs Fichiers

Un cas pratique fréquent : des données réparties dans plusieurs fichiers. Par exemple, un dossier `data` contient plusieurs fichiers CSV. On peut utiliser une compréhension de liste pour lister seulement les fichiers CSV, puis une autre pour les lire avec Pandas, avant de les combiner avec `pd.concat`.

```python
import os
import pandas as pd

file_list = [f for f in os.listdir('./data') if f.endswith('.csv')]
data_sets = [pd.read_csv(os.path.join('./data', f)) for f in file_list]
data = pd.concat(data_sets, axis=0)
```

**Explication du code :**  
En trois lignes, on liste les CSV, on les lit et on les fusionne en un seul jeu de données !

---

### Sélectionner des Colonnes d’un DataFrame selon une Condition

Autre exemple : sélectionner les colonnes numériques dont la moyenne est supérieure à 15.

```python
data = pd.read_csv('vehicles.csv')

selected_columns = [col for col in data._get_numeric_data() if data[col].mean() > 15]
print(selected_columns)
```

**Explication du code :**  
On récupère uniquement les colonnes numériques dont la moyenne est supérieure à 15.

---

## Résumé

Dans cette leçon, nous avons découvert les compréhensions de liste :  
- La base : combiner stockage et itération.
- La syntaxe : version plus compacte des boucles `for` classiques.
- Des variantes : conditions simples, boucles multiples.
- Des cas pratiques pour la manipulation de données.  

Ces techniques sont des outils puissants pour rendre votre code Python plus clair et plus efficace.

---
