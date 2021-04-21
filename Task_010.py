def common_char(name1, name2):
    size1 = len(name1)
    size2 = len(name2)
    smallest = 0
    largest = 0
    counter = 0
    counter2 = 0
    common_chars = ""
    print_chars = ""

    if size1 < size2:
        smallest = size1
        name_small = name1
        largest = size2
        name_large = name2
    else:
        smallest = size2
        name_small = name2
        largest = size1
        name_large = name1
    
    while counter < smallest:
        counter2 = 0
        while counter2 < largest:
            if name_small[counter] == name_large[counter2]:
                common_chars += name_small[counter]
            counter2 += 1
        counter += 1
    
    for i in range(0,len(common_chars)-1):
        print_chars += f'{common_chars[i]}, '
    print_last_char = f'{common_chars[len(common_chars)-1]}'
    print(print_chars + print_last_char)
