class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        elif self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def sum_num(self):
        current = self.head
        string = str(current)
        while current.next:
            current = current.next
            string += str(current)
        num = float(string)
        if num % 1 == 0:
            return int(num)
        return num


def get_linked_list_sum(linked_list_1, linked_list_2):
    sum_list1 = linked_list_1.sum_num()
    sum_list2 = linked_list_2.sum_num()
    return sum_list1 + sum_list2


if __name__ == '__main__':
    linked_list_1 = LinkedList(6)
    linked_list_1.append(7)
    linked_list_1.append(0.1)
    linked_list_1.append(8)
    linked_list_2 = LinkedList(3)
    linked_list_2.append(5)
    linked_list_2.append(4)
    print(get_linked_list_sum(linked_list_1, linked_list_2))
