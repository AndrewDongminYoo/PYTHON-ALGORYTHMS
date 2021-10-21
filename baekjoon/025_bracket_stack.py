import sys
inp = sys.stdin.readline
cnt = int(inp().strip())
for _ in range(cnt):
    sting = inp().strip()
    b = 0
    for l in string:
        if l == "(":
            b += 1
        else:
            b -= 1
    if b == 0:
        print("YES")
    else:
        print("NO")