# https://leetcode.com/problems/reduce-array-size-to-the-half/
# https://leetcode.com/problems/reduce-array-size-to-the-half/discuss/2443799/python-easily-understood-faster-than-90-explanation

from collections import Counter


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        total_len = len(arr)
        target_len = total_len // 2
        counter = 0
        arr_chr_count = Counter(arr).most_common()
        for x in arr_chr_count:
            total_len -= x[1]
            counter += 1
            print(counter)
            if total_len <= target_len:
                break

        return counter


arr = [7,7,7,7,7,7]
sol = Solution()
result = sol.minSetSize(arr)
print(result)
