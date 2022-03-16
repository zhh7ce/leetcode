/*
 * @lc app=leetcode.cn id=2044 lang=cpp
 *
 * [2044] 统计按位或能得到最大值的子集数目
 */
#include<vector>
using namespace std;

// @lc code=start
class Solution {
public:
    int countMaxOrSubsets(vector<int>& nums) {
        int n = nums.size();
        int target = 0;
        int res = 0;
        int mask = 1 << n;
        for (auto i: nums) {
            target |= i;
        }
        for (int i = 0; i < mask; i++) {
            int cur = 0;
            for (int j = 0; j < n; j++) {
                if ((i >> j) & 1) {
                    cur |= nums[j];
                }
            }
            if (cur == target) {
                res++;
            }
        }
        return res;

    }
};
// @lc code=end

