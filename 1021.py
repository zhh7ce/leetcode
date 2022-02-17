#
# @lc app=leetcode.cn id=1021 lang=python3
#
# [1021] 删除最外层的括号
#

# @lc code=start
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        left = 0
        index = []
        n = len(S)
        for i in range(n):
            if left == 0:
                index.append(i)
            if S[i] == '(':
                left += 1
            else:
                left -= 1
        index.append(n)
        answer = ''
        m = len(index)
        for i in range(m-1):
            answer += S[index[i]+1:index[i+1]-1]
        return answer
# @lc code=end

s = Solution()
print(s.removeOuterParentheses("()()"))