import sys
def bino_coef(N, K):
    if K>N:
        return 0
    if K==0 or N==0:
        return 1
    return bino_coef(N-1, K-1) + bino_coef(N-1, K)


# N, K = map(int, sys.stdin.readline().split())
print(bino_coef(29, 13))