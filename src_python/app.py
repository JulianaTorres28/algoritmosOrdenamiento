# app.py
from src_python.benchmarking import Benchmarking
from src_python.grafica import plot_graph

def main():
    benchmarking = Benchmarking()
    sizes, results = benchmarking.run_benchmark()
    plot_graph(sizes, results)

if __name__ == "__main__":
    main()
