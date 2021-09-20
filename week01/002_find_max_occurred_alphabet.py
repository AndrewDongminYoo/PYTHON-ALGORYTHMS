import datetime
value = "hello my name is sparta."*1000


def find_alphabet_occurrence_array(string):
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
