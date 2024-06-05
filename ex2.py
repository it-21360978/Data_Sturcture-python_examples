def insertion(array):
    n=len(array)

    for i in range(1,n):
        key = array[i]
        j=i-1
        while j>=0 and key<array[j]:
            array[j+1] = array[j]
            j = j-1
        array[j+1]=key
    return array


array = [2,7,0,3]
print("unsorted:{}".format(array))

insertion(array)
print("array:{}".format(array))


def selection(array):
    n = len(array)

    for i in range(n):
        min = i
        for j in range(i+1,n):
            if array[min]> array[j]:
                min = j
                array[i],array[min] = array[min],array[i]
    return array

array=[1,5,3,9]
print("array:={}".format(array))
selection(array)
print("array:={}".format(array))
