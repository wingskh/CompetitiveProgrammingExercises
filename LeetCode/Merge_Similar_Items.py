# 6141. Merge Similar Items
# https://leetcode.com/contest/biweekly-contest-84/problems/merge-similar-items/
class Solution:
    def mergeSimilarItems(self, items1, items2):
        count_dict = {}
        for item1 in items1:
            if item1[0] not in count_dict:
                count_dict[item1[0]] = 0
            count_dict[item1[0]] += item1[1]

        for item2 in items2:
            if item2[0] not in count_dict:
                count_dict[item2[0]] = 0
            count_dict[item2[0]] += item2[1]

        return list(map(list, sorted(list(count_dict.items()), key = lambda x:x[0])))

items1 = [[1,1],[4,5],[3,8]]
items2 = [[3,1],[1,5]]
sol = Solution()
print(sol.mergeSimilarItems(items1,items2))
