#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#
from typing import List
# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        for i in range(n):
            gas[i] -= cost[i]
        for i in range(1, n):
            gas[i] += gas[i-1]
        if gas[-1] < 0:
            return -1
        return (gas.index(min(gas)) + 1) % n

# @lc code=end
gas  = [3,3,4]
cost = [3,4,4]
s = Solution()
print(s.canCompleteCircuit(gas, cost))