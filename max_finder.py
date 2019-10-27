def max_finder(numbers):
    '''
    :param numbers: Series of numbers that has been given input by the user
    :return: This will only return the maximum number among the inputs
    '''
    return max(numbers)


number =[]
while(1):
    a = input("Enter a number or to finish type E :").lower()
    if (a=='e'):
        break;
    else:
        number.append(int(a))
print(max_finder(number))