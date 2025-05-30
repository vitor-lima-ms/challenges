while True:
    from collections import deque

    inp = input()

    N = int(inp.split()[0])
    D = int(inp.split()[1])

    prize = input()

    fila = deque(prize)

    while len(fila) > (N - D):
        fila.remove(min(fila))