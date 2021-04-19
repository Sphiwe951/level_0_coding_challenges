def maximum(*args):          #to pass in unknown number of arguments
    size = len(args)
    counter = 0
    maxi = 0
    while counter < size:
        if args[counter] > maxi:
            maxi = args[counter]
        counter +=1
    return maxi
