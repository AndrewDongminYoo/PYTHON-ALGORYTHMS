import sys

a, b = map(int, sys.stdin.read().split())
print(a + b, a - b, a * b, a // b, a % b, sep="\n")
