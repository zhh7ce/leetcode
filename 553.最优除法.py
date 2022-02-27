#
# @lc app=leetcode.cn id=553 lang=python3
#
# [553] 最优除法
#

# @lc code=start
class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        n = len(nums)
        s = [str(_) for _ in nums]
        if n < 3:
            return '/'.join(s)
        return s[0] + '/' + '(' + '/'.join(s[1:]) + ')'
# @lc code=end

