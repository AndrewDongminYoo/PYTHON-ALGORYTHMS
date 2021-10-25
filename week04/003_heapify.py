def swap(tree, index_1, index_2):
    """완전 이진 트리의 노드 index_1과 노드 index_2의 위치를 바꿔준다"""
    temp = tree[index_1]
    tree[index_1] = tree[index_2]
    tree[index_2] = temp


def heapify(tree, index, tree_size):
    """heapify 함수"""

    # 왼쪽 자식 노드의 인덱스와 오른쪽 자식 노드의 인덱스를 계산
    left = 2 * index
    right = 2 * index + 1
    largest = index
    if 0 < left < tree_size and tree[left] > tree[largest]:
        largest = left
    if 0 < right < tree_size and tree[right] > tree[largest]:
        largest = right
    if largest != index:
        swap(tree, largest, index)
        heapify(tree, largest, tree_size)


def heapsort(tree):
    """힙 정렬 함수"""
    tree_size = len(tree)
    for _ in range(tree_size, 0, -1):
        heapify(tree, _, tree_size)
    for i in range(1, tree_size):
        swap(tree, 1, tree_size - i)
        heapify(tree, 1, tree_size - i)

    return tree


def reverse_heapify(tree, index):
    """reverse_heapify 함수"""
    tree_size = len(tree)
    parent_index = index // 2
    smaller = index
    if 0 < parent_index < tree_size and tree[parent_index] > tree[smaller]:
        smaller = parent_index
    if smaller != index:
        swap(tree, smaller, index)
        reverse_heapify(tree, smaller)


class PriorityQueue:
    """힙으로 구현한 우선순위 큐"""
    def __init__(self):
        self.heap = [None]  # 파이썬 리스트로 구현한 힙

    def insert(self, data):
        """삽입 메소드"""
        tree_size = len(self.heap)
        self.heap.append(data)
        reverse_heapify(self.heap, tree_size)

    def extract_max(self):
        """최우선순위 데이터 추출 메소드"""
        swap(self.heap, 1, len(self.heap)-1)
        result = self.heap.pop()
        heapify(self.heap, 1, len(self.heap))
        return result

    def __str__(self):
        return str(self.heap)
