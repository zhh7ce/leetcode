#
# @lc app=leetcode.cn id=1046 lang=python3
#
# [1046] 最后一块石头的重量
#

# @lc code=start
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        q = []
        for i in stones:
            heapq.heappush(q, -i)
        while q and len(q) != 1:
            x = -heapq.heappop(q)
            y = -heapq.heappop(q)
            if x != y:
                heapq.heappush(q, -abs(x-y))
        if not q:
            return 0
        else:
            return -q[0]
# @lc code=end

