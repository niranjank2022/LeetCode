def mostCompetitive(nums: list[int], k: int) -> list[int]:
    n = len(nums)
    length = 0
    stack = []

    for i in range(n):

        while stack and stack[-1] > nums[i] and (n - i - 1 >= k - length):
            stack.pop()
            length -= 1
        if length < k:
            stack.append(nums[i])
            length += 1

    return stack


if __name__ == '__main__':
    testcases = [([3, 5, 2, 6], 2), ([2, 4, 3, 3, 5, 4, 9, 6], 4), ([42, 66, 8, 80, 2], 3),
                 ([84, 10, 71, 23, 66, 61, 62, 64, 34, 41, 80, 25, 91, 43, 4, 75, 65, 13, 37, 41, 46, 90, 55, 8, 85, 61,
                   95, 71], 24), (
                 [11, 52, 57, 91, 47, 95, 86, 46, 87, 47, 70, 56, 54, 61, 89, 44, 3, 73, 1, 7, 87, 48, 17, 25, 49, 54,
                  6, 72, 97, 62, 16, 11, 47, 34, 68, 58, 14, 36, 46, 65, 2, 15], 18)]
    for case in testcases:
        print(f"{case} ->\n{mostCompetitive(case[0], case[1])}")
