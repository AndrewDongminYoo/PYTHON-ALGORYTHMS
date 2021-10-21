import sys
inp = sys.stdin.readline
stack = list()

cnt = int(inp().strip())
for _ in range(cnt):
    new = int(inp().strip())
    if new:
        stack.append(new)
    else:
        stack.pop()
print(sum(stack))
