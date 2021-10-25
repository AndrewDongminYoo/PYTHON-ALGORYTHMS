class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        curr = len(self.items)-1
        while curr > 1:
            parent = curr // 2
            if self.items[curr] > self.items[parent]:
                self.items[curr], self.items[parent] = self.items[parent], self.items[curr]
                curr = parent
            else:
                break
        return self

    def delete(self):
        self.items[1], self.items[-1] = self.items[-1], self.items[1]
        result = self.items.pop()
        curr = 1
        while curr < len(self.items):
            left = curr*2
            right = curr*2+1
            max_idx = curr
            if left < len(self.items) and self.items[max_idx] < self.items[left]:
                max_idx = left
            if right < len(self.items) and self.items[max_idx] < self.items[right]:
                max_idx = right
            if max_idx == curr:
                break
            self.items[curr], self.items[max_idx] = self.items[max_idx], self.items[curr]
            curr = max_idx
        return result


max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(6)
max_heap.insert(7)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)  # [None, 8, 6, 7, 2, 5, 4]
print(max_heap.delete())  # 8 을 반환해야 합니다!
print(max_heap.items)  # [None, 7, 6, 4, 2, 5]!
