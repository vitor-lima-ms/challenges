from copy import deepcopy

x = int(input())
y = int(input())
z = int(input())
n = int(input())

x_list = [x for x in range (0, x + 1)]
y_list = [y for y in range (0, y + 1)]
z_list = [z for z in range (0, z + 1)]

main_list = list()
for num_x in x_list:
    for num_y in y_list:
        for num_z in z_list:
            aux_list = list()
            aux_list.append(num_x)
            aux_list.append(num_y)
            aux_list.append(num_z)
            main_list.append(deepcopy(aux_list))

while_counter = 0
for_counter = 1
while True:
    if while_counter == for_counter:
        break

    for sub_list in main_list:
        if sum(sub_list) == n:
            main_list.remove(sub_list)
            for_counter +=1
    
    while_counter += 1

print(main_list)