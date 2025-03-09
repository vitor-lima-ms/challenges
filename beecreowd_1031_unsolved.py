"""beecrowd 1031"""

def remove_last_occurence(list_, num):
    last_index = -1
    
    for index, value in enumerate(list_):
        if value == num:
            last_index = index
    
    if last_index != -1:
        list_.pop(last_index)
    
    return list_

N = int(input())

regions = [num for num in range(1, N + 1)]
turn_off_order = [-1 for i in range(N)]

counter = 0
while True:
    if turn_off_order[-1] == 13 and len(turn_off_order) == N:
        break
    
    counter += 1
    new_regions = regions * counter

    for num in new_regions[::counter]:
        other_counter = 1
        while other_counter < counter:
            new_regions = remove_last_occurence(new_regions, num)
            other_counter += 1
        if counter == 1:
            turn_off_order.append(num)
            turn_off_order.remove(-1)
        else:
            if (num + counter) >= (N + (counter - 1)) and counter >= 2:
                turn_off_order.append(new_regions[(new_regions.index(num) + 1)])
                turn_off_order.remove(-1)
            else:
                turn_off_order.append(num)
                turn_off_order.remove(-1)

    turn_off_order = [-1 for i in range(N + 1)]
    regions = [num for num in range(1, N + 1)]
