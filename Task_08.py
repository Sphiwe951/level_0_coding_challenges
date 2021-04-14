def converter(number):
    temp = number/60
    hours = int(temp)
    minutes = int((temp-hours)*60)
    if hours == 1:
        print(hours , end="")
        print(" hour,", end="")
    else:
        print(hours, end="")
        print(" hours,",end="")
    
    if minutes == 1:
        print(minutes , end="")
        print(" minute", end="")    
    else:
        print(minutes , end="")
        print(" minutes", end="")