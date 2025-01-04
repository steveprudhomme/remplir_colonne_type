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