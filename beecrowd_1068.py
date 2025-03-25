while True:
    try:
        expression = input()

        open_list = list()
        close_list = list()
        for char in expression:
            if char == '(':
                open_list.append(char)
            elif char == ')' and len(open_list) > 0:
                open_list.pop()
            elif char == ')' and len(open_list) == 0:
                close_list.append(char)
        
        if len(open_list) == 0 and len(close_list) == 0:
            print('correct')
        else:
            print('incorrect')
    except EOFError:
        break