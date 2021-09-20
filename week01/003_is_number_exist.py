import datetime

value = [3, 5, 6, 1, 2, 4]*1000


def is_number_exist(number, array):
    for num in array:
        if number == num:
            return True
    return False


def is_exist(number, array):
    return number in array


if __name__ == '__main__':
    start = datetime.datetime.now()
    print("result:", is_number_exist(9, value))
    end = datetime.datetime.now()
    print("time:", (end - start).microseconds, "ms")
    start = datetime.datetime.now()
    print("result:", is_exist(9, value))
    end = datetime.datetime.now()
    print("time:", (end - start).microseconds, "ms")
