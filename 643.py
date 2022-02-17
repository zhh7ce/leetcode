#
# @lc app=leetcode.cn id=643 lang=python3
#
# [643] 子数组最大平均数 I
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = sum(nums[:k])
        ans = s
        left = 0
        right = k
        n = len(nums)
        while right < n:
            s += nums[right]
            s -= nums[left]
            ans = max(ans, s)
            right += 1
            left += 1
        return ans/k
# @lc code=end

