#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#
from typing import List
# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount + 1)
        coins.sort()
        for i in range(1, amount+1):
            tmp = float('inf')
            for j in coins:
                if j > i:
                    break
                tmp = min(tmp, dp[i-j])
            dp[i] = tmp + 1
        if dp[-1] == float('inf'):
            return -1
        return dp[-1]
# @lc code=end

sol = Solution()
print(sol.coinChange([474,83,404,3], 264))

