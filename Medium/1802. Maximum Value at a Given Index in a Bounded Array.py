def maxValue(n: int, index: int, maxSum: int) -> int:
    hashmap = {}
    k = maxSum // n + 1
    for i in range(n):

        times = i
        while k >= 1:
