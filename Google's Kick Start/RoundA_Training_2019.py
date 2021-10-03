import sys


def cal_prefix_sum(x, n, length):
    y = [None] * (length-n+1)
    y[0] = x[0]

    for i in range(1, n-1):
        y[0] += x[i]

    for i in range(1, length-n+1):
        y[i] = y[i-1]-x[i-1]+x[i+n-2]

    return y


def find_min_traning_time(array, n):
    min_time = sys.maxsize
    k = 0
    prefix_sum = cal_prefix_sum(array, n, len(array))

    for i in range(n-1, len(array)):
        sum_time = array[i]*(n-1) - prefix_sum[i-n+1]
        if sum_time < min_time:
            min_time = sum_time
        k += 1
    return min_time


test_case = int(input())
i = 1
while test_case > 0:
    num_of_student, num_of_selected = list(map(int, input().split()))
    skill_list = list(map(int, input().split()))
    num_of_skills = len(skill_list)
    skill_list.sort()
    print("Case #" + str(i) + ":", str(find_min_traning_time(skill_list, num_of_selected)))
    i += 1
    test_case -= 1

