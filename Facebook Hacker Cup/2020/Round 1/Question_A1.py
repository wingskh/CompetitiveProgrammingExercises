def find_all_perimeter():
    rightmost_coord = -1
    range_dict = dict()
    global latest_perimeter_product
    prior_perimeter = 0

    for room_index in range(len(k_left)):
        new_width = width
        new_height = k_height[room_index]

        if k_left[room_index] <= rightmost_coord:
            new_width = k_left[room_index] + width - rightmost_coord
            highest_height = 0
            for key in list(range_dict.keys()):
                if k_left[room_index] in key:
                    highest_height = max(highest_height, range_dict[key])
                else:
                    del range_dict[key]

            if highest_height >= new_height:
                new_height = 0
            else:
                new_height = new_height-highest_height
        else:
            range_dict.clear()

        range_dict[range(k_left[room_index], k_left[room_index]+width+1)] = k_height[room_index]
        if room_index != 0:
            prior_perimeter += (new_height+new_width)*2
            latest_perimeter_product = (latest_perimeter_product*prior_perimeter) % 1000000007

        else:
            prior_perimeter = (new_height+new_width)*2
            latest_perimeter_product = (new_height+new_width)*2 % 1000000007
        rightmost_coord = k_left[room_index]+width


with open('./round1_qa1_2020.txt') as file:
    num_of_case = int(file.readline())

    for i in range(num_of_case):
        num_of_room, k, width = map(int, file.readline().split())
        k_left = list(map(int, file.readline().split()))
        abcd_left = list(map(int, file.readline().split()))
        k_height = list(map(int, file.readline().split()))
        abcd_height = list(map(int, file.readline().split()))
        latest_perimeter_product = 0

        if num_of_room == k:
            find_all_perimeter()
            print(f'Case #{i+1}:', latest_perimeter_product)
            continue

        for j in range(k, num_of_room):
            left_i = (abcd_left[0]*k_left[j-2] + abcd_left[1]*k_left[j-1] + abcd_left[2]) % abcd_left[3] + 1
            height_i = (abcd_height[0]*k_height[j-2] + abcd_height[1]*k_height[j-1] + abcd_height[2]) % abcd_height[3] + 1
            k_left.append(left_i)
            k_height.append(height_i)

        find_all_perimeter()
        print(f'Case #{i+1}:', latest_perimeter_product)
