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
            return
        elif self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)
            return

    def print_all(self):
        current = self.head
        result = f"[{current}]"
        while current.next:
            current = current.next
            result += f"->[{current}]"
        print(result)

    def get_node(self, index):
        current = self.head
        for i in range(index):
            if current.next is not None:
                current = current.next
            else:
                return None
        return current

    def add_node(self, index, data):
        node = Node(data)
        if index > 0:
            _prev = self.get_node(index-1)
            _next = self.get_node(index)
            _prev.next = node
            node.next = _next
        elif index == 0:
            _prev = self.head
            node.next = _prev
            self.head = node
        else:
            print("cannot add node!")

    def delete_node(self, index):
        if index == 0:
            self.head = self.head.next
        else:
            _prev = self.get_node(index-1)
            _next = self.get_node(index)
            _prev.next = _next.next


if __name__ == '__main__':
    one = Node(1)
    two = Node(2)
    three = Node(3)
    ll = LinkedList(0)
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(0)
    ll.add_node(3, 120)
    ll.add_node(0, 55)
    ll.delete_node(1)
    ll.delete_node(6)
    ll.print_all()
    print(ll.get_node(4))
    print(ll.get_node(0))
