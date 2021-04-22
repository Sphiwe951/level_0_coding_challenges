def maximum(*arguments):
    max_variable = arguments[0]

    for i in range(0,len(arguments)):
        if arguments[i] > max_variable:
            max_variable = arguments[i]
            
    return max_variable
