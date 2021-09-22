value = [4, 6, 2, 9, 1]


def bubble_sort_v1(array):
    for i in range(len(array) - 1, 0, -1):
        for j in range(i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


def bubble_sort_v2(array):
    for i in range(len(array) - 1, 0, -1):
        swapped = False
        for j in range(i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if not swapped:
            break


def bubble_sort_v3(array):
    end = len(array) - 1
    while end > 0:
        last_swap = 0
        for i in range(end):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                last_swap = i
        end = last_swap


if __name__ == '__main__':
    bubble_sort_v3(value)
    print(value)  # [1, 2, 4, 6, 9] 가 되어야 합니다!
