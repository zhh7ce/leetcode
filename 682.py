#
# @lc app=leetcode.cn id=682 lang=python3
#
# [682] 棒球比赛
#

# @lc code=start
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for i in ops:
            if i == '+':
                stack.append(stack[-1] + stack[-2])
                continue
            if i == 'C':
                stack.pop()
                continue
            if i == 'D':
                stack.append(2 * stack[-1])
                continue
            stack.append(int(i))
        return sum(stack)
# @lc code=end

