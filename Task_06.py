def maximum(*arguments):         
    size = len(arguments)
    counter = 0
    max_variable = -2147483648
    while counter < size:
        if arguments[counter] > max_variable:
            max_variable = arguments[counter]
        counter +=1
    return max_variable