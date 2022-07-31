# https://leetcode.com/problems/word-subsets/

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        words2_ch_counter = {}

        for word in words2:
            cur_ch_counter = {}
            for ch in word:
                if ch not in cur_ch_counter:
                    cur_ch_counter[ch] = 1
                    if ch not in words2_ch_counter:
                        words2_ch_counter[ch] = 1
                else:
                    cur_ch_counter[ch] += 1
                    words2_ch_counter[ch] = max(words2_ch_counter[ch], cur_ch_counter[ch])

        result = []
        for word in words1:
            selected = True
            cur_ch_counter = {}
            for ch in word:
                if ch not in cur_ch_counter:
                    cur_ch_counter[ch] = 1
                else:
                    cur_ch_counter[ch] += 1

            for ch in words2_ch_counter:
                if not(ch in cur_ch_counter and cur_ch_counter[ch] >= words2_ch_counter[ch]):
                    selected = False
                    break
            
            if selected:
                result.append(word)

        return result

words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["e","oo"]

sol = Solution()
print(sol.wordSubsets(words1, words2))
