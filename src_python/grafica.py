import matplotlib.pyplot as plt

def plot_graph(sizes, results):
    for name, times in results.items():
        plt.plot(sizes, times, marker='o', label=name)
    plt.title("Comparación de algoritmos de ordenamiento")
    plt.xlabel("Tamaño del arreglo")
    plt.ylabel("Tiempo de ejecución (s)")
    plt.legend()
    plt.grid(True)
    plt.show()
