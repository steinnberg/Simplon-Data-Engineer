# Lab | Nettoyage de Données

## Introduction

On entend souvent dire qu’un data scientist consacre 80 % de son temps au nettoyage de données. Nous ne savons pas si ce chiffre est exact, mais un data scientist passe effectivement beaucoup de temps et d’efforts à collecter, nettoyer et préparer les données pour l’analyse.  
En effet, les jeux de données sont généralement désordonnés et complexes par nature. Il est donc essentiel pour un data scientist de savoir affiner et restructurer les jeux de données afin de les rendre exploitables pour passer à l’étape d’analyse.

Dans cet exercice, vous allez pratiquer les techniques de nettoyage de données abordées pendant le cours et en découvrir de nouvelles en consultant de la documentation et des références.  
Vous travaillerez de manière autonome, mais rappelez-vous que l’équipe pédagogique est à votre disposition en cas de problème.

## Pour commencer

Vous devriez déjà être familier avec le déroulement pour résoudre et soumettre les labs. Mais si ce n’est pas le cas, relisez les consignes dans le `README.md` à la [racine du repo](../..) ainsi que dans le [lab précédent](../Intro_Pandas).

Dans ce lab, vous travaillerez dans le fichier [main.ipynb](your-code/main.ipynb). Pour le lancer, naviguez d’abord dans le terminal jusqu’au répertoire contenant `main.ipynb`, puis exécutez `jupyter notebook`. Sur la page web qui s’ouvrira automatiquement, cliquez sur le lien `main.ipynb` pour l’ouvrir.

Lorsque vous êtes dans `main.ipynb`, lisez bien les instructions pour chaque cellule et écrivez vos réponses.  
Testez vos réponses dans chaque cellule et sauvegardez régulièrement votre travail. Jupyter Notebook enregistre normalement votre progression automatiquement, mais sauvegardez aussi manuellement par précaution.

## Objectifs

Vous vous souvenez de votre projet MySQL ? Dans ce lab, vous allez examiner quelques tables MySQL disponibles [ici](https://relational.fit.cvut.cz/dataset/Stats).  
Cette base de données contient un dump anonymisé de tout le contenu généré par les utilisateurs sur le réseau Stats Stack Exchange.

Vous devrez importer la bibliothèque `pymysql` et la fonction `create_engine` de la bibliothèque `sqlalchemy` :

```python
import pymysql
from sqlalchemy import create_engine
