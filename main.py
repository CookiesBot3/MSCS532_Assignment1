#This function returns a decreasing order of a sorted array.
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key > arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

array1 = [3,4,5,1,2,6]
array2 = [13,35,1,43,67]
insertionSort(array1)
insertionSort(array2)
print(array1) #[6, 5, 4, 3, 2, 1]
print(array2) #[67, 43, 35, 13, 1]