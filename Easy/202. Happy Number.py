def isHappy(n: int) -> bool:
    nums = list()
    sqrSum = n
    while sqrSum != 1:
        sqrSum = sum(map(lambda x: int(x) ** 2, str(sqrSum)))
        if sqrSum in nums:
            # print(nums)

            return False
        nums.append(sqrSum)

    # print(nums)
    return True


print(isHappy(19))
