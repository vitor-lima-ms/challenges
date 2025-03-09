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

min_score = 999
for student in main_list:
    if student[1] < min_score:
        min_score = student[1]

while_counter = 0
forif_counter = 1
while while_counter < forif_counter:
    while_counter += 1
    for student in main_list:
        if student[1] == min_score:
            forif_counter += 1
            main_list.remove(student)
    

min_score = 999
for student in main_list:
    if student[1] < min_score:
        min_score = student[1]

students_list = list()
for student in main_list:
    if student[1] == min_score:
        students_list.append(student[0])

students_list.sort()
for student in students_list:
    print(student)