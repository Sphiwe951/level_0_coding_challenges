def maximum(*args):         
    size = len(args)
    counter = 0
    maximum_var = 0
    while counter < size:
        if args[counter] > maximum_var:
            maximum_var = args[counter]
        counter +=1
    return maximum_var