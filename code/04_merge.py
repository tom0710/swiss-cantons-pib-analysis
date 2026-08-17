import pandas as pd
from pathlib import Path

# Partie 1 : Harmonisation des noms des cantons

BASE_DIR = Path(__file__).resolve().parent.parent#créer le lien du dossier de mon projet

population = pd.read_csv(BASE_DIR / "data" / "data_clean" / "population_cantons_clean.csv")#importer population

superficie = pd.read_csv(BASE_DIR / "data" / "data_clean" / "superficie_cantons_clean.csv")#importer superficie

pib_habitant = pd.read_csv(BASE_DIR / "data" / "data_clean" / "pib_habitant_clean.csv")#importer PIB par habitant

print(set(superficie["canton"])-set(population["canton"]))#Je vérifie les noms de cantons différent entre le fichier population et le fichier superficie

correspondance = {
    "Aargau": "Argovie",
    "Appenzell Ausserrhoden": "Appenzell Rh.-Ext.",
    "Appenzell Innerrhoden": "Appenzell Rh.-Int.",
    "Basel-Landschaft": "Bâle-Campagne",
    "Basel-Stadt": "Bâle-Ville",
    "Bern / Berne": "Berne",
    "Fribourg / Freiburg": "Fribourg",
    "Glarus": "Glaris",
    "Graubünden / Grigioni / Grischun": "Grisons",
    "Luzern": "Lucerne",
    "Nidwalden": "Nidwald",
    "Obwalden": "Obwald",
    "Schaffhausen": "Schaffhouse",
    "Schwyz": "Schwytz",
    "Solothurn": "Soleure",
    "St. Gallen": "Saint-Gall",
    "Thurgau": "Thurgovie",
    "Ticino": "Tessin",
    "Valais / Wallis": "Valais",
    "Zug": "Zoug",
    "Zürich": "Zurich"
}#dictionnaire qui fait la traduction

superficie["canton"] = superficie["canton"].replace(correspondance)#on remplace les noms des cantons par des noms français

superficie.to_csv(
    BASE_DIR / "data" / "data_clean" / "superficie_cantons_clean.csv",
    index=False
)

# Partie 2 : Fusion des jeux de données

cantons = pd.merge(
    population,
    superficie,
    on="canton"
)
cantons = pd.merge(
    cantons,
    pib_habitant,
    on="canton"
)

cantons["population"] = cantons["population"].astype(int)

cantons["densite_km2"] = (cantons["population"]/(cantons["superficie_ha"]/100)).round(2)

cantons = cantons[
    ["canton", "population", "superficie_ha", "densite_km2", "pib_hab"]
]

cantons.to_csv(
    BASE_DIR / "data" / "data_clean" / "cantons.csv",
    index=False
)
print(cantons.head())