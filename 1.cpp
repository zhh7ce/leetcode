/*
 * @lc app=leetcode.cn id=1 lang=cpp
 *
 * [1] 两数之和
 */

// @lc code=start
#include <unordered_map>
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> umap;
        std::vector<int> ans;
        for (int i = 0; i < nums.size(); ++i) {
            if (umap.find(nums[i]) != umap.end()) {
                ans.push_back(umap[nums[i]]);
                ans.push_back(i);
                return ans;
            }
            umap[target - nums[i]] = i;
        }
        return ans;
    }
};
// @lc code=end

