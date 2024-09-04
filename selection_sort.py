# SELECTION SORT

def selectionSort(array):
    
    # travers the whole array
    for i in range(len(array)-1):
        min_index = i
 
        for j in range(i + 1, len(array)):
            # if new minimum element is identified
            if array[j] < array[min_index]:
                min_index = j  # set new minimum index for future calculation
        # swap if out of order
        array[i], array[min_index] = array[min_index], array[i]


# Example Usage
# arr = [4, 67, 3, 6, 8, 94, 3, 52, 23, 87, 11, 31]
# print(f'Array before sorting: {arr}')
# selectionSort(arr)
# print(f'Array after sorting: {arr}')