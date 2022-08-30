import math


with open('./second_second_meaning_input.txt') as file:
    num_of_case = int(file.readline())
    for i in range(num_of_case):
        n = int(file.readline())
        c1 = file.readline().strip()
        c1_len = len(c1)
        height = math.ceil(math.log(n / (2**c1_len-1), 2) + 1 + c1_len)
        if c1_len >= height:
            c1 = c1[:height]
            c1_len = height
        print(f'Case #{i+1}:')
        counter = 0
        for i in range(2**height):
            leaf = format(i, f'0{height}b').replace('0', '-').replace('1', '.')
            if not leaf.startswith(c1):
                print(leaf)
                counter += 1
                if counter == n - 1:
                    break
            