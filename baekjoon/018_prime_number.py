# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
import sys
M, N = map(int, sys.stdin.readline().split())
div = [False]*2 + [True]*(N - 1)
primes = []
for i in range(2, N + 1):
    if div[i]:
        primes.append(i)
        for j in range(2 * i, N + 1, i):
            div[j] = False
for x in primes:
    if M <= x <= N:
        print(x)