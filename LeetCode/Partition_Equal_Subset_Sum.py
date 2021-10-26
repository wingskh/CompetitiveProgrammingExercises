# https://leetcode.com/problems/partition-equal-subset-sum/
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False
        elif total_sum == 0:
            return True

        target_value = int(total_sum // 2)
        last_set = set()

        for i in nums:
            cur_set = set()
            for j in last_set:
                if j + i < target_value:
                    cur_set.add(i + j)
                elif j + i == target_value:
                    return True

            if i < target_value:
                cur_set.add(i)
            elif i == target_value:
                return True

            last_set = last_set.union(cur_set)
        return False


nums = [3, 3, 3, 4, 5]
sol = Solution()
print(sol.canPartition(nums))
