# TP – Script Bash + planification CRON

## Objectif
Automatiser une tâche quotidienne à l’aide de bash + cron.

---

### Étapes

1. Créer un script `backup.sh` :
   - Archive un dossier `~/Documents/mon_projet`
   - Enregistre la date dans un fichier `log.txt`
   - Enregistre l’archive dans un dossier `~/Backups/`

2. Donner les droits d’exécution :
```bash
chmod +x backup.sh
```

3. Tester le script manuellement :
```bash
./backup.sh
```

4. Programmer le script avec `crontab` :
```bash
crontab -e
```

Ajouter cette ligne pour un test toutes les 2 minutes :
```
*/2 * * * * /chemin/vers/backup.sh
```

---

### Bonus

- Ajouter un test de présence du dossier avant backup
- Envoyer un email en cas d’échec (avec `mailx` ou `echo`)