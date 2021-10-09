<span style="font-family:Papyrus; font-size:4em;">Dynamic Programming</span>

### Type 1: Time Series I
dp[i][j]:
```
i: Day -> inferred by dp[i-1]
j: Action -> inferred by cost+dp[i-1][j-1] or dp[i-1][j]
```

### Type 2: Time Series II
dp[i][j]:
```
i: Day -> inferred by dp[k] where k < i
j: Action -> inferred by cost+dp[k][j-1] or dp[k][j]
```

### Type 3: Two Arrays Operation
dp[i][j]:
```
i: array1 operation
j: array2 operation
```
```
inferred by dp[i][j - 1], dp[i - 1][j] and dp[i - 1][j-1]
```

### Type 4: Continuous Partition
dp[i][k]:
```
i: word[:j] / word[:j+1]
k: k groups
```
```
inferred by dp[l][j - 1] for l in range(i)
```

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

><span style="font-family:calibri; font-size:15px;color:black">seems can use Frontier Set to replace dp</span>
>>`474.    Ones and Zeroes`
>>`494.    Target Sum`
>>`1049.   Last Stone Weight II`