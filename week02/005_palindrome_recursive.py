def is_palindrome(string):
    if len(string) <= 1:
        return True
    if string[0] == string[-1]:
        return is_palindrome(string[1:-1])
    return False


if __name__ == '__main__':
    print(is_palindrome("nolemonsnomelon"))
    print(is_palindrome("UFOTOFU"))
    print(is_palindrome("NEVERODDOREVEN"))
    print(is_palindrome("STEP ON NO PETS"))
    print(is_palindrome("ASANTAATNASA"))
    print(is_palindrome("wasitacaroracatisaw"))