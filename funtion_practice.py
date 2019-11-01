def lesser_of_two_evens(a,b):
    '''

    :param a: first number
    :param b: second number
    :return: returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
    '''
    if a%2==0 and b%2==0:
        if a>b:
            return b
        elif b>a:
            return a
    elif a%2!=0 or b%2!=0:
        if a<b:
            return b
        elif b<a:
            return a
    pass