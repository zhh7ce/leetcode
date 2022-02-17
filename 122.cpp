/*
 * @lc app=leetcode.cn id=122 lang=cpp
 *
 * [122] 买卖股票的最佳时机 II
 */

// @lc code=start
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int ans = 0;
        int minPrice = prices[0];
        for (int day = 1; day < prices.size(); ++day) {
            if (prices[day] <= minPrice) {
                minPrice = prices[day];
            } else {
                ans += prices[day] - minPrice;
                minPrice = prices[day];
            }
        }
        return ans;
    }
};
// @lc code=end

