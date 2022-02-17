#
# @lc app=leetcode.cn id=703 lang=python3
#
# [703] 数据流中的第K大元素
#
from typing import List
# @lc code=start
import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.full = True
        self.heap = []
        if not nums:
            self.full = False
            return
        if k > len(nums):
            self.full = False
        for i in range(min(k, len(nums))):
            heapq.heappush(self.heap, nums[i])
        for i in range(k, len(nums)):
            if nums[i] > self.heap[0]:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, nums[i])

    def add(self, val: int) -> int:
        if self.full:
            if val > self.heap[0]:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, val)
        else:
            heapq.heappush(self.heap, val)
            self.full = True
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end

