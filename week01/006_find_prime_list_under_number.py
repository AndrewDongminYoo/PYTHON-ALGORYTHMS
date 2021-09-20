import datetime
value = 20


def find_prime_list_under_number(number):
    prime_list = []
    for number in range(2, number+1):
        for prime in prime_list:
            if number % prime == 0 and prime**2 <= number:
                break
        else:
            prime_list.append(number)
    return prime_list


if __name__ == '__main__':
    start = datetime.datetime.now()
    print("result:", find_prime_list_under_number(value))
    end = datetime.datetime.now()
    print("time:", (end - start).microseconds, "microseconds")
