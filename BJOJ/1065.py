# 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다.
# 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때,
# 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.
def arithmetic_sequence(n: int) -> int:
    if n < 100:
        return n
    if n == 1000:
        return 144
    answer = set(c for c in range(1, 100))
    if n >= 100:
        for i in range(101, n + 1):
            a, b, c = map(int, list(str(i)))
            if a - b == b - c:
                answer.add(i)
    return len(answer)


import sys

number = int(sys.stdin.readline())
print(arithmetic_sequence(number))
