class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedTuple:
    def __init__(self):
        self._items = list()

    def add(self, key, value):
        self._items.append((key, value))
        return

    def get(self, key):
        for k, value in self._items:
            if k == key:
                return value
        return "cannot get key-value"

    @property
    def items(self):
        return self._items


class LinkedDict:
    def __init__(self):
        self._items = list()
        for i in range(12):
            self._items.append(LinkedTuple())

    @property
    def items(self):
        return self._items

    def put(self, key, value):
        i = hash(key) % len(self._items)
        self._items[i].add(key, value)

    def get(self, key):
        i = hash(key) % len(self._items)
        return self._items[i].get(key)


if __name__ == '__main__':
    my_dict = LinkedDict()
    my_dict.put("hi", "hello")
    print(my_dict.get("hi"))
