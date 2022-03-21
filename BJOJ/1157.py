import sys

word = sys.stdin.readline().lower().strip()
d = dict()
for w in word:
    if w not in d.keys():
        d[w] = 1
    else:
        d[w] += 1
wordlist = sorted(d.items(), key=lambda x: x[1], reverse=True)
a = wordlist.pop(0)
if not wordlist:
    print(a[0].upper())
elif a[1] == wordlist.pop(0)[1]:
    print("?")
else:
    print(a[0].upper())
