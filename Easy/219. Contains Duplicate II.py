def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    hashmap = {}
    for i, v in enumerate(nums):
        if hashmap.get(v) is not None and i - hashmap[v] <= k:
            return True
        hashmap[v] = i
    return False
