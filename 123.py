#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        profit1 = 0
        profit2 = 0
        minPrice = prices[0]
        for i in prices:
            if i < minPrice:
                minPrice = i
            elif profit < i - minPrice:
                profit = i - minPrice
        return profit
# @lc code=end

