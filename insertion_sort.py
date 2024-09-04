# INSERTION SORT

def insertionSort(arr):
    n = len(arr)  
      
    # handle edge case where array is too small
    if n <= 1:
        return
 
    for i in range(1, n):  
        key = arr[i]  
        j = i-1
        while j >= 0 and key < arr[j]:  
            # array elements are shifted
            arr[j+1] = arr[j]  
            j -= 1
        
        arr[j+1] = key  # restore the value of arr[j+1]

    # array passed by reference, no need to return

# # Example Usage
# arr = [4, 67, 3, 6, 8, 94, 3, 52, 23, 87, 11, 31]
# print(f'Array before sorting: {arr}')
# insertionSort(arr)
# print(f'Array after sorting: {arr}')