class MyHashMap:

    def __init__(self):
        self.bucket = [[] for _ in range(100)]

    def findIndex(self, key):
        for i, (k, v) in enumerate(self.bucket[key % 100]):
            if k == key:
                return i
        return -1

    def put(self, key: int, value: int) -> None:
        i = self.findIndex(key)
        if i == -1:
            self.bucket[key % 100].append([key, value])
        else:
            self.bucket[key % 100][i][1] = value

    def get(self, key: int) -> int:
        i = self.findIndex(key)
        return self.bucket[key % 100][i][1] if i != -1 else -1

    def remove(self, key: int) -> None:
        i = self.findIndex(key)
        if i != -1:
            del self.bucket[key % 100][i]
