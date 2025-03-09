from copy import deepcopy

N = int(input())

aux_list = list()
main_list = list()
for i in range(N):
    name = input()
    aux_list.append(name)
    score = float(input())
    aux_list.append(score)
    main_list.append(deepcopy(aux_list))
    aux_list.clear()

print(main_list)