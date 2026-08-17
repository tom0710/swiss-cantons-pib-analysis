import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

df = pd.read_excel(
    BASE_DIR / "data" / "data_raw" / "Superficie.xlsx",
    sheet_name="Données"
    )

df = df[["KTNAME", "AREA_HA"]]#on garde que les colonnes KTNAME et AREA_HA

df.columns = ["canton", "superficie_ha"]#on renome les colonnes

print(df.isna().sum())#on verifie si il y a des valeurs manquantes

df = df.sort_values("canton")#on trie 

df.to_csv(
    BASE_DIR / "data" / "data_clean" / "superficie_cantons_clean.csv",
    index=False
)
print(df.head())#on sauvegarde