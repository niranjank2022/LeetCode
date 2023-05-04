def predictPartyVictory(senate: str) -> str:
    stack = list(senate)

    while len(stack) > 1:
        flag = 0
        for i in stack[1:]:
            if i != stack[0]:
                stack.remove(i)
                flag = 1
                stack.append(stack.pop(0))
                break
        if flag == 0:
            break

    return "Radiant" if stack[0] == 'R' else "Dire"


if __name__ == '__main__':
    testcases = ["RD", "RDD", "DDRRRR", "RRDDD", "DDRRR"]
    for case in testcases:
        print(f"{case} -> {predictPartyVictory(case)}")
