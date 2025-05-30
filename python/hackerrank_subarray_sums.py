def findSum(numbers, queries):
    result_array = list()

    for querie in queries:
        sum_ = 0
        for index in range(querie[0] - 1, querie[1]):
            if numbers[index] == 0:
                sum_ += querie[2]
            sum_ += numbers[index]
        result_array.append(sum_)
        
    return result_array
    
from copy import deepcopy

N = int(input())
numbers = list()
for i in range(N):
    num = int(input())
    numbers.append(num)

n_queries = int(input())
n_num_queries = int(input())

main_queries_list = list()
for i in range(n_queries):
    num_queries = input()
    list_num_queries_str = num_queries.split()
    aux_list = list()
    
    for str in list_num_queries_str:
        aux_list.append(int(str))
    inter_list = deepcopy(aux_list)
    main_queries_list.append(inter_list)
    aux_list.clear()

results = findSum(numbers, main_queries_list)
for result in results:
    print(result)