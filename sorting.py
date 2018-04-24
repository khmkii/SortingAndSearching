def bubble_sort(value_array):
    n = len(value_array)
    while n > 0:
        for i in range(n):
            try:
                first = value_array[i]
                second = value_array[i+1]
            except IndexError:
                pass
            else:
                if first > second:
                    value_array[i] = second
                    value_array[i + 1] = first
        n = n-1


def partition(arr,low,high):
    i = ( low-1 )
    pivot = arr[high]

    for j in range(low , high):
        if   arr[j] <= pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )


def quickSort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
