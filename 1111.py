#
# @lc app=leetcode.cn id=1111 lang=python3
#
# [1111] 有效括号的嵌套深度
#
from typing import List
# @lc code=start
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        n = len(seq)
        answer = [0] * n
        stack = []
        for i in range(n):
            if seq[i] == '(':
                if not stack: # empty
                    answer[i] = 0
                    stack.append(0)
                else:
                    answer[i] = 1-stack[-1]
                    stack.append(1-stack[-1])
            else:
                answer[i] = stack.pop()
        return answer

# @lc code=end

s = Solution()
print(s.maxDepthAfterSplit("()(())()"))
