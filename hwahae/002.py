def solution1(waiting):
    answer = []

    for i in range(len(waiting)):
        if waiting[i] not in answer:
            answer.append(waiting[i])
            waiting[waiting.index(waiting[i])] = None

    return answer


def solution(waiting):
    answer = []

    dic = {}

    for wait in waiting:
        if wait in dic:
            continue
        else:
            dic[wait] = 1
            answer.append(wait)

    return answer


if __name__ == "__main__":
    print(solution([1, 5, 8, 2, 10, 5, 4, 6, 4, 8]), "[1, 5, 8, 2, 10, 4, 6]")
    print(solution([5, 4, 4, 3, 5]), "[5, 4, 3]")
