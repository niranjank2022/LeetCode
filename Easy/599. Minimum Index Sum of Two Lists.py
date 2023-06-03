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


if __name__ == '__main__':
    testcases = [[["Shogun", "Tapioca Express", "Burger King", "KFC"], ["KFC", "Shogun", "Burger King"]],
                 [["happy", "sad", "good"], ["sad", "happy", "good"]],
                 [["Shogun", "Tapioca Express", "Burger King", "KFC"], ["KFC", "Shogun", "Burger King"]]]

    for case in testcases:
        print(f"{case} -> {findRestaurant(case[0], case[1])}")
