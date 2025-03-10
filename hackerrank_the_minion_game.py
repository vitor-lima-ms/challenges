def minion_game(string: str):

    LEN_S  = len(string)
    string = string.upper()

    """Consonant"""
    consonants_list = list()

    counter = int()
    for letter1 in string:
        if letter1 not in 'AEIOU':
            consonant_word = str()
            for letter2 in string[counter:LEN_S]:
                consonant_word += letter2
                consonants_list.append(consonant_word)
            counter += 1
            continue
        
        counter += 1

    for consonant_word in consonants_list:
        while consonants_list.count(consonant_word) > 1:
            consonants_list.remove(consonant_word)
    
    print(consonants_list)

    """Vowel"""
    vowels_list = list()

    counter = int()
    for letter1 in string:
        if letter1 in 'AEIOU':
            vowel_word = str()
            for letter2 in string[counter:LEN_S]:
                vowel_word += letter2
                vowels_list.append(vowel_word)
            counter += 1
            continue
        
        counter += 1

    for vowel_word in vowels_list:
        while vowels_list.count(vowel_word) > 1:
            vowels_list.remove(vowel_word)
    
    print(vowels_list)

    """Calculating points"""
    consonant_points = int()
    for consonant_word in consonants_list:
        consonant_points += string.count(consonant_word)

    vowel_points = int()
    for vowel_word in vowels_list:
        vowel_points += string.count(vowel_word)

    """Assigning points to players"""
    stuart_list = ['Stuart', consonant_points]
    kevin_list = ['Kevin', vowel_points]

    """Checking the winner"""
    if stuart_list[1] > kevin_list[1]:
        print(f'{stuart_list[0]} {stuart_list[1]}')
    elif stuart_list[1] < kevin_list[1]:
        print(f'{kevin_list[0]} {kevin_list[1]}')
    else:
        print('Draw')

s = input()

minion_game(s)