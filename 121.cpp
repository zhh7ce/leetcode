/*
 * @lc app=leetcode.cn id=121 lang=cpp
 *
 * [121] 买卖股票的最佳时机
 */

// @lc code=start
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        int minPrice = prices[0];
        int ans = 0;
        for (int day = 1; day < n; ++day) {
            minPrice = min(minPrice, prices[day]);
            ans = max(ans, prices[day]-minPrice);
        }
        return ans;
    }
};
// @lc code=end

