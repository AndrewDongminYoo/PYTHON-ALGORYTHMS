class Node:
    """이진 트리 노드 클래스"""
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def get_parent_index(complete_binary_tree, index):
    """배열로 구현한 완전 이진 트리에서 index번째 노드의 부모 노드의 인덱스를 리턴하는 함수"""
    _parent_index = index // 2
    if len(complete_binary_tree) > _parent_index > 0:
        return _parent_index


def get_left_child_index(complete_binary_tree, index):
    """배열로 구현한 완전 이진 트리에서 index번째 노드의 왼쪽 자식 노드의 인덱스를 리턴하는 함수"""
    _left_child_index = index * 2
    if 0 < _left_child_index < len(complete_binary_tree):
        return _left_child_index


def get_right_child_index(complete_binary_tree, index):
    """배열로 구현한 완전 이진 트리에서 index번째 노드의 오른쪽 자식 노드의 인덱스를 리턴하는 함수"""
    _right_child_index = index * 2 + 1
    if 0 < _right_child_index < len(complete_binary_tree):
        return _right_child_index


def traverse_inorder(node):
    """in-order 순회 함수"""
    if node:
        traverse_inorder(node.left_child)
        print(node.data)
        traverse_inorder(node.right_child)


# 실행 코드
root_node_index = 1  # root 노드

tree = [None, 1, 5, 12, 11, 9, 10, 14, 2, 10]  # 과제 이미지에 있는 완전 이진 트리

# root 노드의 왼쪽과 오른쪽 자식 노드의 인덱스를 받아온다
left_child_index = get_left_child_index(tree, root_node_index)
right_child_index = get_right_child_index(tree, root_node_index)

print(tree[left_child_index])
print(tree[right_child_index])

# 9번째 노드의 부모 노드의 인덱스를 받아온다
parent_index = get_parent_index(tree, 9)

print(tree[parent_index])

# 부모나 자식 노드들이 없는 경우들
parent_index = get_parent_index(tree, 1)  # root 노드의 부모 노드의 인덱스를 받아온다
print(parent_index)

left_child_index = get_left_child_index(tree, 6)  # 6번째 노드의 왼쪽 자식 노드의 인덱스를 받아온다
print(left_child_index)

right_child_index = get_right_child_index(tree, 8)  # 8번째 노드의 오른쪽 자식 노드의 인덱스를 받아온다
print(right_child_index)

print(max(tree[1:]))
