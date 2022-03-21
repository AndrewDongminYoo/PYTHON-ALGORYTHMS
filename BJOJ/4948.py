# 베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다.
# 이 명제는 조제프 베르트랑이 1845년에 추측했고, 파프누티 체비쇼프가 1850년에 증명했다.
# 예를 들어, 10보다 크고, 20보다 작거나 같은 소수는 4개가 있다. (11, 13, 17, 19)
# 또, 14보다 크고, 28보다 작거나 같은 소수는 3개가 있다. (17,19, 23)
# 자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오.
import sys

while True:
    num = int(sys.stdin.readline())
    if not num:
        break
    limit = num * 2
    alpha = [False, False] + [True] * (limit - 1)
    prime_number = []

    for i in range(2, limit + 1):
        if alpha[i]:
            prime_number.append(i)
            for j in range(2 * i, limit + 1, i):
                alpha[j] = False
    print(len([x for x in prime_number if num < x <= limit]))
