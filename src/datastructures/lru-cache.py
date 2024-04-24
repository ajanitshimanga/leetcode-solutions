from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._dict = OrderedDict()

    def get(self, key: int) -> int:
        if key in self._dict:
            val = self._dict.get(key)
            self._dict.move_to_end(key, True)
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if len(self._dict) <= self._capacity:
            self._dict[key] = value
            self._dict.move_to_end(key, True)
            if len(self._dict) == self._capacity + 1:
                self._dict.popitem(last=False)
