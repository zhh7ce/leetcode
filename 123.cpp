/*
 * @lc app=leetcode.cn id=123 lang=cpp
 *
 * [123] 买卖股票的最佳时机 III
 */

// @lc code=start
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        int minPrice = prices[0];
        int front[n];
        front[0] = 0;
        for (int day = 1; day < n; ++day) {
            minPrice = min(minPrice, prices[day]);
            front[day] = max(front[day-1], prices[day]-minPrice);
        }
        int maxPrice = prices[n-1];
        int back[n];
        back[n-1] = 0;
        for (int day = n-2; day >= 0; --day) {
            maxPrice = max(maxPrice, prices[day]);
            back[day] = max(back[day+1], maxPrice-prices[day]);
        }
        int ans = 0;
        for (int day = 0; day < n; ++day) {
            ans = max(ans, front[day]+back[day]);
        }
        return ans;
    }
};
// @lc code=end

