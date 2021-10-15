# https://www.youtube.com/watch?v=rw4s4M3hFfs&t=406s


def find_suitable_apartment(blocks, reqs):
    blocks_length = len(blocks)
    reqs_length = len(reqs)
    dp = [[float("inf")] * (reqs_length + 1) for _ in range(blocks_length)]
    best_apartment_index = -1
    best_apartment_path = float("inf")
    for i in range(reqs_length):
        if blocks[0][i]:
            dp[0][i] = 0

    for i in range(1, blocks_length):
        dp[i][-1] = 0
        for j in range(reqs_length):
            if blocks[i][j]:
                dp[i][j] = 0
            else:
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j])

            dp[i][-1] = max(dp[i][-1], dp[i][j])

    for i in range(blocks_length - 2, -1, -1):
        dp[i][-1] = 0
        for j in range(reqs_length):
            if blocks[i][j]:
                dp[i][j] = 0
            else:
                dp[i][j] = min(dp[i + 1][j] + 1, dp[i][j])
            dp[i][-1] = max(dp[i][-1], dp[i][j])
        if dp[i][-1] < best_apartment_path:
            best_apartment_path = dp[i][-1]
            best_apartment_index = i

    return best_apartment_index


blocks = [
    [False, True, False],
    [True, False, False],
    [True, True, False],
    [False, True, False],
    [False, True, True],
]
reqs = [0, 1, 2]
print(find_suitable_apartment(blocks, reqs))
