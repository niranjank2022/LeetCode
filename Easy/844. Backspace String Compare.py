def backspaceCompare(s: str, t: str) -> bool:
    stack1 = list()
    stack2 = list()
    for i in s:
        if i == '#' and len(stack1) >= 1:
            stack1.pop()
        if i != '#':
            stack1.append(i)

    for j in t:
        if j == '#' and len(stack2) >= 1:
            stack2.pop()
        if j != '#':
            stack2.append(j)

    return stack1 == stack2


def main():
    testcases = [('ab#c', 'ad#c'), ('ab##', 'c#d#'), ('a#c', 'b'), ("a##c", "#a#c"), ("y#fo##f", "y#f#o##f")]
    for case in testcases:
        print(f"s: {case[0]} t: {case[1]}: {backspaceCompare(case[0], case[1])}")


main()
