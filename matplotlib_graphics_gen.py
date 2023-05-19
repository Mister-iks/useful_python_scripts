import matplotlib.pyplot as plt

def graphics_gen(x: list[int], y: list[int], title: str):
    try:
        plt.plot(x, y)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title(title)
        plt.show()
    except Exception as e:
        print("Erreur lors de la génération du graphique :", str(e))

try:
    x_values = [1, 2, 3, 4, 5]
    y_values = [10, 20, 15, 25, 30]
    graphics_gen(x_values, y_values, "Graphique de test")
except ValueError:
    print("Erreur : Veuillez fournir des listes valides pour les valeurs x et y.")
