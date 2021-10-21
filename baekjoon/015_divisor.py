# 양수 A가 N의 진짜 약수가 되려면, N이 A의 배수이고, A가 1과 N이 아니어야 한다.
# 어떤 수 N의 진짜 약수가 모두 주어질 때, N을 구하는 프로그램을 작성하시오.

import sys
c = int(sys.stdin.readline())
n = sorted(list(map(int, sys.stdin.readline().split())))
print(min(n)*max(n))