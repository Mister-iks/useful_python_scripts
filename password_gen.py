import random
import string


def generate_password(length):
    try:
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password
    except ValueError:
        print("Erreur : Veuillez fournir une longueur valide pour le mot de passe.")
    except Exception as e:
        print("Erreur lors de la génération du mot de passe :", str(e))

try:
    password_length = int(input("Longueur du mot de passe : "))
    generated_password = generate_password(password_length)
    print("Mot de passe généré :", generated_password)
except ValueError:
    print("Erreur : Veuillez entrer une longueur de mot de passe valide.")
