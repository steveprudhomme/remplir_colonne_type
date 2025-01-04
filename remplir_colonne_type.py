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