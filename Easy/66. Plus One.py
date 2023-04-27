def plusOne(digits: list[int]) -> list[int]:
    carry = 1
    for i in reversed(range(len(digits))):
        num = digits[i]
        digits[i] = (carry + num) % 10
        carry = (carry + num) // 10

    if carry > 0:
        digits.insert(0, carry)
    return digits


def main():
    testcases = [[1, 2, 3], [4, 3, 2, 1], [9]]
    for case in testcases:
        print(f"{case} --> {plusOne(case)}")


main()
