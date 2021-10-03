# https://leetcode.com/problems/median-of-two-sorted-arrays/submissions/
import bisect


def find_median_from_list(nums1):
    if len(nums1) % 2 == 0:
        half = int(len(nums1) / 2) - 1
        return sum(nums1[half : half + 2]) / 2, half + 0.5
    else:
        num = int(len(nums1) / 2)
        return nums1[num], num


def handle_insertion(longer_list, shorter_list):
    for value in shorter_list:
        bisect.insort(longer_list, value)

    result, _ = find_median_from_list(longer_list)
    return result


class Solution(object):
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        list1_median, index1 = find_median_from_list(nums1)
        list2_median, index2 = find_median_from_list(nums2)

        if len(nums1) <= 2 and len(nums2) >= len(nums1):
            return handle_insertion(nums2, nums1)
        elif len(nums2) <= 2 and len(nums1) >= len(nums2):
            return handle_insertion(nums1, nums2)
        if list1_median < list2_median:
            left = int(index1)
            right = int(len(nums2) - index2 - 1)
            drop_num = min(left, right)

            return self.findMedianSortedArrays(nums1[drop_num:], nums2[:-drop_num])
        elif list1_median > list2_median:
            left = int(index1)
            right = int(len(nums2) - index2 - 1)
            drop_num = min(left, right)

            return self.findMedianSortedArrays(nums1[:-drop_num], nums2[drop_num:])
        else:
            return list1_median


sol = Solution()
l1 = [1, 5, 6]
l2 = [2, 3, 4, 7, 8]
print(sol.findMedianSortedArrays(l1, l2))
