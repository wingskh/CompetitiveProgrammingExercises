# https://www.facebook.com/codingcompetitions/hacker-cup/2023/practice-round/problems/B

input_file = open('./dim_sum_delivery_input.txt')

num_of_case = int(input_file.readline())
output_file = open("output.txt", "w")

for i in range(num_of_case):
    r, c, a, b = map(int, input_file.readline().split())

    if c >= r:
        output_file.write(f'Case #{i+1}: NO\n')
    else:
        output_file.write(f'Case #{i+1}: YES\n')

output_file.close()
input_file.close()