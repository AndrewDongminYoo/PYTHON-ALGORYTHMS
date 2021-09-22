import datetime
value = "hello my name is sparta."*1000


def find_alphabet_occurrence_array(string):
    """
    특정 알파벳의 출현 빈도를 구해주는 메소드입니다. \n
    :param string: 대상 문자열입니다.
    :return: 출현 빈도를 리턴합니다.
    """
    alphabet_occurrence_array = [0] * 26
    a = ord('a')
    for char in string:
        if not char.isalpha():
            continue
        index = ord(char) - a
        alphabet_occurrence_array[index] += 1
    return alphabet_occurrence_array


def find_max_occurred_alphabet(string):
    occurrence_array = find_alphabet_occurrence_array(string)
    max_occurred = max(occurrence_array)
    index = occurrence_array.index(max_occurred)
    return chr(ord('a') + index)


if __name__ == '__main__':
    start = datetime.datetime.now()
    print("result:", find_max_occurred_alphabet(value))
    end = datetime.datetime.now()
    print("time:", (end-start).microseconds, "ms")

    # some_list = [1,8,2,7,3,5]
    # sorted(some_list) => 함수 => 정렬된 배열 리턴
    # some_list.sort() => 리스트의 메소드 => 배열 자체를 리턴하기는 하지만 none 출력
    # print(sorted(some_list)) => 정렬된 리스트가 출력 [1,2,3,5,7,8]
    # print(some_list) [1,8,2,7,3,5]
    # print(some_list.sort()) => None
    # print(some_list) [1,2,3,5,7,8]


