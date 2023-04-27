def addDigits(nums: int) -> int:
    number = str(nums)

    while len(number) > 1:
        nums = 0
        for i in number:
            nums += int(i)
        number = str(nums)

    return nums


def main():
    testcases = [38, 0, 234, 95]
    for case in testcases:
        print(f"{case} -> {addDigits(case)}")


main()
