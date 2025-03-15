while True:
    try:
        from random import randint

        N = input()

        if not N:
            break

        N = int(N)

        bi_array = [[] for _ in range(N)]

        for sub_array in bi_array:
            while len(sub_array) < N:
                sub_array.append(randint(1, 3))
        
        for sub_array in bi_array:
            index = 0
            while index < N:
                if index == (N - 1):
                    print(sub_array[index])
                    index += 1

                else:
                    print(sub_array[index], end='')
                    index += 1

    except EOFError:
        break