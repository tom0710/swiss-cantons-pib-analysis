# Analyse économique des cantons suisses

## Objectif

Ce projet a pour objectif d'explorer les différences entre les cantons suisses et d'étudier la relation entre la densité de population et le PIB par habitant.

Il constitue également un projet concret d'apprentissage de l'analyse de données avec Python, couvrant l'ensemble du processus, de la recherche et de la collecte des données à leur nettoyage, leur traitement, leur visualisation et leur analyse.

## Sommaire

- [Données](#données)
- [Méthodologie](#méthodologie)
- [Analyse](#analyse)
- [Résultats](#résultats)
- [Limites](#limites)
- [Structure du projet](#structure-du-projet)
- [Technologies utilisées](#technologies-utilisées)

## Données

Les données utilisées dans ce projet proviennent de l'Office fédéral de la statistique (OFS).

Les principales données utilisées sont :

- **Population cantonale (2024)** : [Office fédéral de la statistique (OFS) – Population résidante permanente et non permanente selon le canton](https://www.bfs.admin.ch/bfs/rm/home.assetdetail.36139710.html)
- **Superficie des cantons (2025)** : [Office fédéral de la statistique (OFS) – Chiffres clés géographiques des cantons](https://www.agvchapp.bfs.admin.ch/fr/kennzahlen/results?IncArea=True&SnapshotDate=01.01.2025&Unit=Cantons)
- **PIB par habitant (2022)** : [Office fédéral de la statistique (OFS) – PIB par habitant](https://www.bfs.admin.ch/asset/fr/32627395)

Les données originales sont conservées dans le dossier `data/data_raw/`.

Les données nettoyées et préparées pour l'analyse sont disponibles dans `data/data_clean/`.

Les données brutes sont conservées afin de permettre de reproduire les différentes étapes de nettoyage et de préparation des données.

## Méthodologie

Le traitement des données est réalisé en plusieurs étapes :

1. Importation des données originales.
2. Nettoyage des données.
3. Harmonisation des noms des cantons.
4. Sélection et transformation des variables.
5. Fusion des différents jeux de données.
6. Calcul de la densité de population.
7. Analyse statistique et visualisation des données.

L'analyse est ensuite réalisée à l'aide de statistiques descriptives, de graphiques et d'une régression linéaire.

## Analyse

L'analyse porte principalement sur la relation entre la densité de population et le PIB par habitant.

Un nuage de points est utilisé afin de visualiser cette relation. Une droite de régression linéaire est ensuite ajoutée afin d'étudier la relation entre les deux variables.

Le coefficient de corrélation et le coefficient de détermination R² sont utilisés afin de mesurer la force de cette relation.

Une analyse des observations atypiques est également réalisée afin d'étudier leur influence sur les résultats.

## Résultats

Pour l'ensemble des 26 cantons, le coefficient de corrélation entre la densité de population et le PIB par habitant est de **0,748**.

Le coefficient de détermination est de **0,559**. La relation linéaire avec la densité est ainsi associée à environ 55,9 % de la variation du PIB par habitant dans cet échantillon.

L'analyse met toutefois en évidence plusieurs observations atypiques, notamment Bâle-Ville, Zoug et Genève.

Après exclusion de ces trois cantons, le coefficient de corrélation diminue à **0,328** et le R² à environ **0,108**.

Ces résultats montrent que la relation observée est fortement influencée par quelques observations particulières.

## Limites

Cette analyse repose sur seulement 26 observations, correspondant aux cantons suisses.

La régression utilisée est une régression linéaire simple et ne prend en compte que la densité de population. D'autres facteurs économiques peuvent également être liés au PIB par habitant.

Enfin, l'analyse met en évidence une association statistique mais ne permet pas d'établir une relation causale entre la densité de population et le PIB par habitant.

## Structure du projet

```text
swiss-cantons-pib-analysis/
│
├── code/
│   ├── 01_population.py
│   ├── 02_superficie.py
│   ├── 03_PIB.py
│   └── 04_merge.py
│
├── data/
│   ├── data_raw/
│   └── data_clean/
│
├── notebooks/
│   └── 05_analyse.ipynb
│
├── .gitignore
└── README.md