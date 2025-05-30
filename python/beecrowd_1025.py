while True:
    serial_number = 1
    try:
        N, Q = input().split()
        if N == '0' and Q == '0':
            break

        marble_numbers = list()
        for _ in range(int(N)):
            num = int(input())
            marble_numbers.append(num)
        marble_numbers.sort()

        queries = list()
        for _ in range(int(Q)):
            num = int(input())
            queries.append(num)
        
        results = list()
        for querie in queries:
            flag = False
            counter = 0
            for marble_number in marble_numbers:
                counter += 1

                if marble_number == querie:
                    flag == True
                    results.append((marble_number, marble_numbers.index(marble_number)))
                    break
                elif flag == False and counter == len(marble_numbers):
                    results.append((querie, 'not found'))        

        print(f'CASE #{serial_number}')
        for result in results:
            if result[1] == 'not found':
                print(f'{result[0]} {result[1]}')
            else:
                print(f'{result[0]} found at {result[1] + 1}')

    except EOFError:
        break