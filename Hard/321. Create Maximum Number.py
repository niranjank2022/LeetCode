def maxNumber(nums1: list[int], nums2: list[int], k: int) -> list[int]:
    n1 = len(nums1)
    n2 = len(nums2)
    length = 0
    stack = []
    popped = []

    i = j = 0

    while not (i >= n1 or j >= n2):

        if i >= n1:
            while stack and stack[-1] < nums2[j]:
                popped.append(stack.pop())
                length -= 1
            if length < k:
                stack.append(nums2[j])
                length += 1
                j += 1

        elif j >= n2:
            while stack and stack[-1] < nums1[i]:
                popped.append(stack.pop())
                length -= 1
            if length < k:
                stack.append(nums1[i])
                length += 1
                i += 1

        elif nums1[i] >= nums2[j]:
            while stack and stack[-1] < nums1[i]:
                popped.append(stack.pop())
                length -= 1
            if length < k:
                stack.append(nums1[i])
                length += 1
                i += 1

        else:
            while stack and stack[-1] < nums2[j]:
                popped.append(stack.pop())
                length -= 1
            if length < k:
                stack.append(nums2[j])
                length += 1
                j += 1

    print(popped)
    return stack


if __name__ == '__main__':
    testcases = [([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5), ([6, 7], [6, 0, 4], 5), ([3, 9], [8, 9], 3)]
    for case in testcases:
        print(f"{case} ->\n{maxNumber(case[0], case[1], case[2])}")
