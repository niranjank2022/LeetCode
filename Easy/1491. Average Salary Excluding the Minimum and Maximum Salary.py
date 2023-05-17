def average(salary: list[int]) -> float:
    max_value = max(salary[0], salary[1])
    min_value = min(salary[0], salary[1])

    salary_sum = 0
    salary_count = 0
    for i in range(2, len(salary)):

        if salary[i] > max_value:
            salary_sum += max_value
            max_value = salary[i]
        elif salary[i] < min_value:
            salary_sum += min_value
            min_value = salary[i]
        else:
            salary_sum += salary[i]
        salary_count += 1

    return salary_sum / salary_count


if __name__ == '__main__':
    testcases = [[4000, 3000, 1000, 2000], [1000, 2000, 3000]]
    for case in testcases:
        print(f"{case} -> {average(case)}")
