import urllib.request

def download_file(file_url: str):
    try:
        filename = input("Nom du fichier de destination + extension : ")
        urllib.request.urlretrieve(file_url, filename)
        print("Téléchargement terminé!")
    except urllib.error.URLError as e:
        print("Erreur lors du téléchargement :", e.reason)
    except Exception as e:
        print("Erreur lors du téléchargement :", str(e))

try:
    download_file("votre url ici")
except ValueError:
    print("Erreur : Veuillez entrer une URL valide.")
