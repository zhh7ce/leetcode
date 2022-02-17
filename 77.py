#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#
from typing import List
# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        stack = []
        for i in range(n):
            stack.append([i+1])
        answer = []
        while stack:
            s = stack.pop()
            if len(s) == k:
                answer.append(s)
                continue
            value = s[-1]
            for i in range(value, n):
                tmp = s.copy()
                tmp.append(i+1)
                stack.append(tmp)
        return answer

# @lc code=end

s = Solution()
print(s.combine(1,0))