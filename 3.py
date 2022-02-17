#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        dp = [1] * n
        for i in range(1, n): # for every char
            for j in range(dp[i-1]): # test is same
                if s[i-1-j] == s[i]:
                    dp[i] += j # max len is to a prev same
                    break
            else:
                dp[i] += dp[i-1] # new char for subs
        return max(dp)
                
# @lc code=end

