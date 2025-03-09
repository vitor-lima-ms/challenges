n = int(input())
arr = map(int, input().split())

my_list = list()
for num in arr:
    my_list.append(num)

final_list =list()
for num_list in my_list:
    if num_list != max(my_list):
        final_list.append(num_list)

print(max(final_list))