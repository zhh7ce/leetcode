#
# @lc app=leetcode.cn id=1658 lang=python3
#
# [1658] 将 x 减到 0 的最小操作数
#

# @lc code=start
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        if target < 0:
            return -1
        left = 0
        right = 0
        s = 0
        maxCount = -1
        nums.append(0)
        n = len(nums)
        while right < n:
            if s == target:
                maxCount = max(maxCount, right-left)
                s += nums[right]
                right += 1
            elif s < target:
                s += nums[right]
                right += 1
            else:
                s -= nums[left]
                left += 1
        if maxCount < 0:
            return -1
        else:
            return n - maxCount - 1
# @lc code=end

