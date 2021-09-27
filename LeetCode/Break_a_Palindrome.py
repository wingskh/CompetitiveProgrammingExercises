def break_a_palindrome(palindrome):
    if len(palindrome) < 2:
        return ""
    
    for i in range(len(palindrome)):
        if i == (len(palindrome)-1)/2:
            continue
        if i != len(palindrome) - 1:
            # reverse_index = len(palindrome) - i -1
            if ord(palindrome[i]) > 97:
                palindrome = palindrome[:i] + 'a' + palindrome[i+1:]
                return palindrome
            else:
                continue
        else:
            if ord(palindrome[i]) > 97:
                palindrome = palindrome[:-1]+'a'
            else:
                palindrome = palindrome[:-1]+chr(ord(palindrome[i])+1)
                
    return palindrome


palindrome = "aba"
print(break_a_palindrome(palindrome))
