class MyHashSet:

    def __init__(self):
        self.bucket = [[] for _ in range(10)]

    def add(self, key: int) -> None:
        if not key in self.bucket[key % 10]:
            self.bucket[key % 10].append(key)

    def remove(self, key: int) -> None:
        if key in self.bucket[key % 10]:
            self.bucket[key % 10].remove(key)

    def contains(self, key: int) -> bool:
        return key in self.bucket[key % 10]
