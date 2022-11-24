with open('./consecutive_cuts_chapter_2_input.txt') as file:
    num_of_case = int(file.readline())
    output_file = open("output.txt", "w")

    for i in range(num_of_case):
        nums_len, k = map(int, file.readline().split())
        ori_order  = file.readline().strip()
        target_order  = file.readline().strip()
        
        # full_seq =  ori_order + " " + ori_order 
        
        if target_order not in f"{ori_order} {ori_order}":
            output_file.write(f'Case #{i+1}: NO\n')
            continue

            
        if nums_len == 2:
            if (k % 2 == 0 and ori_order == target_order) or (k % 2 == 1 and ori_order != target_order):
                output_file.write(f'Case #{i+1}: YES\n')
            else:
                output_file.write(f'Case #{i+1}: NO\n')
        else:
            if (ori_order == target_order and k == 1) or (ori_order != target_order and k == 0):
                output_file.write(f'Case #{i+1}: NO\n')
            else:
                output_file.write(f'Case #{i+1}: YES\n')

    output_file.close()

# 1 2 3 4 5 6 7 8 1 2 3 4 5 6 7 8

# 4
# 5 1
# 5 1 2 4 3
# 2 4 3 5 1
# 4 10
# 3 1 4 2
# 1 2 3 4
# 4 0
# 3 1 4 2
# 2 3 1 4
# 3 3
# 3 2 1
# 1 2 3
# 2 3 1
# 3 1 2
# 1 2 3

# 3 1 2
#
#

# 1 2 -> odd k: 2, even k: 1

# 1 2 3
# k = 1:
#       2 3 1
#               3 1 2
#               1 2 3
#       3 1 2
#               1 2 3
#               2 1 3










