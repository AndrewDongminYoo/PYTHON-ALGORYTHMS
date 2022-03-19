word = input()
answer = []
for i in range(ord("a"), ord("z") + 1):
    alpha = chr(i)
    if alpha not in word:
        answer.append(-1)
    else:
        answer.append(word.index(alpha))
print(*answer)
