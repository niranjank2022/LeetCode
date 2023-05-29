def minimumCost(s: str) -> int:
    n = len(s)
    count0 = s.count('0', 0, n // 2)
    count1 = s.count('1', n // 2)
    print(count0, n // 2 - count0, count1, n // 2 - count1)

    # if count0 >


if __name__ == '__main__':
    testcases = ["0011", "010101", "11111 010101"]
    for case in testcases:
        print(f"{case} -> {minimumCost(case)}")

'''
000110

101 111
 
'''

