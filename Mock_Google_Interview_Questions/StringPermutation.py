# https://www.youtube.com/watch?v=JHzX-57dgn0&ab_channel=KeertiPurswani

# If the chars in smallString cannot be duplicated
# n: num of char in bigString
# m: num of char in smallString
# Time Complexity   (on average) = O(n)
#                   (worst)      = O(n^2)
# Space Complexity               = O(m)
def find_string_permutation(bigString, smallString):
    big_string_length = len(bigString)
    small_string_length = len(smallString)
    dp = [""] * big_string_length
    dp[0] = bigString[0]
    small_string_set = set(smallString)
    result = []
    for i in range(big_string_length - small_string_length + 1):
        cur_string = bigString[i : i + small_string_length]
        if set(cur_string) == small_string_set:
            result.append(cur_string)
    return result


# If the chars in smallString can be duplicated
# n: num of char in bigString
# m: num of char in smallString
# Time Complexity   = O(n*m)
# Space Complexity  = O(n*m)
def find_string_permutation(bigString, smallString):
    def string_to_dict(string, smallString):
        small_string_dict = {}
        for i in string:
            if i in smallString:
                if i not in small_string_dict:
                    small_string_dict[i] = 0
                small_string_dict[i] += 1
        return small_string_dict

    big_string_length = len(bigString)
    small_string_length = len(smallString)
    small_string_dict = string_to_dict(smallString, smallString)
    small_string_keys, small_string_values = list(small_string_dict.keys()), list(
        small_string_dict.values()
    )
    char_to_index = {key: index for index, key in enumerate(small_string_keys)}
    dp = [[0] * len(small_string_keys) for _ in range(big_string_length)]

    beginning_string_dict = string_to_dict(bigString[:small_string_length], smallString)
    for j in range(small_string_length):
        if small_string_keys[j] in beginning_string_dict:
            dp[small_string_length - 1][j] = min(
                beginning_string_dict[small_string_keys[j]], small_string_values[j]
            )

    result = (
        []
        if dp[small_string_length - 1] != small_string_values
        else [bigString[:small_string_length]]
    )

    for i in range(small_string_length, big_string_length):
        if bigString[i] in smallString:
            remove_char_col = char_to_index[bigString[i - small_string_length]]
            cur_char_col = char_to_index[bigString[i]]
            need_append = True
            for j in range(small_string_length):
                if j == remove_char_col:
                    dp[i][remove_char_col] = max(dp[i - 1][remove_char_col] - 1, 0)
                if j == cur_char_col:
                    dp[i][cur_char_col] = dp[i - 1][cur_char_col] + 1

                if j != remove_char_col and j != cur_char_col:
                    dp[i][j] = dp[i - 1][j]

                if dp[i][j] < small_string_values[j]:
                    need_append = False

            if need_append:
                result.append(bigString[i - small_string_length + 1 : i + 1])

    return result


big_string = "cbabcacabca"
smallString = "abc"
print(find_string_permutation(big_string, smallString))
