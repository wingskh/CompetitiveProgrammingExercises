# https://leetcode.com/problems/maximum-length-of-repeated-subarray/
class Solution:
    def findLength(self, nums1, nums2) -> int:
        nums1 = [-1] + nums1
        nums2 = [-2] + nums2
        nums1_length = len(nums1)
        nums2_length = len(nums2)
        dp = [[0] * nums2_length for _ in range(nums1_length)]
        result = 0
        for i in range(1, nums1_length):
            for j in range(1, nums2_length):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    result = max(result, dp[i][j])
        return result

    def findLength(self, nums1, nums2) -> int:
        nums1 = [-1] + nums1
        nums2 = [-2] + nums2
        nums1_length = len(nums1)
        nums2_length = len(nums2)
        dp = [[0] * nums2_length for _ in range(nums1_length)]
        result = 0
        for i in range(1, nums1_length):
            for j in range(1, nums2_length):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    result = max(result, dp[i][j])
        return result


nums1 = [1, 2, 3, 2, 1]
nums2 = [3, 2, 1, 4, 7]
nums1 = [0,0,0,0,0]
nums2 = [0,0,0,0,0]
sol = Solution()
print(sol.findLength(nums1, nums2))
