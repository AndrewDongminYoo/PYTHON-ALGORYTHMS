# 한수는 지금 (x, y)에 있다.
# 직사각형은 각 변이 좌표축에 평행하고,
# 왼쪽 아래 꼭짓점은 (0, 0), 오른쪽 위 꼭짓점은 (w, h)에 있다.
# 직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램을 작성하시오.

# 0,H       W,H
#
#     X,Y
# 0,0       W,0


X, Y, W, H = map(int, input().split())

case1 = min(abs(W-X), abs(X))  # 가로 최단 거리
case2 = min(abs(H-Y), abs(Y))  # 세로 최단 거리
print(min(case1, case2))  # 총 최단 거리
