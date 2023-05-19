def celsius_to_fahrenheit(celsius):
    try:
        return (celsius * 9/5) + 32
    except Exception as e:
        print("Erreur lors de la conversion de la température :", str(e))


def kilometers_to_miles(kilometers):
    try:
        return kilometers * 0.621371
    except Exception as e:
        print("Erreur lors de la conversion de la distance :", str(e))


try:
    celsius = float(input("Température en degrés Celsius : "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print("Température en degrés Fahrenheit :", fahrenheit)

    kilometers = float(input("Distance en kilomètres : "))
    miles = kilometers_to_miles(kilometers)
    print("Distance en miles :", miles)

except ValueError:
    print("Erreur : Veuillez entrer des valeurs numériques valides.")
