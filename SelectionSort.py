#SELECTION SORT
#TIME COMPLEXITY: O(N^2)
#
def SelectionSort(arr):
    for i in range(len(arr)):
        min_index=i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index=j
                arr[i], arr[j] = arr[j], arr[i]
    
    return arr

#Driver Code
if __name__ == '__main__':
    arr=[64, 25, 12, 22, 10, 8, 11]
    print('Original Array: ', arr)
    print('Sorted Array: ',SelectionSort(arr))