#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel表列序号
#

# @lc code=start
class Solution:
    def titleToNumber(self, s: str) -> int:
        if not s:
            return 0
        ans = 0
        for i in s:
            ans  *= 26
            ans += ord(i) - 64
        return ans
# @lc code=end

