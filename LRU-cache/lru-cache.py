"""
Implement an LRU (Least Recently Used) cache.
It should be able to be initialized with a cache size n,
and contain the following methods:

set(key, value): sets key to value.
If there are already n items in the cache and we are adding a new item,
then it should also remove the least recently used item.
get(key): gets the value at key. If no such key exists, return null.

Each operation should run in O(1) time.
"""


from collections import OrderedDict

class LRU(OrderedDict):
    """LRU cache implement in Python 3"""

    def __init__(self, maxsize=128):
        self.maxsize = maxsize
        super().__init__()

    def get(self, key):
        try:
            value = super().__getitem__(key)
            self.move_to_end(key)
            return value
        except KeyError:
            return -1

    def set(self, key, value):
        super().__setitem__(key, value)
        if len(self) > self.maxsize:
            oldest = next(iter(self))
            del self[oldest]


a = LRU(2)

a.set(1, 1)
a.set(2, 1)
a.get(1)
a.set(3, 3)

print(a)
