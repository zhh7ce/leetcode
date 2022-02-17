#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长上升子序列
#
from typing import List
# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            maxPrev = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    maxPrev = max(maxPrev, dp[j])
            dp[i] = maxPrev + 1
        return max(dp)
        
# @lc code=end
nums = [10,9,2,5,3,7,101,18]
sol = Solution()
print(sol.lengthOfLIS(nums))
