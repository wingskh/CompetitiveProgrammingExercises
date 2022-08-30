import sys

sys.setrecursionlimit(1000000000)
# def is_there_any_tree():


# def is_valid_flood_fill(cur_row, cur_col):
#     def dfs(cur_row, cur_col):
#         if (
#             is_valid(cur_row, cur_col)
#             and trees[cur_row][cur_col] != "!"
#             and count_neighbour_tree(cur_row, cur_col) < 3
#         ):
#             if trees[cur_row][cur_col] == "^":
#                 # raise
#                 return False

#             trees[cur_row][cur_col] = "!"
#             # dfs(cur_row+1, cur_col)
#             # dfs(cur_row,cur_col+1)
#             # dfs(cur_row-1,cur_col)
#             # dfs(cur_row,cur_col-1)
#             return (
#                 dfs(cur_row + 1, cur_col)
#                 and dfs(cur_row, cur_col + 1)
#                 and dfs(cur_row - 1, cur_col)
#                 and dfs(cur_row, cur_col - 1)
#             )

#         return True

#     # try:
#     #     dfs(cur_row, cur_col)
#     #     return True
#     # except Exception as e:
#     #     # output_file.write(e)
#     #     return False
#     return dfs(cur_row, cur_col)




def is_valid_flood_fill(cur_row, cur_col):
    if trees[cur_row][cur_col] == "!":
        return True
    stack = [(cur_row, cur_col)]
    while stack:
        r, c = stack.pop()
        if trees[r][c] == "^":
            return False
        if (r, c) in no_adj_trees:
            no_adj_trees.remove((r, c))
        trees[r][c] = "!"
        stack += ((r + i, c + j) for i, j in ((-1,0),(1,0),(0,1),(0,-1)) if 
            0 <= r + i < len(trees) and 
            0 <= c + j < len(trees[0]) and 
            trees[r + i][c + j] != "#" and count_neighbour_tree(cur_row, cur_col) < 3)
    return True


def is_valid(cur_row, cur_col):
    if (
        cur_row < 0
        or cur_col < 0
        or cur_row >= row
        or cur_col >= col
        or trees[cur_row][cur_col] == "#"
    ):
        return 0
    return 1


def count_neighbour_tree(r, c):
    neighbour_count = 0
    for i in range(4):
        adj_row = r + row_direction[i]
        adj_col = c + col_direction[i]
        neighbour_count += is_valid(adj_row, adj_col)
    return neighbour_count


def found_init_no_adj_trees():
    for r in range(row):
        for c in range(col):
            neighbour_count = 0
            for i in range(4):
                adj_row = r + row_direction[i]
                adj_col = c + col_direction[i]
                neighbour_count += is_valid(adj_row, adj_col)
            if count_neighbour_tree(r, c) < 2:
                if trees[r][c] == "^":
                    return False
                no_adj_trees.add((r, c))

    return True


with open("./second_second_friend_input.txt") as file:
    num_of_case = int(file.readline())
    output_file = open("output.txt", "w")
    for i in range(num_of_case):
        row, col = list(map(int, file.readline().split(" ")))
        trees = []
        visited = []
        ori_tree_loc = []
        stone_count = 0
        row_direction = [0, 1, 0, -1]
        col_direction = [-1, 0, 1, 0]
        no_adj_trees = set()
        exist_tree = False
        print(f"Case #{i+1}: \n")
        for _ in range(row):
            tree_row = file.readline().strip()
            if not exist_tree and "^" in tree_row:
                exist_tree = True
            trees.append([*tree_row])
        if not exist_tree:
            output_file.write(f"Case #{i+1}: Possible\n")
            for r in trees:
                output_file.write("".join(r) + "\n")
        else:
            valid = found_init_no_adj_trees()
            if not valid:
                output_file.write(f"Case #{i+1}: Impossible\n")
            else:
                found_invalid = False
                while len(no_adj_trees) != 0:
                    no_adj_tree = no_adj_trees.pop()
                    valid_flood_fill = is_valid_flood_fill(
                        no_adj_tree[0], no_adj_tree[1]
                    )
                    if not valid_flood_fill:
                        found_invalid = True
                        break
                if found_invalid:
                    output_file.write(f"Case #{i+1}: Impossible\n")
                else:
                    output_file.write(f"Case #{i+1}: Possible\n")
                    for r in trees:
                        tree_row = "".join(r)
                        output_file.write(
                            tree_row.replace(".", "^").replace("!", ".") + "\n"
                        )

    print("=" * 50, "end")
    output_file.close()
