# https://leetcode.com/problems/minimum-window-subsequence/
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_length = len(s)
        t_length = len(t)
        
        if t_length > s_length:
            return ""
        elif t_length > s_length:
            return "" if s != t else s

        min_window_dp = [[-1]*(t_length + 1) for _ in range(s_length + 1)]
        for i in range(s_length+1):
            min_window_dp[i][0] = i
        
        shortest_subsequence = ""
        shortest_length = s_length
        for i in range(s_length):
            min_length = min(t_length, i+1)
            for j in range(min_length):
                min_window_dp[i+1][j+1] = min_window_dp[i][j] if s[i] == t[j] else min_window_dp[i][j+1]
            if min_window_dp[i+1][-1] != -1 and shortest_length > i - min_window_dp[i+1][-1]:
                shortest_subsequence = s[min_window_dp[i+1][-1]:i+1]
                shortest_length = i - min_window_dp[i+1][-1]
                
        return shortest_subsequence
