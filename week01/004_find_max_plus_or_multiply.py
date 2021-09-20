value = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    number_sum = 0
    for number in array:
        if number_sum <= 1 or number <= 1:
            number_sum += number
        else:
            number_sum *= number
    return number_sum


if __name__ == '__main__':
    result = find_max_plus_or_multiply(value)
    print(result)
