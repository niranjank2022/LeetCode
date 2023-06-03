from heapq import *


class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = nums
        heapify(self.heap)
        for _ in range(len(nums) - self.k):
            heappop(self.heap)

    def add(self, val: int) -> int:
        heappush(self.heap, val)
        if len(self.heap) > self.k:
            heappop(self.heap)
        print(self.heap)
        return heappop(self.heap)


klarge = KthLargest(3, [4, 5, 8, 2])
print(klarge.add(3))
print(klarge.add(5))
print(klarge.add(10))

print(klarge.add(9))
print(klarge.add(4))
