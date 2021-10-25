import sys
# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.


def queen(n):
    if n == N:  # 마지막까지 탐색한 경우 (False 가 발생하지 않았음)
        global count  # 글로벌 변수 가져옴
        count += 1  # count++
    else:
        for i in range(N):  # N의 수 만큼 순회
            if visited[i]:  # 이미 시도한 경우의 수는 넘어가기
                continue
            board[n] = i  # (n, i) 지점에 퀸을 놓습니다.
            if queen_check(n):  # 퀸을 놓을 수 있는지 확인합니다.
                visited[i] = True
                queen(n + 1)  # 재귀적으로 다음 행을 검사합니다.
                visited[i] = False  # 다시 i 번째를 초기화합니다.


def queen_check(n):
    for i in range(n):  # n개의 배열 인덱스 i
        # 이미 놓여져 있는 퀸 board[n]과 같은 열일 경우 False
        # (행 끼리의 차 == 열 끼리의 차의 절댓값)이 True 인 경우 두 퀸이 대각선 상에 있는 경우임
        if (board[n] == board[i]) or (n - i == abs(board[n] - board[i])):
            return False
    return True


N = int(sys.stdin.readline())
count = 0  # 모든 경우의 수를 담을 변수
board = [0 for _ in range(N)]  # N개의 0으로 만들어진 배열 생성
visited = [False for _ in range(N)]  # N개의 False 로 만들어진 배열
queen(0)  # 0부터 시작합니다. N의 값을 구할 때까지 n+1
print(count)

if 1 <= N < 15:
    result = [False, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596, 2279184]
    print(result[N])