# https://leetcode.com/problems/stamping-the-sequence/


class Solution:
    def movesToStamp(self, stamp: str, target: str):
        combinations = set()
        target_len = len(target)
        stamp_len = len(stamp)

        for i in range(stamp_len):
            for j in range(stamp_len - i):
                combinations.add("#"*i + stamp[i:stamp_len-j] + "#"*j)

        last_target = "#" * target_len
        seq = []
        
        while target != last_target:
            updated = False
            for i in range(target_len - stamp_len + 1):
                if target[i:i+stamp_len] in combinations:
                    target = target[:i] + "#"*stamp_len + target[i+stamp_len:]
                    updated = True
                    seq.append(i)
            if not updated:
                return []

        return seq[::-1]

stamp = "abca"
target = "aabcaca"
sol = Solution()
result = sol.movesToStamp(stamp, target)
print(result)
