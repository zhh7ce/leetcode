/*
 * @lc app=leetcode.cn id=416 lang=cpp
 *
 * [416] 分割等和子集
 */

// @lc code=start
class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int n = nums.size();
        int sum = 0;
        for (int i = 0; i < n; ++i) {
            sum += nums[i];
        }
        if (sum & 1) {
            return false;
        }
        sum /= 2;
        int dp[sum];
        for (int size = sum; size > 0; --size) {
            if (size >= nums[0]) {
                dp[size-1] = nums[0];
            } else {
                dp[size-1] = 0;
            }
        }
        for (int item = 1; item < n; ++item) {
            for (int size = sum; size > 0; --size) {
                if (size > nums[item]) {
                    dp[size-1] = max(nums[item]+dp[size-nums[item]-1], dp[size-1]);
                }
            }
        }
        return (dp[sum-1] == sum);
    }
};
// @lc code=end

