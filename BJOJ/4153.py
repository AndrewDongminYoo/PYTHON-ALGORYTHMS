# 문제
# 과거 이집트인들은 각 변들의 길이가 3, 4, 5인 삼각형이 직각 삼각형인 것을 알아냈다.
# 주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분하시오.
#
# 입력
# 입력은 여러 개의 테스트 케이스로 주어지며 마지막 줄에는 0 0 0이 입력된다.
# 각 테스트 케이스는 모두 30,000보다 작은 양의 정수로 주어지며,
# 각 입력은 변의 길이를 의미한다.

while True:
    a, b, c = map(int, input().split())
    if a == 0 or b == 0 or c == 0:
        break
    elif a ** 2 + b ** 2 == c ** 2:
        print('right')
    elif a ** 2 + c ** 2 == b ** 2:
        print('right')
    elif b ** 2 + c ** 2 == a ** 2:
        print('right')
    else:
        print('wrong')
