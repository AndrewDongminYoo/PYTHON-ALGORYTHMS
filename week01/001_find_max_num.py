import datetime


def find_max_num(array: list) -> int:
    largest = array[0]
    for num in array:
        if num > largest:
            largest = num
    return largest


if __name__ == '__main__':
    numbers = [3, 5, 6, 1, 2, 4]
    start = datetime.datetime.now()
    print("result:", find_max_num(numbers))
    end = datetime.datetime.now()
    print("time:", (end-start).microseconds, "microseconds")
