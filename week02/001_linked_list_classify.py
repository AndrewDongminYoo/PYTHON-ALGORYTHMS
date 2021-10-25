class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        """링크드 리스트를 문자열로 표현해서 리턴하는 메소드"""
        res_str = "|"

        # 링크드  리스트 안에 모든 노드를 돌기 위한 변수. 일단 가장 앞 노드로 정의한다.
        iterator = self.head

        # 링크드  리스트 끝까지 돈다
        while iterator:
            # 각 노드의 데이터를 리턴하는 문자열에 더해준다
            res_str += f" {iterator.data} |"
            iterator = iterator.next  # 다음 노드로 넘어간다

        return res_str

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_after(self, pre_node, data):
        new_node = Node(data)

        if pre_node is self.tail:
            self.append(data)
        else:
            new_node.next = pre_node.next
            new_node.prev = pre_node
            pre_node.next.prev = new_node
            pre_node.next = new_node

    def delete(self, node_to_delete):
        d_data = node_to_delete.data

        if node_to_delete is self.tail:  # 가장 뒤의 노드를 지우려 할 때
            if node_to_delete is self.head:
                self.head = None
                self.tail = None
            else:
                node_to_delete.prev.next = None
                self.tail = node_to_delete.prev
        elif node_to_delete is self.head:
            self.head = node_to_delete.next
            self.head.prev = None
        else:  # 두 노드 사이의 노드를 지우려 할 때
            node_to_delete.next.prev = node_to_delete.prev
            node_to_delete.prev.next = node_to_delete.next
        return d_data

    def find_node_at(self, index):
        iterator = self.head

        for _ in range(index):
            iterator = iterator.next

        return iterator

    def find_node_with_data(self, data):
        iterator = self.head

        while iterator:
            # 코드를 쓰세요
            if iterator.data is data:
                return iterator
            iterator = iterator.next  # 다음 노드로 넘어간다
