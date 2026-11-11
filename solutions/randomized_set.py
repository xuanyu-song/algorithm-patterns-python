"""Randomized Set (LeetCode 380). Swap the removed item with the final item and repair its index."""

import random

class RandomizedSet:

    def __init__(self):
        self.dict = dict()
        self.list = list()

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.dict:
            idx = self.dict[val]
            last = self.list[-1]
            self.list[idx] = last
            self.dict[last] = idx
            self.list.pop()
            self.dict.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.list)
