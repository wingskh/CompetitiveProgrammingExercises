from collections import Counter


def has_two_friends():
    exist_tree = False
    for i in range(row):
        trees.append([*file.readline().strip()])
        if '^' in trees[-1]:
            exist_tree = True

    if exist_tree:
        return "Possible" if row != 1 and col != 1 else "Impossible"
    else:
        return "Possible"

with open('./second_friend_input.txt') as file:
    num_of_case = int(file.readline())
    for i in range(num_of_case):
        row, col = list(map(int, file.readline().split(' ')))
        trees = []
        result = has_two_friends()
        print(f'Case #{i+1}:', result)
        if result =="Possible":
            if row != 1 and col != 1:
                for _ in range(row):
                    print('^'*col)
            else:
                for _ in range(row):
                    print('.'*col)
