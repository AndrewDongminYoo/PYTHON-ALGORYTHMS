solution = 1


def bridge(n, m):
    global solution
    if n == 0:
        print(round(solution))
        solution = 1
    else:
        solution = solution * (m / n)
        bridge(n - 1, m - 1)


T = []
N = int(input().strip())
for _ in range(N):
    T.append(list(map(int, input().split())))
for west, east in T:
    bridge(west, east)
