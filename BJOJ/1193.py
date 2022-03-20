# 무한히 큰 배열에 다음과 같이 분수들이 적혀있다.
#
# 1/1	1/2	1/3	1/4	1/5	…
# 2/1	2/2	2/3	2/4	…	…
# 3/1	3/2	3/3	…	…	…
# 4/1	4/2	…	…	…	…
# 5/1	…	…	…	…	…
# …	…	…	…	…	…
# 이와 같이 나열된 분수들을 1/1 → 1/2 → 2/1 → 3/1 → 2/2 → …
# 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, …
# 분수라고 하자.

# 1/1 → 1/2 → 2/1 → 3/1 → 2/2 → 3/1 → 1/4 → 2/3 → 3/2 → 4/1 → 1/5 → 2/4 → 3/3 → 4/2 → …
# X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.

# dicto = [{} for _ in range(1000)]
# array = []
#
# for k in range(1000):
#     for j in range(1000):
#         dicto[k][j] = f"{k + 1}/{j + 1}"
#
#     for l in range(k + 1):
#         if k % 2 == 1:
#             array.append(dicto[l][k-l])
#         else:
#             array.append(dicto[k-l][l])
#
# print(array[int(input()) - 1])


X = int(input())

line = 0
END_OF_LINE = 0
while X > END_OF_LINE:
    line += 1
    END_OF_LINE += line

gap = END_OF_LINE - X
if line % 2 == 0:
    child = line - gap
    parent = gap + 1
else:
    child = gap + 1
    parent = line - gap
print(f'{child}/{parent}')
