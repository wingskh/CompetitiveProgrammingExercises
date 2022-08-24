test_case = int(input())

for  i in range(test_case):
    n_cells = int(input())
    if n_cells < 6:
        print("Case #" + str(i + 1) + ":", 1)
    else:
        result = n_cells // 5
        padding = 1 if n_cells % 5 >= 1 else 0 
        print("Case #" + str(i + 1) + ":", result+padding)
