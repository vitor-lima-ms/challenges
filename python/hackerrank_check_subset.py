T = int(input())

for i in range(T):
    n_a = int(input())
    a = input()
    n_b = int(input())
    b = input()

    a_list_str = a.split(' ')
    b_list_str = b.split(' ')

    counter = 0
    for element in a_list_str:
        if b_list_str.count(element) > 0:
            counter += 1
    
    if counter == n_a:
        print(True)
    else:
        print(False)