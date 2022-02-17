#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#

# @lc code=start
import math
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n + 1)
        length = int(math.sqrt(n)) + 1
        sq = [1] * length
        for i in range(1, length):
            sq[i] = sq[i-1] + 2 * i + 1
        for i in range(1, n+1):
            tmp = float('inf')
            for j in sq:
                if j > i:
                    break
                tmp = min(tmp, dp[i-j])
            dp[i] = tmp + 1
        return dp[-1]
    
# @lc code=end
sol = Solution()
print(sol.numSquares(9999))
