# Sorting Algorithms

This repo contains implementations of **Selection Sort**, **Insertion Sort**, and **Bubble Sort** in Python. It also contains benchmarks of these different sorting algorithms visualized using Matplotlib.

## Benchmark - Sorting Algorithms

### Environment

- **Python Version**: 3.11.5
- **Processor/Chip**: Apple M2 Pro (16-core CPU)
- **Operating System**: macOS 14.4.1 (23E224)
- **RAM**: 16 GB
- **Storage**: 1TB Macintosh HD
- **Dependencies**: `timeit`, `matplotlib`

### Benchmark

![sorting_algorithms_benchmark]() add image here

### Proving Selection Sort's Correctness

This is a method of sorting an array by iteratively identifying the minimum element in the unsorted portion and swapping it with the first unsorted element.

This process continues until the array is fully sorted. We can establish Selection Sort’s correctness by means of using a "loop invariant".

## Loop Invariant

Invariant: As the name suggests, it "does not vary". At the start of each outer loop iteration (indexed by i), the subarray array[0..i-1] contains the i smallest elements of the full array, sorted in non-decreasing order.

## Inductive Proof

One way to prove/argue Selection Sort’s correctness is by showing that the loop "invariant" holds across the three phases of the sorting process: Initialization, Maintenance, and Termination.

1. Initialization
   Before the first loop iteration (i = 0), the subarray array[0..i-1] is empty, trivially maintaining the invariant (as zero elements are sorted).

2. Maintenance
   Assume the invariant holds prior to the i-th iteration: array[0..i-1] contains the i smallest elements, sorted. In the i-th iteration, the algorithm scans array[i..n-1] to find the smallest element, and swaps this element with array[i], extending the sorted subarray to array[0..i]. After the swap, array[0..i] contains the smallest i+1 elements, sorted, thus maintaining the invariant.

3. Termination
   The loop terminates when i = n-1. At this point, array[0..n-2] holds the n-1 smallest elements, sorted. The final element (array[n-1]) must be the largest and is already in place.

## Conclusion

By mathematical induction, the loop invariant holds throughout all iterations. So we can state that Selection Sort correctly sorts the array for any input.

## **Environment Setup**

### 1. Install Python

Ensure that Python 3.11.5 (or later) is installed on your machine.

### 2. Set Up Your Environment

Two dependencies need to be installed by running the following commands:

```sh
pip install timeit
pip install matplotlib
```
