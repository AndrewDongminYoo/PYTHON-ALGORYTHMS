# 세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.
# 5 5   0 1 2 3 4 5
# 5 7   0 1 2 3 4 5
# 7 5   0 1 2 3 4 5
#       0 1 2 3 4 5
# 7 7 <-출력 2 3 4 5
#       0 1 2 3 4 5
#       0 1 2 3 4 5

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
if x1 == x2:
    if y1 == y3:
        print(x3, y2)
    elif y2 == y3:
        print(x3, y1)
elif x1 == x3:
    if y1 == y2:
        print(x2, y3)
    elif y2 == y3:
        print(x2, y1)
elif x2 == x3:
    if y1 == y2:
        print(x1, y3)
    elif y1 == y3:
        print(x1, y2)

