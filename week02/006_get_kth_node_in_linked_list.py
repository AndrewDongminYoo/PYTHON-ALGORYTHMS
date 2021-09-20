class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        elif self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)
            return

    def get_kth_node_from_last1(self, k: int) -> Node:
        current = self.head
        length = 1
        while current.next:
            length += 1
            current = current.next
        current = self.head
        for i in range(length-k):
            current = current.next
        return current

    def get_kth_node_from_last2(self, k: int) -> Node:
        slow = self.head
        fast = self.head
        for i in range(k):
            fast = fast.next
        while fast is not None:
            slow = slow.next
            fast = fast.next
        return slow


if __name__ == '__main__':
    linked_list = LinkedList(6)
    linked_list.append(7)
    linked_list.append(8)
    # 7이 나와야 합니다!
    print(linked_list.get_kth_node_from_last1(2).data)
