class Node:
    """이진 탐색 트리 노드 클래스"""
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.right_child = None
        self.left_child = None


def print_inorder(node):
    """주어진 노드를 in-order로 출력해주는 함수"""
    if node:
        print_inorder(node.left_child)
        print(node.data)
        print_inorder(node.right_child)


class BinarySearchTree:
    """이진 탐색 트리 클래스"""
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)  # 삽입할 데이터를 갖는 새 노드 생성

        # 트리가 비었으면 새로운 노드를 root 노드로 만든다
        if self.root is None:
            self.root = new_node
            return
        temp = self.root
        while temp is not None:
            if temp.data < data:
                if temp.right_child is None:
                    new_node.parent = temp
                    temp.right_child = new_node
                    return
                else:
                    temp = temp.right_child
            else:
                if temp.left_child is None:
                    new_node.parent = temp
                    temp.left_child = new_node
                    return
                else:
                    temp = temp.left_child

    def print_sorted_tree(self):
        """이진 탐색 트리 내의 데이터를 정렬된 순서로 출력해주는 메소드"""
        print_inorder(self.root)  # root 노드를 in-order로 출력한다

    def search(self, data):
        """이진 탐색 트리 탐색 메소드, 찾는 데이터를 갖는 노드가 없으면 None을 리턴한다"""
        temp = self.root

        while temp is not None:
            if temp.data > data:
                temp = temp.left_child
            elif temp.data < data:
                temp = temp.right_child
            else:
                return temp
        return None

    @staticmethod
    def find_min(node):
        """(부분)이진 탐색 트리의 가장 작은 노드 리턴"""
        temp = node

        while temp.left_child:
            temp = temp.left_child
        return temp

    def delete(self, data):
        """이진 탐색 트리 삭제 메소드"""
        node_to_delete = self.search(data)  # 삭제할 노드를 가지고 온다
        parent_node = node_to_delete.parent  # 삭제할 노드의 부모 노드

        # 경우 1: 지우려는 노드가 leaf 노드일 때
        if node_to_delete.left_child is None and node_to_delete.right_child is None:
            if self.root is node_to_delete:
                self.root = None
            else:  # 일반적인 경우
                if node_to_delete is parent_node.left_child:
                    parent_node.left_child = None
                else:
                    parent_node.right_child = None
        # 경우 2: 지우려는 노드가 왼쪽 자식만 가지고 있을 때
        elif node_to_delete.right_child is None:
            if node_to_delete is self.root:
                self.root = node_to_delete.left_child
                self.root.parent = None
            else:
                if node_to_delete is parent_node.left_child:
                    parent_node.left_child = node_to_delete.left_child
                else:
                    parent_node.right_child = node_to_delete.left_child
                node_to_delete.left_child.parent = parent_node
        # 경우 3: 지우려는 노드가 오른쪽 자식만 가지고 있을 때
        elif node_to_delete.left_child is None:
            if node_to_delete is self.root:
                self.root = node_to_delete.right_child
            else:
                if node_to_delete is parent_node.left_child:
                    parent_node.left_child = node_to_delete.right_child
                else:
                    parent_node.right_child = node_to_delete.right_child
                node_to_delete.right_child.parent = parent_node
        # 경우 4: 지우려는 노드가 양쪽 자식을 모두 가지고 있을 때
        else:
            successor = self.find_min(node_to_delete.right_child)
            node_to_delete.data = successor.data
            if successor is successor.parent.left_child:
                successor.parent.left_child = None
            else:
                successor.parent.right_child = None
            if successor.right_child:
                successor.parent.left_child = successor.right_child


 # 빈 이진 탐색 트리 생성
bst = BinarySearchTree()

# 데이터 삽입
bst.insert(7)
bst.insert(11)
bst.insert(9)
bst.insert(17)
bst.insert(8)
bst.insert(5)
bst.insert(19)
bst.insert(3)
bst.insert(2)
bst.insert(4)
bst.insert(14)

# 이진 탐색 트리 출력
print(bst.search(7).data)
print(bst.search(19).data)
print(bst.search(2).data)
print(bst.search(20))
