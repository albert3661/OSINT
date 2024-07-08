import csv
import os

# Chemin du fichier CSV original
input_csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'incubateurs-accelerateurs.csv')
# Chemin du fichier CSV nettoyé
output_csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'incubateurs-accelerateurs-nettoye.csv')

# Définir le nombre correct de champs (basé sur une ligne correcte)
correct_field_count = 35  # Remplacez ce nombre par le nombre correct de champs dans vos lignes

with open(input_csv_path, mode='r', encoding='utf-8') as input_file, \
     open(output_csv_path, mode='w', encoding='utf-8', newline='') as output_file:
    
    csv_reader = csv.reader(input_file, delimiter=';')
    csv_writer = csv.writer(output_file, delimiter=';')
    
    for row in csv_reader:
        if len(row) > correct_field_count:
            row = row[:correct_field_count]  # Truncate extra fields
        elif len(row) < correct_field_count:
            row.extend([''] * (correct_field_count - len(row)))  # Add missing fields
        
        csv_writer.writerow(row)

print(f"Fichier CSV nettoyé créé à: {output_csv_path}")
