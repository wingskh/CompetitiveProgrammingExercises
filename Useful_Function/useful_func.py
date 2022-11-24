# import sys

# sys.path.append("..")
# from useful_func import *


def display_matrix(matrix):
    import numpy as np

    a = np.array(matrix)
    print(a)


def display_matrix(matrix, word1, word2):
    if isinstance(word1, list):
        word1 = list(map(str, word1))
    if isinstance(word2, list):
        word2 = list(map(str, word2))
    matrix_height = len(matrix)
    matrix_width = len(matrix[0])
    word1_length = len(word1)
    word2_length = len(word2)

    for _ in range(matrix_width - word2_length):
        print("\t", end="")

    for c in word2:
        print(f"\t{c}", end="")
    print()

    for i in range(matrix_height):
        if i >= matrix_height - word1_length:
            print(f"{word1[i-matrix_height+word1_length]}", end="")
        for j in range(matrix_width):
            print(f"\t{matrix[i][j]}", end="")
        print()


def direction(row, col):
    row_direction = [0, 1, 0, -1]
    col_direction = [-1, 0, 1, 0]

    for i in range(4):
        adj_row = row + row_direction[i]
        adj_col = col + col_direction[i]

    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for i in range(4):
        adj_row, adj_col = row + direction[i][0], col + direction[i][1]

    return adj_row, adj_col


def leftmost_binary_search(nums, target):
    left_index, right_index = 0, len(nums) - 1
    while left_index <= right_index:
        middle_index = left_index + (right_index - left_index) // 2
        if target == nums[0]:
            left_index = middle_index
            break
        if target < nums[0]:
            right_index = middle_index - 1
        else:
            left_index = middle_index + 1
