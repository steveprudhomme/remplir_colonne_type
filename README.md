# Remplir Colonne Type

## Description

Ce script Python a pour but de remplir les valeurs manquantes dans la première colonne d'un fichier Excel avec la valeur précédente de la colonne. Cela est particulièrement utile pour les tableaux où certaines cellules de la première colonne sont vides mais devraient contenir la même valeur que la cellule précédente.

## Fonctionnement

Le script charge un fichier Excel, remplit les valeurs manquantes dans la première colonne avec la valeur précédente, puis sauvegarde le tableau mis à jour dans un nouveau fichier Excel.

## Origine du Fichier Excel

Le fichier Excel utilisé dans ce script provient du **Catalogue Exotica** de Breakthrough Listen, un projet de recherche de l'Université de Californie à Berkeley. Le Catalogue Exotica est une collection de plus de 700 objets célestes distincts, visant à inclure "un de chaque" type d'objet astronomique connu. Il comprend des exemples de chaque type dans l'échantillon Prototype, des objets extrêmes avec des propriétés record dans l'échantillon Superlative, et des cibles énigmatiques dans l'échantillon Anomaly.

Le fichier Excel a été extrait du code source de l'article scientifique "One of Everything: The Breakthrough Listen Exotica Catalog" disponible sur arXiv. La conversion du tableau LaTeX en fichier Excel a été réalisée à l'aide du convertisseur en ligne disponible sur TableConvert.

## Prérequis

- Python 3.x
- Pandas
- Openpyxl

## Installation des prérequis

Pour installer Python, vous pouvez le télécharger et l'installer depuis le site officiel : Python.org.

Pour installer les bibliothèques nécessaires, vous pouvez utiliser `pip` :

```bash
pip install pandas openpyxl
```
## Médiagraphie

Breakthrough Listen. (n.d.). Exotic Target Catalog. Récupéré de http://seti.berkeley.edu/exotica/
Lacki, B. C., Lebofsky, M., Isaacson, H., Siemion, A., Sheikh, S., Croft, S., ... & Werthimer, D. (2020). One of Everything: The Breakthrough Listen Exotica Catalog. arXiv. Récupéré de https://arxiv.org/pdf/2006.11304.pdf
Python Software Foundation. (2023). Pandas documentation. Repéré le 4 janvier 2025 à https://pandas.pydata.org/pandas-docs/stable/
Python Software Foundation. (2023). Openpyxl documentation. Repéré le 4 janvier 2025 à https://openpyxl.readthedocs.io/en/stable/
TableConvert. (n.d.). Convert LaTeX Table to Excel Online. Récupéré de https://tableconvert.com/latex-to-excel

## Journal des modifications
### 2025-01-02 21h35
Il semble que le script ait rencontré une erreur car la colonne "Type" n'a pas été trouvée dans le fichier Excel. J'ai ajusté le script pour qu'il fonctionne correctement avec votre fichier. Voici le script mis à jour :

```python

import pandas as pd

# Charger le fichier Excel
file_path = 'tableConvert.com_o2we7a.xlsx.xlsx'
df = pd.read_excel(file_path, engine='openpyxl')

# Afficher les premières lignes pour vérifier les colonnes
print(df.head())

# Remplir les valeurs manquantes dans la première colonne avec la valeur précédente de la colonne
df.iloc[:, 0] = df.iloc[:, 0].fillna(method='ffill')

# Sauvegarder le DataFrame mis à jour dans un fichier Excel
output_file_path = 'updated_table.xlsx'
df.to_excel(output_file_path, index=False)

print(f"Le tableau mis à jour a été sauvegardé dans {output_file_path}.")
```

Ce script utilise `iloc` pour cibler la première colonne du DataFrame, ce qui devrait résoudre le problème de la colonne "Type" introuvable. Vous pouvez enregistrer ce script dans un fichier nommé `remplir_colonne_type.py` et l'exécuter pour remplir les trous dans la colonne "Type" de votre fichier Excel.

J'ai également exécuté ce script pour vous et le tableau mis à jour a été sauvegardé dans un fichier Excel. Vous pouvez télécharger le fichier mis à jour ici : updated_table.xlsx.


### 2025-01-02 21h31

J'ai essayé de remplir les trous dans la colonne "Type" de votre fichier Excel, mais j'ai rencontré une erreur. Il semble que la colonne "Type" n'existe pas dans le fichier tel qu'il est actuellement formaté.

Pour résoudre ce problème, je vais vérifier et ajuster le script pour m'assurer qu'il fonctionne correctement avec votre fichier Excel. Voici le script mis à jour :

```python
import pandas as pd

# Charger le fichier Excel
file_path = 'tableConvert.com_o2we7a.xlsx.xlsx'
df = pd.read_excel(file_path, engine='openpyxl')

# Afficher les premières lignes pour vérifier les colonnes
print(df.head())

# Remplir les valeurs manquantes dans la colonne 'Type' avec la valeur précédente de la colonne
df['Type'] = df['Type'].fillna(method='ffill')

# Sauvegarder le DataFrame mis à jour dans un fichier Excel
output_file_path = 'updated_table.xlsx'
df.to_excel(output_file_path, index=False)

print(f"Le tableau mis à jour a été sauvegardé dans {output_file_path}.")
```



### 2025-01-02 21h29
J'ai créé un script Python pour remplir les trous dans la colonne "Type" de votre tableau. Voici le script :

```python
import pandas as pd
from io import StringIO

# Données fournies sous forme de chaîne de caractères
data = """
Type	Subtype	Prototype	ID	Solar?	Ref
Asteroid	A-type	446 Aeternitas	001	\checkmark	\nodata
	C-type	52 Europa	002	\checkmark	B02
	D-type	624 Hektor	003	\checkmark	\nodata
	E-type	434 Hungaria	004	\checkmark	B02
	M-type	16 Psyche	005	\checkmark	\nodata
	O-type	3628 Bo\v{z}n\v{e}mcov\'a	006	\checkmark	B02
	P-type	420 Bertholda	007	\checkmark	\nodata
	Q-type	1862 Apollo	008	\checkmark	B02, T84
	R-type	349 Dembowska	009	\checkmark	B02, T84
	S-type	15 Eunomia	010	\checkmark	\nodata
	T-type	233 Asterope	011	\checkmark	\nodata
	V-type	4 Vesta	012	\checkmark	B02, T84
	Binary (double)	90 Antiope	013	\checkmark	\nodata
	Asteroid satellite	Dactyl	014	\checkmark	\nodata
	Mercury-crossers	3200 Phaethon	015	\checkmark	\nodata
	Vatira	2020 AV$_2$	016	\checkmark	\nodata
	Venus co-orbital	(322756) 2001 CK$_{32}$	017	\checkmark	\nodata
	Atira	163693 Atira	018	\checkmark	\nodata
	Aten	3753 Cruithne	019	\checkmark	\nodata
	Arjuna	1991 VG	020	\checkmark	\nodata
	Apollo	1862 Apollo	008	\checkmark	\nodata
	Earth Trojan	2010 TK$_7$	021	\checkmark	\nodata
	Earth horseshoe	3753 Cruithne	019	\checkmark	\nodata
	Earth quasisatellite	(469219) Kamo'oalewa	022	\checkmark	\nodata
	Earth Kozai librator	4660 Nereus	023	\checkmark	\nodata
	Amor	433 Eros	024	\checkmark	\nodata
	Mars Trojan	5261 Eureka	025	\checkmark	\nodata
	Hungaria	434 Hungaria	004	\checkmark	\nodata
	Flora	8 Flora	026	\checkmark	\nodata
	Main Belt Zone I	4 Vesta	012	\checkmark	\nodata
	Phocaea	25 Phocaea	027	\checkmark	\nodata
	Main Belt Zone II	15 Eunomia	010	\checkmark	\nodata
	Main Belt Zone III	52 Europa	002	\checkmark	\nodata
	Cybele	65 Cybele	028	\checkmark	\nodata
	Hilda	153 Hilda	029	\checkmark	\nodata
	Jupiter Trojan	624 Hektor	003	\checkmark	\nodata
Comet	Typical composition	6P/d'Arrest	030	\checkmark	\nodata
	Carbon-chain depleted	21P/Giacobini-Zinner	031	\checkmark	1
	Active	1P/Halley	032	\checkmark	\nodata
	Manx	C/2014 S3 (PAN-STARRS)	033	\checkmark	\nodata
	Extinct (Damocloid)	5335 Damocles	034	\checkmark	2
	Falling evaporating bodies	$\beta$ Pic	035		\nodata
	Encke-type	2P/Encke	036	\checkmark	\nodata
	Main belt comet	133P/Elst-Pizarro	037	\checkmark	3
	Jupiter-family	9P/Tempel 1	038	\checkmark	\nodata
	Chiron-type	95P/Chiron	039	\checkmark	4
	Halley-type	1P/Halley	032	\checkmark	\nodata
	Long-period	153P/Ikeya-Zhang	040	\checkmark	\nodata
"""

# Lire les données dans un DataFrame
df = pd.read_csv(StringIO(data), sep='\t')

# Remplir les valeurs manquantes dans la colonne 'Type' avec la valeur précédente de la colonne
df['Type'] = df['Type'].fillna(method='ffill')

# Afficher le DataFrame mis à jour
print(df)
```

Ce script lit les données fournies dans un DataFrame, puis remplit les valeurs manquantes dans la colonne "Type" avec la valeur précédente de la colonne. Vous pouvez exécuter ce script pour obtenir le tableau mis à jour. 
