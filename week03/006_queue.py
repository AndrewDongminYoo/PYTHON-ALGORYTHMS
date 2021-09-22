from queue import Queue as Q


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue(Q):
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
            return self.tail
        else:
            self.head = new_node
            self.tail = new_node

    def dequeue(self):
        if self.head:
            delete_head = self.head
            self.head = self.head.next
            return delete_head.data
        return "It's empty"

    def peek(self):
        if self.head:
            return self.head
        return "It's empty"

    def is_empty(self):
        return self.head == self.tail
