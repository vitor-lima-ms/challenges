a = input()
n = int(input())

result_list = list()
for i in range(n):
    b = input()

    set_a = a.split(' ')
    set_b = b.split(' ')

    aux_list_1 = list()
    for element_a in set_a:
        if set_b.count(element_a) > 1:
            aux_list_1.append(True)
        elif set_b.count(element_a) == 0:
            aux_list_1.append(False)
    
    aux_list_2 = list()
    for element_b in set_b:
        if set_a.count(element_b) > 1:
            aux_list_2.append(True)
        elif set_a.count(element_b) == 0:
            aux_list_2.append(False)
    
    if False in aux_list_1 and (aux_list_2.count(True) == len(aux_list_2)):
        result_list.append(True)
    else:
        result_list.append(False)

if False in result_list:
    print(False)
else:
    print(True)