count = int(input())
numbers = list(map(int, list(input())))
answer = 0
for i in range(count):
    answer += numbers[i]
print(answer)
