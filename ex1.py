def insertion_sort(arr):
    n = len(arr)
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key
    return arr

arr = [6, 7, 0, 1, 5]
print("unsorted = {}".format(arr))

sorted_arr = insertion_sort(arr)
print("sorted = {}".format(sorted_arr))

range = (max(arr) - min(arr))
print("range",range)


def SelectionSort(arr):
    n = len(arr)
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if arr[min] > arr[j]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr

arr = [6, 7, 0, 1, 5]
print("unsorted = {}".format(arr))
sorted_arr = SelectionSort(arr)
print("sorted = {}".format(sorted_arr))




def BubbleSort(arr):
    n = len(arr)
    for k in range(0, n):
        for j in range(0, n-k-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [5, 7, 2, 4, 9]
print("unsorted array = {}".format(arr))
sorted_arr = BubbleSort(arr)
print("sorted array = {}".format(sorted_arr))

