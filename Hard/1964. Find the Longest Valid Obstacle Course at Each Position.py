def binary_search(nums: list[int], n, target):
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] <= target and (mid == n - 1 or nums[mid + 1] > target):
            return mid + 1
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return 0


def longestObstacleCourseAtEachPosition(obstacles: list[int]) -> list[int]:
    answer = []
    lis = []
    n = 0
    for i in range(len(obstacles)):
        if not lis:
            lis.append(obstacles[i])
            indx = 0
            n += 1
        else:
            indx = binary_search(lis, len(lis), obstacles[i])
            if indx >= n:
                lis.append(obstacles[i])
                n += 1
            else:
                lis[indx] = obstacles[i]

        answer.append(indx + 1)

    return answer


if __name__ == '__main__':
    testcases = [[1, 2, 3, 2], [2, 2, 1], [3, 1, 5, 6, 4, 2], [5, 1, 5, 5, 1, 3, 4, 5, 1, 4]]
    for case in testcases:
        print(f"{case}\n{longestObstacleCourseAtEachPosition(case)}\n\n ")
