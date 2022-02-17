#
# @lc app=leetcode.cn id=376 lang=python3
#
# [376] 摆动序列
#
from typing import List
# @lc code=start
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = 1
        start = n
        for i in range(1, n):
            if nums[i] != nums[0]:
                dp = 2
                bigger = (nums[i] > nums[0])
                start = i+1
                break
        for i in range(start, n):
            if (nums[i] != nums[i-1]) and (bigger != (nums[i] > nums[i-1])):
                dp += 1
                bigger = not bigger
        return dp


# @lc code=end
nums = [1,1,7,4,9,2,5]
s = Solution()
print(s.wiggleMaxLength(nums))
