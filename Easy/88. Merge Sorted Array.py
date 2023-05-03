def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    if n > m:
        return
    curr = nums1.index(max(nums1))
    prev = curr - 1
    for num in nums2[::-1]:
        print("***", curr, prev, num, end=' ')
        if nums1[curr] < num:

            nums1.insert(curr + 1, num)
            nums1.remove(0)
            print(nums1, "***")

        elif nums1[curr] > num:
            while nums1[prev] > num:
                prev -= 1
                curr -= 1
            if nums1[prev] <= num:
                nums1.insert(prev + 1, num)
                nums1.pop()


def main():
    testcases = [([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3), ([1], 1, [], 0), ([0], 0, [1], 1)]
    for case in testcases:
        print(f"{case} ->", end=' ')
        merge(case[0], case[1], case[2], case[3])
        print(case[0])


main()
