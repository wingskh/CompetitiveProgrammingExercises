# https://leetcode.com/problems/partition-labels/
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        s_len = len(s)
        last_occurence_map = {s[i]: i for i in range(s_len)}
        i = 0
        size_of_partitions = []
        while i < s_len:
            last_index = last_occurence_map[s[i]]
            j = i + 1
            while j < last_index:
                last_index = max(last_occurence_map[s[j]], last_index)
                j += 1

            size_of_partitions.append(last_index - i + 1)
            i = last_index + 1

        return size_of_partitions


s = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
s = "qiejxqfnqceocmy"
len(s)
# Output: [13, 1, 1]
s = "mlullbhiuiujgvwvurcdvhzdk"
# Output: [1, 23, 1]
sol = Solution()
print(sol.partitionLabels(s))


