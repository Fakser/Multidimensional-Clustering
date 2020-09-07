from controller import *

def is_iter(variable):
    """
    Function that can be used to find 
    wheter object is iterable

    Args:
        variable (object): ariable to be checked

    Returns:
        True: variable is iterable
        True: variable is not iterable
    >>> from losses import is_iter
    >>> is_iter([1,2])
    True
    >>> is_iter("hello")
    >>> is_iter(6)
    False
    """
    try:
        _  = (a for a in range(len(variable)))
    except:
        return False
    return True

def recursive_min(array, min_val = None):
    if is_iter(array):
        for data in array:
            if is_iter(data):
                min_val = recursive_min(data, min_val)
            elif (min_val and min_val > data) or (min_val == None):
                min_val = data
    else:
        if (min_val and min_val > array) or (min_val == None):
            min_val = array
    return min_val



def recursive_max(array, max_val = None):
    if is_iter(array):
        for data in array:
            if is_iter(data) == True:
                max_val = recursive_max(data, max_val)
            elif (max_val and max_val < data) or (max_val == None):
                max_val = data
    else:
        if (max_val and max_val < array) or (max_val == None):
            max_val = array
    return max_val

def recursive_list(array):
    if is_iter(array):
        for data_index in range(len(array)):
            if is_iter(array[data_index]) == True:
                array[data_index] = recursive_list(array[data_index])
        return list(array)
    else:
        return array
            
def recursive_nparray(array):
    if is_iter(array):
        for data_index in range(len(array)):
            if is_iter(array[data_index]) == True:
                array[data_index] = recursive_nparray(array[data_index])
        return np.array(array)
    else:
        return array

def recursive_mean(array):
    if len(array) > 0:
        np_array = recursive_nparray(deepcopy(array))
        mean_of_np_array = np_array[0]
        for data in np_array[1:]:
            mean_of_np_array += data
        return recursive_list(mean_of_np_array/len(np_array))
    else:
        return array
