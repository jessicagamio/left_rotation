

def rotate(array,d):
    """
    >>> rotate([1,2,3,4,5], 4)
    '5 1 2 3 4'
    """

    i = 0

    while i < d:
        array = array[1:]+ [array[0]]
        i+= 1

        string_array=[str(i) for i in array]

    return " ".join(string_array)


if __name__=="__main__":
    import doctest
    doctest.testmod()