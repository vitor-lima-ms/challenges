from collections import Counter

K = int(input())
str_ = input()

str_list = str_.split(' ')
str_list.sort()

main_list = Counter(str_list)

for key, value in main_list.items():
    if value == 1:
        caps_room = key

print(caps_room)