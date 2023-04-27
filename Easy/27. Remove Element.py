def removeElement(self, nums: list[int], val: int) -> int:
    times = nums.count(val)
    size = len(nums)
    for i in range(times):
        nums.remove(val)

    return len(nums)