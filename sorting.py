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
    
