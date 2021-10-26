<span style="font-family:Papyrus; font-size:4em;">Dynamic Programming</span>

### Type 1: Time Series I
dp[i][j]:
```
i: Day -> inferred by dp[i-1]
j: Action -> inferred by cost+dp[i-1][j-1] or dp[i-1][j]
```
>```
> LC 123.   Best Time to Buy and Sell Stock III
> LC 198.   House Robber
> LC 213.   House Robber II
> LC 276.   Paint Fence
> LC 309.   Best Time to Buy and Sell Stock with Cooldown
> LC 376.   Wiggle Subsequence
> LC 487.   Max Consecutive Ones II
> LC 903.   Valid Permutations for DI Sequence
> LC 1186.  Maximum Subarray Sum with One Deletion
>```

### Type 2: Time Series II
dp[i][j]:
```
i: Day -> inferred by dp[k] where k < i
j: Action -> inferred by cost+dp[k][j-1] or dp[k][j]
```
>```
> LC 300.   Longest Increasing Subsequence
> LC 368.   Largest Divisible Subset
> LC 1105.  Filling Bookcase Shelves
> LC 983.   Minimum Cost For Tickets
>```

### Type 3: Two Arrays Operation
dp[i][j]:
```
i: array1 operation
j: array2 operation
```
```
inferred by dp[i][j - 1], dp[i - 1][j] and dp[i - 1][j - 1]
```
>```
> LC 72.    Edit Distance
> LC 97.    Interleaving String
> LC 115.   Distinct Subsequences
> LC 727.   Minimum Window Subsequence
> LC 1092.  Shortest Common Supersequences
> LC 1143.  Longest Common Subsequences

### Type 4: Continuous Partition
dp[i][k]:
```
i: word[:j] / word[:j+1]
k: k groups
```
```
inferred by dp[l][j - 1] for l in range(i) + cost(word[j : i + 1])
```
>```
> LC 410.   Split Array Largest Sum
> LC 813.   Largest Sum of Averages
> LC 1278.  Palindrome Partitioning III
> LC 1335.  Minimum Difficulty of a Job Schedule
>```

### Type 5: Partition without dependency
dp[i][j]:
```
i: start index for string s
j: end index for string s
```
```
CANNOT inferred dp[i] by dp[j] where j < i
Inferr dp[0][-1] from the smallest parts first
```
```python
for length in range(2, nums_length + 1):
    for i in range(nums_length - length + 1):
        j = i + length - 1
        dp[i][j] = float("inf")
        for k in range(i, j + 1):
            ...
```
>```
> LC 516.   Longest Palindromic Subsequence
> LC 312.   Burst Balloons
> LC 375.   Guess Number Higher or Lower II
> LC 375.   Guess Number Higher or Lower II
> LC 1246.  Palindrome Removal
>```

### Type 6: Backpack Problem
dp[i][s]:
```
i: The round that using i items in total
s: current cost
```
```
Inferred dp[i][s] by dp[i - 1][s - nums[i]] and/or dp[i - 1][s + nums[i]]
as dp[i][s] is inferred by not using the ith items in the last round
```
>```
> LC 474.   Ones and Zeroes
> LC 494.   Target Sum
> LC 518.   Coin Change 2
> LC 879.   Profitable Schemes
> LC 956.   Tallest Billboard
> LC 1049.  Last Stone Weight II
>```

><span style="font-family:calibri; font-size:15px;color:black">seems can use Frontier Set/Dict to replace dp</span>
>>`474.    Ones and Zeroes`
>>`494.    Target Sum`
>>`956.    Tallest Billboard`
>>`1049.   Last Stone Weight II`

### Useful predefined function
```
string_name.isalpha()
string_name.isalnum()
string_name.isnumeric()
string_name.isdigit()
chr(ascii_code)                 # transform decimal number to char
ord(char_name)                  # transform char to decimal number
set_a.union(set_b)              # output {set_a} ∪ {set_b} 
set_a.difference(set_b)         # output {set_a} / {set_b} 
set_a.intersection(set_b)       # output {set_a} ∩ {set_b} 
```