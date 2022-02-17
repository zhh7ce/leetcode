#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#
from typing import List
# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                for j in range(i):
                    if nums[i-j-1] >= j+2:
                        break
                else:
                    return i == n-1
        return True

# @lc code=end

nums = [3,2,2,0,0]
s = Solution()
print(s.canJump(nums))
