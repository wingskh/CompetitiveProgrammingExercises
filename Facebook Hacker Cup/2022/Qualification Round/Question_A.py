from collections import Counter

def no_duplicated_style():
    styles_count = Counter(styles)
    duplicated_count = 0

    # Case 1
    if len(styles) > 2*k:
        return "NO"

    for style in styles_count:
        if styles_count[style] > 1:
            duplicated_count += 1
            # Case 2
            if styles_count[style] > 2:
                return "NO"
    # Case 3
    return "NO" if duplicated_count > k else "YES"

with open('./second_hands_input.txt') as file:
    num_of_case = int(file.readline())

    for i in range(num_of_case):
        n, k = map(int, file.readline().split())
        # styles = list(map(int, file.readline().split()))
        styles = list(file.readline().split())
        result = no_duplicated_style()
        print(f'Case #{i+1}:', result)

# Rejected:
# Case 1: len(styles) > 2*k 
# Case 2: one of the part > 2
# Case 3: len(duplicated style) > k 

# 5
# 3 2
# 1