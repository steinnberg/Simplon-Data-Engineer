# Atelier – Diagnostic via logs

## Objectif
Analyser un comportement inattendu d’un script ou d’un cron.

---

### Étapes

1. En binôme, simulez un script contenant une erreur (chemin faux, nom erroné…).
2. Tentez de trouver la cause dans les logs :
   - `/var/log/syslog` (Linux)
   - `~/.cron.log` ou `journalctl`
3. Proposez une solution : test, echo, log dans fichier, etc.