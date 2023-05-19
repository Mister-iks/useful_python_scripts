import urllib.request

def download_file(file_url: str):
    filename = input("Nom du fichier de destination + extension : ")
    urllib.request.urlretrieve(file_url, filename)
    print("Téléchargement terminé!")

download_file("votre url ici")