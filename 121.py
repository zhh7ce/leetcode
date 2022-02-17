#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#
from typing import List
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        profit = 0
        minPrice = prices[0]
        for i in prices:
            if i < minPrice:
                minPrice = i
            elif profit < i - minPrice:
                profit = i - minPrice
        return profit
# @lc code=end

n = [10]
sol = Solution()
print(sol.maxProfit(n))