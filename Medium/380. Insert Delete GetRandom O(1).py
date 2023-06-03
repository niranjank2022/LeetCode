import random


class RandomizedSet:

    def __init__(self):
        self.hashmap = {}
        self.data = []
        self.length = 0

    def insert(self, val: int) -> bool:
        if val in self.hashmap:
            return False
        self.data.append(val)
        self.hashmap[val] = self.length
        self.length += 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hashmap:
            return False
        self.hashmap[self.data[-1]] = self.hashmap[val]
        self.data[-1], self.data[self.hashmap[val]] = self.data[self.hashmap[val]], self.data[-1]
        self.data.pop()
        del self.hashmap[val]
        self.length -= 1
        return True

    def getRandom(self) -> int:
        return random.choice(self.data)
