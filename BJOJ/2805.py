import sys

input = sys.stdin.readline


def mine():
    cnt, need = map(int, input().split())
    trees = list(map(int, input().split()))
    d = dict()
    for h in range(max(trees), 0, -1):
        for t in trees:
            d[h] = sum(list(map(lambda x: x - h if x - h > 0 else 0, trees)))
        if d[h] >= need:
            print(h)
            break


def theirs():
    cnt, need = map(int, input().split())
    trees = list(map(int, input().split()))

    left = 0
    highest = max(trees)
    answer = 0
    while left <= highest:
        mid = (left + highest) // 2
        _sum = 0
        for i in trees:
            if mid < i:
                _sum += i - mid
                if _sum > need:
                    break
        if _sum < need:
            highest = mid - 1
        else:
            answer = mid
            left = mid + 1

    print(answer)
