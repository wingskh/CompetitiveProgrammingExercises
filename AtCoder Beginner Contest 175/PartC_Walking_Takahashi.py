x, k, d = list(map(int, input().split(' ')))
x = abs(x)
if d*k > x:
    nearest_x = x % d
    nearest_k = k - x // d

    if nearest_k % 2 != 0:
        print(d - nearest_x)
    else:
        print(nearest_x)
else:
    print(x-d*k)
