def isHappy(n: int) -> bool:
    nums = set()
    sqrSum = n
    while sqrSum != 1:
        sqrSum = sum(map(lambda x: int(x) ** 2, str(sqrSum)))
        if sqrSum in nums:
            return False
        nums.add(sqrSum)

    return True


print(isHappy(19))
