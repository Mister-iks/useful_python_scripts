import os

def search_files(directory, pattern):
    try:
        found_files = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                if pattern in file:
                    found_files.append(os.path.join(root, file))
        return found_files
    except Exception as e:
        print("Erreur lors de la recherche de fichiers :", str(e))
try:
    directory = input("Chemin complet répertoire de recherche : ")
    pattern = input(
        "Terme de recherche (extension ou nom de fichier - sensible à la casse) : ")

    matched_files = search_files(directory, pattern)
    print("Fichiers trouvés :")
    for file in matched_files:
        print(file)
except FileNotFoundError:
    print("Erreur : Répertoire de recherche introuvable.")
except Exception as e:
    print("Erreur :", str(e))
