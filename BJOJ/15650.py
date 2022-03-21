# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
#
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 고른 수열은 오름차순이어야 한다.
# 첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)
import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
discovered = [False] * N
result = list()


def solution1(depth, index, n, m):
    if depth == m:
        print(' '.join(map(str, result)))
        return
    for i in range(index, n):
        if not discovered[i]:
            discovered[i] = True
            result.append(i + 1)
            solution1(depth + 1, i + 1, n, m)
            discovered[i] = False
            result.pop()


solution1(0, 0, N, M)
N, M = map(int, input().split())


def solution2(n, m):
    comb = combinations(range(1, n + 1), m)  # iter(tuple)
    for i in comb:
        print(' '.join(map(str, i)))  # tuple -> str


solution2(N, M)
