#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        neg = False
        if dividend < 0:
            dividend = -dividend
            neg = not neg
        if divisor < 0:
            divisor = -divisor
            neg = not neg
        

# @lc code=end

