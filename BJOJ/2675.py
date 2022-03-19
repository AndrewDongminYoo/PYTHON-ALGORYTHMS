T = int(input())
for _ in range(T):
    words = []
    R, S = input().split()
    words += [S[_] * int(R) for _ in range(len(S))]
    print(''.join(words))


