#
# @lc app=leetcode.cn id=241 lang=python3
#
# [241] 为运算表达式设计优先级
#
from typing import List
# @lc code=start
class Solution:
    import operator
    ops = { "+": operator.add, "-": operator.sub, '*': operator.mul}

    def diffWaysToCompute(self, input: str) -> List[int]:
        number = []
        operator = []
        prev = False # false means prev is an operator
        for i in input:
            if i == '+' or i == '-' or i == '*':
                operator.append(i)
                prev = False
            elif prev:
                number[-1] = number[-1] * 10 + int(i)
            else:
                number.append(int(i))
                prev = True
        # print(number, operator)
        self.number = number
        self.operator = operator
        return self.recursion(0, len(self.operator))

    def recursion(self, start, end) -> List[int]:
        # print(start, end)
        if start == end:
            return [self.number[start]]
        array = []
        for i in range(start, end):
            left = self.recursion(start, i)
            right = self.recursion(i+1, end)
            for j in left:
                for k in right:
                    array.append(self.ops[self.operator[i]](j, k))
        return array

# @lc code=end

s = Solution()
print(s.diffWaysToCompute("1+1"))