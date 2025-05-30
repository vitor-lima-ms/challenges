while True:
    try:
        n = int(input())

        if n == 0:
            break

        cards = [number for number in range(1, n + 1)]

        discard = list()
        while True:
            first = cards.pop(0)
            discard.append(first)
            
            second = cards.pop(0)
            cards.append(second)

            if len(cards) == 1:
                break

        print('Discarded cards: ', end='')
        for card in discard:
            if card == discard[-1]:
                print(f'{card}', end='\n')
                continue
            print(f'{card}, ', end='')
        
        print('Remaining card: ', end='')
        print(cards[0])

    except EOFError:
        break