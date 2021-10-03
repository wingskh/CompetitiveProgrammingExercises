## Dynamic Programming

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