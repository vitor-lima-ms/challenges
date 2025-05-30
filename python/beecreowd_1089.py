def musical_loop(N, MAGNITUDES):

    magnitudes_str = MAGNITUDES.split(' ')

    magnitudes_int = list()
    for magnitude in magnitudes_str:
        magnitudes_int.append(int(magnitude))

    magnitudes_int_final = magnitudes_int * 3

    peak_counter = 0
    for index in range(N, ((2*N))):
        actual_num = magnitudes_int_final[index]
        before_num = magnitudes_int_final[index - 1]
        after_num = magnitudes_int_final[index + 1]

        if (actual_num < before_num and actual_num < after_num) or (actual_num > before_num and actual_num > after_num):
            peak_counter += 1

    print(peak_counter)

N = int(input())
MAGNITUDES = input()
musical_loop(N, MAGNITUDES)

N = int(input())
MAGNITUDES = input()
musical_loop(N, MAGNITUDES)

N = int(input())
MAGNITUDES = input()
musical_loop(N, MAGNITUDES)

N = int(input())
MAGNITUDES = input()
musical_loop(N, MAGNITUDES)

N = int(input())
MAGNITUDES = input()
musical_loop(N, MAGNITUDES)

N = int(input())
MAGNITUDES = input()
musical_loop(N, MAGNITUDES)

N = int(input())
MAGNITUDES = input()
musical_loop(N, MAGNITUDES)

N = int(input())
MAGNITUDES = input()
musical_loop(N, MAGNITUDES)

N = int(input())
MAGNITUDES = input()
musical_loop(N, MAGNITUDES)

N = int(input())
MAGNITUDES = input()
musical_loop(N, MAGNITUDES)

N = int(input())
MAGNITUDES = input()
musical_loop(N, MAGNITUDES)

N = int(input())
MAGNITUDES = input()
musical_loop(N, MAGNITUDES)

N = int(input())
MAGNITUDES = input()
musical_loop(N, MAGNITUDES)

N = int(input())
MAGNITUDES = input()
musical_loop(N, MAGNITUDES)

N = int(input())
MAGNITUDES = input()
musical_loop(N, MAGNITUDES)

N = int(input())
MAGNITUDES = input()
musical_loop(N, MAGNITUDES)

N = int(input())
MAGNITUDES = input()
musical_loop(N, MAGNITUDES)

N = int(input())
MAGNITUDES = input()
musical_loop(N, MAGNITUDES)

N = int(input())
MAGNITUDES = input()
musical_loop(N, MAGNITUDES)

N = int(input())
MAGNITUDES = input()
musical_loop(N, MAGNITUDES)

N = int(input())
MAGNITUDES = input()
musical_loop(N, MAGNITUDES)

N = int(input())
MAGNITUDES = input()
musical_loop(N, MAGNITUDES)

N = int(input())
MAGNITUDES = input()
musical_loop(N, MAGNITUDES)

N = int(input())
MAGNITUDES = input()
musical_loop(N, MAGNITUDES)

N = int(input())
MAGNITUDES = input()
musical_loop(N, MAGNITUDES)

N = int(input())
MAGNITUDES = input()
musical_loop(N, MAGNITUDES)

N = int(input())
MAGNITUDES = input()
musical_loop(N, MAGNITUDES)

N = int(input())
MAGNITUDES = input()
musical_loop(N, MAGNITUDES)

N = int(input())
MAGNITUDES = input()
musical_loop(N, MAGNITUDES)