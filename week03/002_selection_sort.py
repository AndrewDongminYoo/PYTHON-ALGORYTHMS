value = [4, 6, 2, 9, 1]


def selection_sort_v1(array):
    n = len(array)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array


def selection_sort_v2(array):
    n = len(array)
    for i in range(n-1):
        min_index = i
        for j in range(n-i):
            if array[i + j] < array[min_index]:
                min_index = i + j

        array[i], array[min_index] = array[min_index], array[i]
    return array


if __name__ == '__main__':
    selection_sort_v1(value)
    print(value)  # [1, 2, 4, 6, 9] 가 되어야 합니다!
