#
# @lc app=leetcode.cn id=441 lang=python3
#
# [441] 排列硬币
#

# @lc code=start
import math
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return math.floor((math.sqrt(1+n*8)-1)/2)
# @lc code=end

