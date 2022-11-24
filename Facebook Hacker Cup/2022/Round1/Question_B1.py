with open('./watering_well_chapter_1_input.txt') as file:
    num_of_case = int(file.readline())
    moduler = 1000000007
    output_file = open("output.txt", "w")

    for i in range(num_of_case):
        trees_len = int(file.readline())
        trees = []
        for _ in range(trees_len):
            trees.append(list(map(int, file.readline().split())))
            
        wells_len = int(file.readline())
        wells = []
        inconvenience = 0
        for _ in range(wells_len):
            well_loc = list(map(int, file.readline().split()))
            # wells.append()

            for tree in trees:
                inconvenience += (well_loc[0] - tree[0])**2 % moduler + (well_loc[1] - tree[1])**2 % moduler
                inconvenience %= moduler

        output_file.write(f'Case #{i+1}: {inconvenience}\n')
        
    output_file.close()
