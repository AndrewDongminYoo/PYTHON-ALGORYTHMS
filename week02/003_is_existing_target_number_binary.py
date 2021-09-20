def is_existing_target_number_binary(target, array):
    min_id = 0
    max_id = len(array)-1
    curr = (min_id+max_id)//2
    while min_id <= max_id:
        if array[curr] == target:
            return True
        elif array[curr] < target:
            min_id = curr+1
        else:
            max_id = curr-1
        curr = (min_id+max_id)//2
    return False


def is_existing_target_number_recursive(target, array):
    if len(array) == 0:
        return False
    curr = (len(array)) // 2
    if array[curr] == target:
        return True
    elif array[curr] < target:
        return is_existing_target_number_recursive(target, array[curr + 1:])
    else:
        return is_existing_target_number_recursive(target, array[:curr])


if __name__ == '__main__':
    finding_target = 11
    finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    print(is_existing_target_number_recursive(finding_target, finding_numbers))
