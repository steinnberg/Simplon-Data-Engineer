##!pip install pandas

import pandas as pd
import sqlite3
from pathlib import Path

# 1) Charger le CSV ----------------------------------------------------------
csv_path = Path("C:\Users\Kered\Simplon-data-engineer\Jour4\resources\publications.csv")          # adapte le chemin si besoin
df = pd.read_csv(csv_path)

# 2) Créer / ouvrir la base SQLite ------------------------------------------
db_path = Path("C:\Users\Kered\Simplon-data-engineer\Jour4\labs\publications.db")            # la BDD sera créée à côté du script
conn = sqlite3.connect(db_path)

# 3) Copier le DataFrame dans une table SQLite ------------------------------
#    - if_exists="replace" : remplace la table si elle existe déjà
#    - index=False         : on n’écrit pas l’index pandas en colonne
df.to_sql(name="books", con=conn, if_exists="replace", index=False)

# 4) (optionnel) Vérifier qu’on a bien importé les données ------------------
cur = conn.cursor()
cur.execute("SELECT COUNT(*) FROM books;")
print("Lignes importées :", cur.fetchone()[0])

# 5) Fermer la connexion -----------------------------------------------------
conn.close()
print(f"Base SQLite créée : {db_path.resolve()}")
