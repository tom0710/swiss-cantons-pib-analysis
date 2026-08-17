import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Paramètres

BASE_DIR = Path(__file__).resolve().parent.parent

# Partie 1 : Importation des données

cantons = pd.read_csv(
    BASE_DIR / "data" / "data_clean" / "cantons.csv"
)

print(cantons.describe())
print(cantons.dtypes)
print(cantons[cantons["population"] == cantons["population"].max()]["canton"].values[0])
print(cantons[cantons["densite_km2"] == cantons["densite_km2"].max()]["canton"].values[0])
print(cantons[cantons["pib_hab"] == cantons["pib_hab"].max()]["canton"].values[0])
print(cantons[cantons["pib_hab"] == cantons["pib_hab"].min()]["canton"].values[0])

# Dataframe sans Bâle-Ville, Zoug et Genève
df = cantons[~cantons["canton"].isin(["Bâle-Ville", "Zoug", "Genève"])].copy()

#Affichage histogramme PIB par habitant

plt.figure(figsize=(8,5))

plt.hist(cantons["pib_hab"], bins=15)

plt.title("Distribution du PIB par habitant des cantons suisses (2022)")
plt.xlabel("PIB par habitant (CHF)")
plt.ylabel("Nombre de cantons")

plt.grid(alpha=0.2)

#plt.show()

#Scatterplot densité/PIB par habitant

plt.figure(figsize=(8,5))

plt.scatter(df["densite_km2"], df["pib_hab"])

plt.title("Densité de population et PIB par habitant")
plt.xlabel("Densité (hab./km²)")
plt.ylabel("PIB par habitant (CHF)")

for i, ligne in df.iterrows():
    plt.annotate(
        ligne["canton"],
        (ligne["densite_km2"],ligne["pib_hab"])
    )

plt.grid(alpha=0.3)

plt.show()

print(cantons["densite_km2"].corr(cantons["pib_hab"]))
print(df["densite_km2"].corr(df["pib_hab"]))