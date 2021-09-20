import datetime


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    if string[0] == "1":
        zero, one = 0, 1
    else:
        zero, one = 1, 0
    for i in range(len(string)-1):
        if string[i] != string[i+1] and string[i+1] == "0":
            zero += 1
        elif string[i] != string[i+1] and string[i+1] == "1":
            one += 1
    return min(zero, one)


if __name__ == '__main__':
    value = "10001111110001"
    start = datetime.datetime.now()
    print("result:", find_count_to_turn_out_to_all_zero_or_all_one(value))
    end = datetime.datetime.now()
    print("time:", (end - start).microseconds, "microseconds")