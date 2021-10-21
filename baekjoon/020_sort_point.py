# 2차원 평면 위의 점 N개가 주어진다. 좌표를 y 좌표가 증가하는 순으로, y 좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.
import sys
c = int(sys.stdin.readline().strip())
d = []
for _ in range(c):
    x, y = map(int, sys.stdin.readline().split())
    d.append((x, y))
points = sorted(d)
for k, v in sorted(points, key=lambda a: a[1]):
    print(k, v)
