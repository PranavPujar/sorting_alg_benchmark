from bubble_sort import bubbleSort
from insertion_sort import insertionSort
from selection_sort import selectionSort
import matplotlib.pyplot as plt
import time
import random


# returns the time difference between before and after a sorting function call
def benchmark(sorting_algorithm, array):
    start = time.time()
    sorting_algorithm(array)
    return time.time() - start


def show_statistics(array_sizes):

    plt.figure(figsize=(10, 6))
    plt.title('Benchmark: Selection Sort vs Insertion Sort vs Bubble Sort')
    plt.xlabel('Array Input Size (n)')
    plt.ylabel('Time to Sort (sec)')
    plt.plot(array_sizes, bubble_times, label='Bubble Sort', marker='-b')
    plt.plot(array_sizes, insertion_times, label='Insertion Sort', marker='-r')
    plt.plot(array_sizes, selection_times, label='Selection Sort', marker='-g')
    plt.legend()
    plt.grid(True)
    plt.show()

def process_benchmarks(array_sizes):
    for size in array_sizes:
        arr = [random.randint(1, 10000) for _ in range(size)]        
        
        selection_times, insertion_times, bubble_times = list(), list(), list()
        
        # Selection Sort
        selection_times.append(benchmark(selectionSort, arr.copy()))
        
        # Insertion Sort
        insertion_times.append(benchmark(insertionSort, arr.copy()))
        
        # Bubble Sort
        bubble_times.append(benchmark(bubbleSort, arr.copy()))

        return selection_times, insertion_times, bubble_times


if __name__ == "__main__":
    
    array_sizes = [5, 10, 50, 100, 500, 2000, 5000, 10000, 20000]
    selection_times, insertion_times, bubble_times = process_benchmarks(array_sizes)
    show_statistics(array_sizes)
