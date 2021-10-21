# 두 자연수 A와 B에 대해서, A의 배수이면서 B의 배수인 자연수를 A와 B의 공배수라고 한다.
# 이런 공배수 중에서 가장 작은 수를 최소공배수라고 한다. 예를 들어, 6과 15의 공배수는 30, 60, 90등이 있으며, 최소 공배수는 30이다.
# 두 자연수 A와 B가 주어졌을 때, A와 B의 최소공배수를 구하는 프로그램을 작성하시오.
import sys
cnt = int(sys.stdin.readline().strip())

def get_divisor(num, arr):
    result = set()
    for i in arr:
        if num % i == 0:
            result.add(i)
    return result
def get_common(num1, num2):
    divisor = get_divisor(num1, range(1,num1+1))
    return max(divisor.intersection(get_divisor(num2, divisor)))
def common_multiple(num1, num2):
    div = get_common(num1, num2)
    return int((num1/div) * num2)
for _ in range(cnt):
    A, B = map(int, sys.stdin.readline().split())
    print(common_multiple(A, B))