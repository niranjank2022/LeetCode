def summaryRanges(nums: list[int]) -> list[str]:
    start = nums[0]
    answer = []
    n = len(nums)
    for i in range(len(nums)):
        if i == n - 1:
            answer.append(f"{start}->{nums[i]}" if start != nums[i] else f"{start}")
        elif nums[i + 1] - nums[i] != 1:
            answer.append(f"{start}->{nums[i]}" if start != nums[i] else f"{start}")
            start = nums[i + 1]

    return answer


if __name__ == '__main__':
    testcases = [[0, 1, 2, 4, 5, 7], [0, 2, 3, 4, 6, 8, 9]]
    for case in testcases:
        print(f"{case} -> {summaryRanges(case)}")
