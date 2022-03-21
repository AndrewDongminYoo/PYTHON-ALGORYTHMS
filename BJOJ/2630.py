import sys

N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
white = 0
blue = 0


def cut_paper(x, y, width):
    check = board[x][y]
    for i in range(x, x + width):
        for j in range(y, y + width):
            if check != board[i][j]:
                cut_paper(x, y, width // 2)  # 1사분면
                cut_paper(x, y + width // 2, width // 2)  # 2사분면
                cut_paper(x + width // 2, y, width // 2)  # 3사분면
                cut_paper(x + width // 2, y + width // 2, width // 2)  # 4사분면
                return
    if check == 0:
        global white
        white += 1
        return
    elif check == 1:
        global blue
        blue += 1
        return


cut_paper(0, 0, N)
print(white)
print(blue)
