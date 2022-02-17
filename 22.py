#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
from typing import List
# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if not n:
            return []
        blankets = ['(']
        lefts = [1]
        rights = [0]
        answer = []
        while blankets:
            blanket = blankets.pop()
            left = lefts.pop()
            right = rights.pop()
            if left < n:
                tmp = blanket + '('
                blankets.append(tmp)
                lefts.append(left+1)
                rights.append(right)
            if right < left:
                tmp = blanket + ')'
                blankets.append(tmp)
                lefts.append(left)
                rights.append(right+1)
            if left == n and right == n:
                answer.append(blanket)
        return answer
# @lc code=end

s = Solution()
print(s.generateParenthesis(0))
