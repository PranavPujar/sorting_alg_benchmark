# BUBBLE SORT

def bubbleSort(arr):
    # n iterations of the outer loop
    for n in range(len(arr) - 1, 0, -1):

        for i in range(n):
            if arr[i] > arr[i + 1]:  # adjacent element comparison
                swapped = True  # flag needs to be set when swap operation occurs
                arr[i], arr[i + 1] = arr[i + 1], arr[i]  # Swap elements if they are in the wrong order
    
    # no need to return arr, it is passed by reference

# # Example Usage
# arr = [4, 67, 3, 6, 8, 94, 3, 52, 23, 87, 11, 31]
# print(f'Array before sorting: {arr}')
# bubbleSort(arr)
# print(f'Array after sorting: {arr}')
