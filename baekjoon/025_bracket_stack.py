import sys
inp = sys.stdin.readline
cnt = int(inp().strip())
for _ in range(cnt):
    string = inp().strip()
    while "()" in string:
        string = string.replace("()","")
    if not string:
        print("YES")
    else:
        print("NO")