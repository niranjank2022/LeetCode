def countQuadruplets(nums: list[int]) -> int:
    count = 0
    leng = len(nums)
    for i in range(leng - 3):
        for j in range(i + 1, leng - 2):
            for k in range(j + 1, leng - 1):
                for l in range(k + 1, leng):
                    if nums[i] + nums[j] + nums[k] == nums[l]:
                        count += 1

    return count


def main():
    testcases = [[1, 2, 3, 6], [3, 3, 6, 4, 5], [1, 1, 1, 3, 5]]
    for case in testcases:
        print(case, countQuadruplets(case))


main()
