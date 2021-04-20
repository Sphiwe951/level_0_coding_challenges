def vowel_finder(name):
    size = len(name)
    counter = 0
    while counter < size:
        if name[counter] == "a" or name[counter] == "A":
            print(name[counter]+", ",end=' ')
        
        elif name[counter] == "e" or name[counter] == "E":
            print(name[counter]+", ",end=' ')
        
        elif name[counter] == "i" or name[counter] == "I":
            print(name[counter]+", ",end=' ')
        
        elif name[counter] == "o" or name[counter] == "O":
            print(name[counter]+", ",end=' ')
        
        elif name[counter] == "u" or name[counter] == "U":
            print(name[counter]+", ",end=' ')
        
        counter+=1