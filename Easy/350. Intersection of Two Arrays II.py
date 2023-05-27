def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    hashmap = {}
    answer = []
    for num in nums1:
        hashmap[num] = hashmap.get(num, 0) + 1

    for num in nums2:
        if hashmap.get(num):
            answer.append(num)
            hashmap[num] -= 1

    return answer
