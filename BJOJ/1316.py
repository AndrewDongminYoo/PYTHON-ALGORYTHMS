import sys

c = int(sys.stdin.readline())
for i in range(c):
    d = sys.stdin.readline()
    l = list()
    for e in d:
        if e not in l:
            l.append(e)
        elif e == tmp:
            pass
        else:
            c -= 1
            break
        tmp = e
print(c)
