def find_prime_list_under_number(number):
    """
    숫자 X 이하의 모든 Prime Number 구하는 함수
    Returns:
        list: 결과를 담은 리스트.
    """
    prime_list = []
    for number in range(2, number + 1):
        for prime in prime_list:
            if number % prime == 0 and prime ** 2 <= number:
                break
        else:
            prime_list.append(number)
    return prime_list


input_data = input("""문제 5-1: 
  통계계산 중에 소수(Prime number)가 들어오면 계산이 이상한 경우가 있습니다. 
  사용자로부터 어떤 숫자 Χ를 입력 받고, 그 이하의 모든 소수를 출력하는 프로그램이 필요합니다. 
  소수를 구하는 프로그램을 부탁드려요.
  """)
X = int(input_data)
print(find_prime_list_under_number(X))


