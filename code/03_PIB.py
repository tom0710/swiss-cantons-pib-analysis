import pandas as pd
from pathlib import Path

# Paramètres

BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)

# Importation des données

pib_habitant = pd.read_excel(
    BASE_DIR / "data" / "data_raw" / "PIB_par_habitant.xlsx",
    sheet_name="PIB cantonal par habitant",
    header=2,
    nrows=27
)

# Selection des colonnes

pib_habitant = pib_habitant[["Canton","2022p"]]

pib_habitant = pib_habitant.drop(index=0)

pib_habitant = pib_habitant.reset_index(drop=True)

pib_habitant["2022p"] = (pib_habitant["2022p"].astype(float)).round(2)

pib_habitant.columns = ["canton","pib_hab"]# Renome les colonnes

pib_habitant = pib_habitant.sort_values("canton")

correspondance = {
    "Appenzell Rhodes-Extérieures": "Appenzell Rh.-Ext.",
    "Appenzell Rhodes-Intérieures": "Appenzell Rh.-Int.",
}

pib_habitant["canton"] = pib_habitant["canton"].replace(correspondance)

print(pib_habitant.head(27))
print(pib_habitant.columns)

pib_habitant.to_csv(
    BASE_DIR / "data" / "data_clean" / "pib_habitant_clean.csv",
    index=False
)


