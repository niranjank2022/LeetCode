def arraySign(nums: list[int]) -> int:
    negative = 0
    for num in nums:
        if num == 0:
            return num
        elif num < 0:
            negative += 1

    return -1 if negative % 2 else 1


if __name__ == '__main__':
    testcases = [[-1, -2, -3, -4, 3, 2, 1], [1, 5, 0, 2, -3], [-1, 1, -1, 1, -1], ]
    for case in testcases:
        print(f"{case} -> {arraySign(case)}")
