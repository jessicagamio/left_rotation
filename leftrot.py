

def rotate(array,d):
    """
    >>> rotate([1,2,3,4,5], 4)
    [5,1,2,3,4]
    """

    i = 0

    while i <= d
        array = array[1:]+array[0]
        i+= 1

    return array.join(" ")


if __name__=="__main__":
    import doctest
    doctest.testmod()