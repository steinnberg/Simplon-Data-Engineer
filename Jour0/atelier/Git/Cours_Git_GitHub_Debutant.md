
# 📚 Cours : Premiers pas avec Git et GitHub

## 🎯 Objectifs du cours

- Comprendre ce qu’est **Git** et **GitHub**
- Installer Git sur son ordinateur
- Configurer Git pour la première fois
- Créer un dépôt local
- Lier son dépôt à GitHub
- Effectuer ses premières opérations : `add`, `commit`, `push`
- Cloner un projet existant
- Prendre de bonnes habitudes

## 🔑 1️⃣ Qu’est-ce que **Git** et **GitHub** ?

- **Git** est un logiciel de **gestion de versions** : il enregistre l’historique des modifications de tes fichiers.
- **GitHub** est une **plateforme en ligne** où tu peux héberger tes dépôts Git et collaborer avec d’autres.

## ⚙️ 2️⃣ Installation de **Git**

### 🪟 Pour Windows

1. Télécharger le programme d’installation : [git-scm.com](https://git-scm.com/)
2. Lancer l’installation et laisser les options par défaut (cocher “Git Bash”).
3. Vérifier l’installation :
   ```bash
   git --version
   ```

### 🍏 Pour macOS

```bash
brew install git
```
ou
```bash
xcode-select --install
```

### 🐧 Pour Linux (Debian/Ubuntu)

```bash
sudo apt update
sudo apt install git
```

## 🛠️ 3️⃣ Configuration initiale

Configure ton identité pour que Git sache qui tu es.

```bash
git config --global user.name "Ton Nom"
git config --global user.email "ton.email@example.com"
```

Vérifie :

```bash
git config --list
```

## 📂 4️⃣ Créer ton premier dépôt local

1. Crée un nouveau dossier et place-toi dedans :

   ```bash
   mkdir mon-projet
   cd mon-projet
   ```

2. Initialise Git dans ce dossier :

   ```bash
   git init
   ```

   ➜ Git va créer un sous-dossier caché `.git` pour gérer ton historique.

## 📝 5️⃣ Ajouter et valider des modifications

1. Crée un fichier `README.md` et écris quelque chose dedans.

2. Vérifie l’état du dépôt :

   ```bash
   git status
   ```

3. Ajoute le fichier à l’index :

   ```bash
   git add README.md
   ```

4. Valide le changement avec un **commit** :

   ```bash
   git commit -m "Ajoute le fichier README"
   ```

## ☁️ 6️⃣ Lier ton dépôt local à **GitHub**

1. Crée un compte sur [github.com](https://github.com) si ce n’est pas fait.
2. Crée un **nouveau dépôt vide** (nom, description, public ou privé).
3. Lien du dépôt (par ex. `https://github.com/toncompte/mon-projet.git`).

4. Lie ton dépôt local au dépôt distant :

   ```bash
   git remote add origin https://github.com/toncompte/mon-projet.git
   ```

5. Envoie ton premier commit :

   ```bash
   git branch -M main  # Renomme la branche principale en main
   git push -u origin main
   ```

## 📥 7️⃣ Cloner un projet existant

Pour récupérer un projet depuis GitHub :

```bash
git clone https://github.com/nomutilisateur/nomrepo.git
```

## 🔄 8️⃣ Cycle de travail courant

```bash
# Vérifie l’état
git status

# Ajoute les fichiers modifiés
git add .

# Fait un commit
git commit -m "Message clair"

# Envoie sur GitHub
git push
```

## ✅ 9️⃣ Bonnes pratiques

- Des **commits clairs et fréquents**.
- Un **README.md** pour décrire ton projet.
- Des **branches** pour séparer les fonctionnalités.
- Toujours **pull** avant de **push** quand on collabore.

```bash
git pull origin main
```

## 🚀 1️⃣0️⃣ Ressources pour aller plus loin

- [Pro Git Book](https://git-scm.com/book/fr/v2)
- [GitHub Docs](https://docs.github.com/fr)
- [Try Git](https://try.github.io/)

**👏 Bravo !**  
Tu maîtrises maintenant les bases pour gérer tes projets avec **Git** et **GitHub** 🚀✨
