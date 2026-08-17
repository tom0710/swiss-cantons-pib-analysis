import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

file_path = BASE_DIR / "data" / "data_raw" / "cc-f-01.02.02.04.xlsx"

# Importer seulement les colonnes A et B
df = pd.read_excel(
    file_path,
    sheet_name="2024",
    skiprows=3,
    usecols="A:B",
    header=None
)

# Donner nous-mêmes les noms de colonnes
df.columns = ["canton", "population"]

# Voir les premières lignes pour contrôler
print(df.head(10))
print(df.columns)

# Supprimer les lignes vides
df = df.dropna(subset=["canton", "population"])

# Supprimer la ligne Suisse
df = df[df["canton"] != "Suisse"]

# Nettoyer la population si elle est en texte
df["population"] = (
    df["population"]
    .astype(str)
    .str.replace("'", "", regex=False)
)
df["population"] = pd.to_numeric(df["population"], errors="coerce")

# Supprimer les lignes où population n'est pas un nombre
df = df.dropna(subset=["population"])

# Trier par canton
df = df.sort_values("canton")

# Contrôle final
print(df.head())
print(df.shape)
print(df.dtypes)

# Exporter le fichier propre
df.to_csv(
    BASE_DIR / "data" / "data_clean" / "population_cantons_clean.csv",
    index=False
)