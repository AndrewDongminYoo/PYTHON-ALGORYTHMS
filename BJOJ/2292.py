def solution(n):
    line = 1
    END_OF_LINE = 1
    ROOMS_IN_LINE = 0
    if n == 1:
        return 1
    while n > END_OF_LINE:
        ROOMS_IN_LINE += 6
        END_OF_LINE += ROOMS_IN_LINE
        line += 1
    return line


N = int(input())
print(solution(N))
