def is_prime_number(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


cases = int(input())
numbers = map(int, input().split())
primes = 0

for _ in range(cases):
    n = next(numbers)
    if is_prime_number(n):
        primes += 1

print(primes)
