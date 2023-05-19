def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Erreur : Division par zéro"


try:
    num1 = float(input("Premier nombre : "))

    num2 = float(input("Deuxième nombre : "))

    print("Résultats :")
    print("Addition :", add(num1, num2))
    print("Soustraction :", subtract(num1, num2))
    print("Multiplication :", multiply(num1, num2))
    print("Division :", divide(num1, num2))

except ValueError:
    print("Erreur : Veuillez entrer des nombres valides.")
