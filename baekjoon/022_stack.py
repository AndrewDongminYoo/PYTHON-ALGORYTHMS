import sys
inp = sys.stdin.readline
stack = list()

cnt = int(inp().strip())
for _ in range(cnt):
    order = inp().strip()
    o = order[:3]
    if o == 'pus':
        method, num = order.split()
        n = int(num)
        stack.append(n)
    elif o == 'pop':
        if len(stack):
            print(stack.pop())
        else:
            print(-1)
    elif o == 'top':
        if len(stack):
            print(stack[-1])
        else:
            print(-1)
    elif o == 'siz':
        print(len(stack))
    elif o == 'emp':
        print(int(len(stack) == 0))
