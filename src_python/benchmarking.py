import time
from src_python.metodos_ordenamiento import bubble_sort, bubble_sort_mejorado, seleccion_sort, shell_sort

class Benchmarking:
    def run_benchmark(self):
        sizes = [1000, 2000, 4000]
        results = {
            "bubble": [],
            "bubbleMejorado": [],
            "seleccion": [],
            "shell": []
        }

        for size in sizes:
            data = list(range(size, 0, -1))

            for name, func in [
                ("bubble", bubble_sort),
                ("bubbleMejorado", bubble_sort_mejorado),
                ("seleccion", seleccion_sort),
                ("shell", shell_sort)
            ]:
                arr = data.copy()
                start = time.time()
                func(arr)
                end = time.time()
                results[name].append(end - start)

        return sizes, results
