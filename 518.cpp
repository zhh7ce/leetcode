/*
 * @lc app=leetcode.cn id=518 lang=cpp
 *
 * [518] 零钱兑换 II
 */

// @lc code=start
class Solution {
public:
    int change(int amount, vector<int>& coins) {
        if (amount == 0){
            return 1;
        }
        if (coins.size() == 0) {
            return 0;
        }
        int n = coins.size();
        int dp[amount+1];
        dp[0] = 0;
        for (int size = 0; size <= amount; ++size) {
            if (size < coins[0]) {
                dp[size] = 0;
            } else if (size == coins[0]) {
                dp[size] = 1;
            } else {
                if (dp[size-coins[0]] > 0) {
                    dp[size] = dp[size-coins[0]];
                } else {
                    dp[size] = 0;
                }
            }
        }
        for (int item = 1; item < n; ++item) {
            for (int size = 0; size <= amount; ++size) {
                if (size == coins[item]) {
                    ++dp[size];
                } else if (size > coins[item]) {
                    if (dp[size-coins[item]] > 0) {
                        dp[size] += dp[size-coins[item]];
                    }
                }
            }
        }
        return dp[amount];
    }
};
// @lc code=end

