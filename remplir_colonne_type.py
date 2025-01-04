# -*- coding: utf-8 -*-
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

def remplir_colonne_type(file_path: str, output_file_path: str) -> None:
    """
    Charger le fichier Excel, remplir les valeurs manquantes dans la première colonne,
    et sauvegarder le DataFrame mis à jour dans un nouveau fichier Excel.

    Load the Excel file, fill missing values in the first column, and save the updated DataFrame to a new Excel file.

    :param file_path: Chemin du fichier Excel à charger / Path to the Excel file to load
    :param output_file_path: Chemin du fichier Excel de sortie / Path to the output Excel file
    """
    # Charger le fichier Excel
    # Load the Excel file
    df = pd.read_excel(file_path, engine='openpyxl')
    
    # Assertion pour vérifier que le DataFrame n'est pas vide
    # Assertion to check that the DataFrame is not empty
    assert not df.empty, "Le fichier Excel est vide / The Excel file is empty"
    
    # Afficher les premières lignes pour vérifier les colonnes
    # Display the first few rows to check the columns
    print(df.head())
    
    # Remplir les valeurs manquantes dans la première colonne avec la valeur précédente de la colonne
    # Fill missing values in the first column with the previous value in the column
    df.iloc[:, 0] = df.iloc[:, 0].fillna(method='ffill')
    
    # Assertion pour vérifier que les valeurs manquantes ont été remplies
    # Assertion to check that missing values have been filled
    assert df.iloc[:, 0].isnull().sum() == 0, "Il reste des valeurs manquantes dans la première colonne / There are still missing values in the first column"
    
    # Sauvegarder le DataFrame mis à jour dans un fichier Excel
    # Save the updated DataFrame to a new Excel file
    df.to_excel(output_file_path, index=False)
    
    print(f"Le tableau mis à jour a été sauvegardé dans {output_file_path}.")
    print(f"The updated table has been saved to {output_file_path}.")

# Chemin du fichier Excel à charger et du fichier de sortie
# Path to the Excel file to load and the output file
file_path = 'tableConvert.com_o2we7a.xlsx.xlsx'
output_file_path = 'updated_table.xlsx'

# Appel de la fonction pour remplir la colonne et sauvegarder le fichier
# Call the function to fill the column and save the file
remplir_colonne_type(file_path, output_file_path)