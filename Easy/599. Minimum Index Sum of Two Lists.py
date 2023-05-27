import sys


def findRestaurant(list1: list[str], list2: list[str]) -> list[str]:
    hashmap = {}
    for i, item in enumerate(list1):
        hashmap[item] = i

    minSum = sys.maxsize
    answer = []
    for i, item in enumerate(list2):
        if item in hashmap:
            indexSum = i + hashmap[item]
            if indexSum < minSum:
                answer.clear()
            if indexSum <= minSum:
                answer.append(item)

            minSum = min(minSum, indexSum)

    return answer
