def is_existing(target, array):
    """
    대상 리스트에 타겟 값이 존재하는지 여부를 나타냅니다.

    :param target: 찾고자 하는 값입니다.
    :type target: Any
    :param array: 찾고자 하는 대상이 되는 배열(리스트)입니다.
    :type array: list
    :return: bool
    """
    if len(array) == 0:
        return False
    curr = (len(array)) // 2
    if array[curr] == target:
        return True
    elif array[curr] < target:
        return is_existing(target, array[curr + 1:])
    else:
        return is_existing(target, array[:curr])


def is_available_to_order(menus, orders):
    menus.sort()  # menus 정렬!
    for order in orders:
        if not is_existing(order, menus):
            return False
    return True


if __name__ == '__main__':
    shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
    shop_orders = ["오뎅", "콜라", "만두"]
    result = is_available_to_order(shop_menus, shop_orders)
    print(result)
