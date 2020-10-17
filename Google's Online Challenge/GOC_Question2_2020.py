# in a list, there is only 1 and 0 in each list element which represents the ith location contain a balloon or not.
# In every second, you can move the balloon to left or right.
# Then, you need to return a list in which each ith element represents the time that moving all the balloons to ith location

def find_footsteps_list(input_list):
    has_bal_list = []
    footstep_list = []
    for index, element in enumerate(input_list):
        footstep_list.append(0)
        if element == 1:
            has_bal_list.append(index)
            footstep_list[0] += index
    
    bal_index = 0
    for index in range(1, len(footstep_list)):
        footstep_list[index] = footstep_list[index-1] + bal_index - (len(has_bal_list)-bal_index)
        if has_bal_list[bal_index] <= index:
            bal_index += 1
    return footstep_list


N = 5
input_string = '0 1 1 0 1'
input_list = list(map(int, input_string.split(' ')))
print(find_footsteps_list(input_list))
