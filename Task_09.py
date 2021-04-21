def vowel_finder(name):
    vowels = ""
    for i in name:
        if "A" == i or "a" == i and ("a" not in vowels):
            vowels += 'a'
        if "E" == i or "e" == i and ("e" not in vowels):
            vowels += 'e'
        if "I" == i or "i" == i and ("i" not in vowels):
            vowels += 'i'
        if "O" == i or "o" == i and ("o" not in vowels):
            vowels += 'o'
        if ("U" == i or "u" == i) and ("u" not in vowels):
            vowels += 'u'
   
    
    print_vowels = ""
    for i in range(0,len(vowels)-1):
        print_vowels += f'{vowels[i]}, '
    print_last_vowels = f'{vowels[len(vowels)-1]}'
    
    print(print_vowels+print_last_vowels)
    
    