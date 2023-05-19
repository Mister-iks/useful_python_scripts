from PIL import Image
def thumbnail_gen(width: int, height: int):
    try:
        image_file = input("Nom du fichier image : ")
        thumbnail_size = (width, height)

        image = Image.open(image_file)
        image.thumbnail(thumbnail_size)

        thumbnail_file = "thumbnail.jpg"
        image.save(thumbnail_file)
        print("Miniature créée :", thumbnail_file)
    except FileNotFoundError:
        print("Erreur : Fichier image introuvable.")
    except Exception as e:
        print("Erreur lors de la génération de la miniature :", str(e))

try:
    thumbnail_gen(300, 300)
except ValueError:
    print("Erreur : Veuillez entrer des dimensions valides pour la miniature.")
