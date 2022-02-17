#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#
from typing import List
# @lc code=start
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        while True:
            bigger = []
            smaller = []
            for i in range(1, len(nums)):
                if nums[i] >= nums[0]:
                    bigger.append(nums[i])
                else:
                    smaller.append(nums[i])
            if len(bigger) >= k:
                nums = bigger
            elif len(bigger) == k-1:
                return nums[0]
            else:
                k -= len(bigger) + 1
                nums = smaller
# @lc code=end
nums = [3,2,1,5,6,4]
s = Solution()
print(s.findKthLargest(nums, 2))
