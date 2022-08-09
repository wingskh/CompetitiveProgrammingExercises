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

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def list_to_treenode(elements):
    root_node = TreeNode(x=elements[0])
    nodes = [root_node]
    for i, x in enumerate(elements[1:]):
        if x is None:
            continue
        parent_node = nodes[i // 2]
        is_left = (i % 2 == 0)
        node = TreeNode(x=x)
        if is_left:
            parent_node.left = node
        else:
            parent_node.right = node
        nodes.append(node)

    return root_node
