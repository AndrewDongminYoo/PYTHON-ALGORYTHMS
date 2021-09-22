class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        if not self.head:
            self.head = Node(value)
            return
        elif self.head:
            temp = self.head
            self.head = Node(value)
            self.head.next = temp
            return

    def pop(self):
        if self.is_empty():
            return "It's Empty Stack"
        else:
            temp = self.head
            self.head = self.head.next
            return temp.data

    def peek(self):
        if self.is_empty():
            return "It's Empty Stack"
        return self.head.data

    # isEmpty 기능 구현
    def is_empty(self):
        return self.head is None


if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print(stack.pop())
    print(stack.peek())
    print(stack.is_empty())
