def minion_game(string: str):
    LEN_S  = len(string)
    string = string.upper()

    consonants_list = list()
    vowels_list = list()

    """The number of words that can be made from a letter is equal to the length of the string that starts with it and goes to the end of the original string."""
    counter = int()
    for letter in string:
        if letter not in 'AEIOU': 
            consonants_list.append(len(string[counter:LEN_S]))
            counter += 1
        elif letter in 'AEIOU':
            vowels_list.append(len(string[counter:LEN_S]))
            counter += 1

    if sum(consonants_list) > sum(vowels_list):
        print(f'Stuart {sum(consonants_list)}')
    elif sum(consonants_list) == sum(vowels_list):
        print('Draw')
    else:
        print(f'Kevin {sum(vowels_list)}')