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

def animal_crackers(text):
    '''

    :param text: a rendom string with two words
    :return: returns True if both words begin with same letter
    '''
    i = 0
    limit = len(text)
    for x in range (limit):
        if text[x]==' ':
            i = x
    if text[0]==text[i+1]:
         return True
    else:
        return False
    pass

def makes_twenty(n1,n2):
    '''

    :param n1: first integer
    :param n2: second integer
    :return:  return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
    '''
    if n1+n2==20 or n1==20 or n2==20:
        return True
    else:
        return False
    pass