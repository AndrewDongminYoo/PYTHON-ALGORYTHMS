import sys

word = sys.stdin.readline().strip()
t = word.replace("c=", "a").replace("c-", "b").replace("dz=", "y")\
    .replace("d-", "d").replace("lj", "k").replace("nj", "o").\
    replace("s=", "t").replace("z=", "z")
print(len(t))
