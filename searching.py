

def binary_search(input_array, value):
    """
    expects a sorted list and a value to search for in the list

    param: input_array
    param: value
    """

    if value > input_array[-1]:
        return -1

    copy_array = input_array[:]
    while len(copy_array) > 1:
        midpoint = ( len(copy_array) + 1 ) // 2
        check_value = copy_array[midpoint - 1]
        if check_value == value:
            return input_array.index(value)
        elif value > check_value:
            copy_array = copy_array[midpoint:]
            continue
        else:
            copy_array = copy_array[:midpoint]
            continue

    if copy_array[-1] == value:
        return input_array.index(value)
    else:
        return -1

def recursive_binary_search():
    pass
