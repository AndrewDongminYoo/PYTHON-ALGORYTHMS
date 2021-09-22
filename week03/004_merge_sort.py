def merge_sort_v1(array: list) -> list:
    """
    조금 더 readable 한 버전의 병합정렬, 정렬된 리스트를 반환한다.\n
    :param array: list
    :return: list
    """
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    array1 = merge_sort_v1(array[:mid])
    array2 = merge_sort_v1(array[mid:])
    return merge(array1, array2)


def merge(array1: list, array2: list) -> list:
    array3 = []
    i = j = 0
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            array3.append(array1[i])
            i += 1
        else:
            array3.append(array2[j])
            j += 1
    array3 += array1[i:]
    array3 += array2[j:]
    return array3


def merge_sort_v2(array: list) -> None:
    """
    효율성이 조금 더 나은 버전의 병합정렬, 원본 리스트를 정렬한다.\n
    :param array: list
    :return: None (changes origin list)
    """
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge1(low, mid, high)

    def merge1(low, mid, high):
        temp = []
        j, h = low, mid

        while j < mid and h < high:
            if array[j] < array[h]:
                temp.append(array[j])
                j += 1
            else:
                temp.append(array[h])
                h += 1

        while j < mid:
            temp.append(array[j])
            j += 1
        while h < high:
            temp.append(array[h])
            h += 1

        for i in range(low, high):
            array[i] = temp[i - low]

    return sort(0, len(array))


if __name__ == '__main__':
    array_a = [9, 6, 3, 5, 1, 4, 2, 8, 7]
    print(merge_sort_v1(array_a))  # [1, 2, 3, 4, 5, 6, 7, 8, 9] sorted() 처럼
    print(array_a)  # [9, 6, 3, 5, 1, 4, 2, 8, 7] 가 됩니다!
    merge_sort_v2(array_a)  # 원본 리스트를 정렬합니다. .sort() 메소드처럼
    print(array_a)  # [1, 2, 3, 4, 5, 6, 7, 8, 9] 가 됩니다!
