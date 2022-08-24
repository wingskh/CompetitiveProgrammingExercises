import collections
from bisect import bisect_left

test_case = int(input())

for i in range(test_case):
    _ = input()
    ratings = list(map(int, input().split(" ")))
    sorted_rating = sorted(ratings)
    duplication = set(
        [item for item, count in collections.Counter(ratings).items() if count > 1]
    )

    result = []
    for rating in ratings:
        leftmost_index = bisect_left(sorted_rating, 2 * rating + 1)

        if (
            sorted_rating[leftmost_index - 1] == rating and rating not in duplication
        ) and leftmost_index - 1 >= 0:
            leftmost_index -= 1

        if 2 * rating >= sorted_rating[leftmost_index - 1]:
            result.append(str(sorted_rating[leftmost_index - 1]))
        else:
            result.append("-1")

    print("Case #" + str(i + 1) + ":", " ".join(result))
