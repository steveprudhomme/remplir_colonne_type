 -*- coding: utf-8 -*-
"""
Remplir Colonne Type

Description:
Ce script Python a pour but de remplir les valeurs manquantes dans la première colonne d'un fichier Excel avec la valeur précédente de la colonne. Cela est particulièrement utile pour les tableaux où certaines cellules de la première colonne sont vides mais devraient contenir la même valeur que la cellule précédente.

Functionality:
This Python script aims to fill in missing values in the first column of an Excel file with the previous value in the column. This is particularly useful for tables where some cells in the first column are empty but should contain the same value as the previous cell.

License:
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""

import pandas as pd

# Charger le fichier Excel
# Load the Excel file
file_path = 'tableConvert.com_o2we7a.xlsx.xlsx'
df = pd.read_excel(file_path, engine='openpyxl')

# Afficher les premières lignes pour vérifier les colonnes
# Display the first few rows to check the columns
print(df.head())

# Remplir les valeurs manquantes dans la première colonne avec la valeur précédente de la colonne
# Fill missing values in the first column with the previous value in the column
df.iloc[:, 0] = df.iloc[:, 0].fillna(method='ffill')

# Sauvegarder le DataFrame mis à jour dans un fichier Excel
# Save the updated DataFrame to a new Excel file
output_file_path = 'updated_table.xlsx'
df.to_excel(output_file_path, index=False)

print(f"Le tableau mis à jour a été sauvegardé dans {output_file_path}.")
print(f"The updated table has been saved to {output_file_path}.")