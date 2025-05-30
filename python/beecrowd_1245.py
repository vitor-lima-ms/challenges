while True:
    try:
        N = input()

        if not N:
            break

        N = int(N)

        boots = list()

        count = int()
        for i in range(N):
            boot = input().split(' ')
            boots.append(boot)

            if i == 0:
                continue

            if boot[1] == 'D':
                other_pair = boots.count([boot[0], 'E'])

                if other_pair > 0:
                    count += 1
                    boots.remove(boot)
                    boots.remove([boot[0], 'E'])
            
            elif boot[1] == 'E':
                other_pair = boots.count([boot[0], 'D'])

                if other_pair > 0:
                    count += 1
                    boots.remove(boot)
                    boots.remove([boot[0], 'D'])
    except EOFError:
        break

    print(count)