# https://leetcode.com/problems/top-k-frequent-elements/
from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurence_counter = defaultdict(int)
        for num in nums:
            occurence_counter[num] += 1

        top_k = list(dict(sorted(occurence_counter.items(), key=lambda x:x[1], reverse=True)).keys())[:k]
        return top_k
    

nums = [1,1,1,2,2,3]
k = 2
sol = Solution()
print(sol.topKFrequent(nums, k))
