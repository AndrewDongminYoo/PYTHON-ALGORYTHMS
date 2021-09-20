def is_palindrome(string):
    n = len(string)
    for i in range(n):
        if string[i] != string[n-1-i]:
            return False
    return True


def is_palindrome_recursive(string):
    if len(string) <= 1:
        return True
    if string[0] == string[-1]:
        return is_palindrome_recursive(string[1:-1])
    return False


if __name__ == '__main__':
    print(is_palindrome_recursive("nolemonsnomelon"))
    print(is_palindrome_recursive("UFOTOFU"))
    print(is_palindrome_recursive("NEVERODDOREVEN"))
    print(is_palindrome_recursive("STEP ON NO PETS"))
    print(is_palindrome_recursive("ASANTAATNASA"))
    print(is_palindrome_recursive("wasitacaroracatisaw"))