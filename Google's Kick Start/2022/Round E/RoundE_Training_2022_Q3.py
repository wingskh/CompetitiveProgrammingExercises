test_case = int(input())

for i in range(test_case):
    _ = input()
    palindrome = input()
    result = palindrome
    for window_size in range(1, len(palindrome)):
        if not (len(palindrome) / window_size).is_integer():
            continue
        elif palindrome[: window_size] * int(len(palindrome) / window_size) == palindrome:
            
            result = palindrome[: window_size]
            break
    print("Case #" + str(i + 1) + ":", result)
