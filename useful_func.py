# import sys

# sys.path.append("..")
# from useful_func import *


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
