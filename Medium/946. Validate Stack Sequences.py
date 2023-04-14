def validateStackSequences(pushed: list[int], popped: list[int]) -> bool:
    stack = list()
    j = 0
    for i in pushed:
        stack.append(i)
        while stack != [] and stack[-1] == popped[j]:
            j += 1
            stack.pop()

    while j < len(popped):
        if popped[j] == stack.pop():
            j += 1
        else:
            return False

    return True


def main():
    testcases = [[[1, 2, 3, 4, 5], [4, 5, 3, 2, 1]], [[1, 2, 3, 4, 5], [4, 3, 5, 1, 2]], [[2, 1, 0], [1, 2, 0]]]
    for case in testcases:
        print(f"'{case}' ~ {validateStackSequences(case[0], case[1])}")
        print("===============")


main()
