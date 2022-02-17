#
# @lc app=leetcode.cn id=991 lang=python3
#
# [991] 坏了的计算器
#

# @lc code=start
import math
class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        count = 0
        while X != Y:
            if Y > X:
                if Y % 2:
                    Y += 1
                else:
                    Y //= 2
            else:
                return count + X - Y
            count += 1
        return count
# @lc code=end

s = Solution()
print(s.brokenCalc(3, 10))