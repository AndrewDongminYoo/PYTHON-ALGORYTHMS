def is_correct_parenthesis(string):
    count = 0
    for i in range(len(string)):
        if string[i] == "(":
            count += 1
        elif string[i] == ")":
            count -= 1
    return count == 0


if __name__ == '__main__':
    s = "(())()"
    # True 를 반환해야 합니다!
    print(is_correct_parenthesis(s))
