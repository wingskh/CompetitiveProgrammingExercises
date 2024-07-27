# https://leetcode.com/problems/merge-triplets-to-form-target-triplet/
from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        result = [False]*3

        for triplet in triplets:
            calculated_triplet = [triplet[i] - target[i] for i in range(3)]
            if max(calculated_triplet) <= 0:
                for i in range(3):
                    if calculated_triplet[i] == 0:
                        result[i] = True
            if all(x for x in result):
                return True
        # print(result)
        return False 

triplets = [[2, 5, 3], [1, 8, 4], [1, 7, 5]]
target = [2, 7, 5]
# Output: True
triplets = [[2,5,3],[2,3,4],[1,2,5],[5,2,3]]
target = [5,5,5]
# Output: True
# triplets = [[3,4,5],[4,5,6]]
# target = [3,2,5]
# Output = False
sol = Solution()
print(sol.mergeTriplets(triplets, target))
