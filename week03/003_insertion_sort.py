value = [4, 6, 2, 9, 1]


def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        for j in range(i):
            if array[i-j-1] > array[i-j]:
                array[i-j-1], array[i-j] = array[i-j], array[i-j-1]
            else:
                break  # 비교를 더 이상 할 이유가 없다!!


if __name__ == '__main__':
    insertion_sort(value)
    print(value)  # [1, 2, 4, 6, 9] 가 되어야 합니다!

