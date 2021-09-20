value = "hellomydarlinghowareyouiamfine"


def find_not_repeating_character(string):
    no_repeat = "_"
    no_repeat_list = []
    alphabet_array = [0]*26
    for char in string:
        if char.isalpha():
            index = ord(char)-ord('a')
            alphabet_array[index] += 1
    for char in string:
        if alphabet_array[ord(char)-ord('a')] == 1:
            if no_repeat == "_":
                no_repeat = char
    return no_repeat


if __name__ == '__main__':
    result = find_not_repeating_character(value)
    print(result)

