import csv


def read_csv(file):
    data = []
    with open(file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data


def write_csv(file, data):
    with open(file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in data:
            writer.writerow(row)
    print("Données écrites dans le fichier CSV.")


file = input("Nom du fichier CSV : ")

# Lecture du fichier CSV
csv_data = read_csv(file)
print("Données lues à partir du fichier CSV :")
for row in csv_data:
    print(row)

# Exemple d'écriture dans le fichier CSV
data_to_write = [['Colonne1', 'Colonne2'], ['Valeur1', 'Valeur2']]
write_csv(file, data_to_write)
