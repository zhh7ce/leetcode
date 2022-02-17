/*
 * @lc app=leetcode.cn id=494 lang=cpp
 *
 * [494] 目标和
 */

// @lc code=start
class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int S) {
        int sum = 0;
        int number = nums.size();
        for (int i = 0; i < number; ++i) {
            sum += nums[i];
        }
        if (S > sum) {
            return 0;
        }
        sum -= S;
        if (sum & 1) {
            return 0;
        }
        sum /= 2;
        int dp[sum+1];
        for (int size = sum; size >= 0; --size) {
            dp[size] = 0;
        }
        if (nums[0] <= sum) {
            dp[nums[0]] = 1;
        }
        for (int item = 1; item < number; ++item) {
            for (int size = sum; size >= 0; --size) {
                if (size > nums[item]) {
                    dp[size] += dp[size - nums[item]];
                }else if (size == nums[item]) {
                    dp[size] += dp[size - nums[item]] + 1;
                }
            }
        }
        if (sum == 0) {
            return dp[sum] + 1;
        }
        return dp[sum];
    }
};
// @lc code=end

