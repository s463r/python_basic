def max_finder(numbers=0):
    '''
    :param numbers: Series of numbers that has been given input by the user
    :return: This will only return the maximum number among the inputs
    '''
    if (len(number)==0):
        return 'No number found'
    return max(numbers)


number =[]
while(1):
    a = input("Enter a number or to finish type E :").lower()
    if (a=='end'):
        break;
    else:
        number.append(float(a))
print(max_finder(number))
