def maxStrength(nums: list[int]) -> int:
    nums.sort()
    j, n, answer, negative = 0, len(nums), 1, 0
    isMultiplied = False

    for i in range(n - 1):
        if nums[i] >= 0:
            break
        negative += 1
        answer *= nums[i]
        if nums[i + 1] >= 0:
            if negative % 2 == 1:
                answer //= nums[i]
            if negative > 0:
                j = i + 1
            break
        isMultiplied = True

    if j == 0 and negative > 0:
        if negative % 2 == 0:
            return answer
        j = n - 1

    for i in range(j, n):
        if nums[i] == 0 and isMultiplied:
            continue
        if answer != 0:
            answer *= nums[i]
        else:
            answer = nums[i]

    return answer


if __name__ == '__main__':
    testcases = [[3, -1, -5, 2, 5, -9], [-4, -5, -4], [9, 6, 3], [-1, 0], [2, 2, 7, 0, -4, 9, 4]]
    for case in testcases:
        print(f"{case} -> {maxStrength(case)}")
