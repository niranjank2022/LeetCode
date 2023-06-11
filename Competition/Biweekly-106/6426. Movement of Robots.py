def sumDistance(nums: list[int], s: str, d: int) -> int:
    def swap(s):
        return 'R' if s == 'L' else 'L'

    n = len(nums)
    for _ in range(d):
        for i in range(1, n, 2):
            nums[i], nums[i - 1] = nums[i] + 1 if s[i] == 'R' else nums[i] - 1, nums[i - 1] + 1 if s[i - 1] == 'R' else \
                nums[i - 1] - 1
            if nums[i] == nums[i - 1]:
                s = s[:i - 1] + swap(s[i - 1]) + swap(s[i]) + s[i + 1:]

        if n % 2:
            nums[n - 1] = nums[n - 1] + 1 if s[n - 1] == 'R' else nums[n - 1] - 1

    distance = 0
    for i in range(n):
        for j in range(i + 1, n):
            distance += abs(nums[j] - nums[i])

    return distance % (10 ** 9 + 7)


if __name__ == '__main__':
    testcases = [([-2, 0, 2], "RLL", 3), ([1, 0], "RL", 2)]
    for case in testcases:
        print(f"{case} -> {sumDistance(case[0], case[1], case[2])}")
