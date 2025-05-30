C = int(input())
T = input().upper()

array = [[] for _ in range(0, 12)]

for i in range(0, 12):
    for j in range(0, 12):
        num = float(input())
        array[i].append(num)

if T == 'S':
    result = sum(sum(array[C]))
    print(f'{result:.1f}')
elif T == 'M' or T == 'A':
    result = sum(array[C]) / len(array[C])
    print(f'{result:.1f}')