while True:
    try:
        from random import randint

        N = int(input())

        bi_array = [[] for _ in range(N)]

        for sub_array in bi_array:
            while len(sub_array) < N:
                sub_array.append(0)
        
        one_index = int()
        two_index = -1
        new_bi_array = list()
        for sub_array in bi_array:
            sub_array[one_index] = 1
            sub_array[two_index] = 2
            
            new_sub_array = [n if n != 0 else 3 for n in sub_array]
            new_bi_array.append(new_sub_array)
            
            one_index += 1
            two_index -= 1

        for array in new_bi_array:
            index = 0
            while index < N:
                if index == (N - 1):
                    print(array[index])
                    index += 1

                else:
                    print(array[index], end='')
                    index += 1

    except EOFError:
        break