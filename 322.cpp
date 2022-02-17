/*
 * @lc app=leetcode.cn id=322 lang=cpp
 *
 * [322] 零钱兑换
 */

// @lc code=start
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        int n = coins.size();
        int dp[amount+1];
        dp[0] = 0;
        for (int size = 1; size <= amount; ++size) {
            if (size < coins[0]) {
                dp[size] = -1;
            }else if (size == coins[0]) {
                dp[size] = 1;
            }else {
                if (dp[size-coins[0]] > 0) {
                    dp[size] = dp[size-coins[0]] + 1;
                } else {
                    dp[size] = -1;
                }
            }
        }
        for (int item = 1; item < n; ++item) {
            for (int size = 1; size <= amount; ++size) {
                if (size == coins[item]) {
                    dp[size] = 1;
                }else if (size > coins[item]) {
                    if (dp[size-coins[item]] > 0) {
                        if (dp[size] > 0) {
                            dp[size] = min(dp[size], dp[size-coins[item]] + 1);
                        } else {
                            dp[size] = dp[size-coins[item]] + 1;
                        }
                    }
                }
            }
        }
        return dp[amount];
    }
};
// @lc code=end

