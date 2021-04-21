import math
def converter(number):
    temp = number/60
    hours = int(temp)
    minutes = round(((temp-hours)*60))
    print(hours,end="")
    if hours == 1:
        print(" hour,", end="")
    else:
        print(" hours,",end="")
    
    print(minutes,end="")
    if minutes == 1:
        print(" minute", end="")    
    else:
        print(" minutes", end="")