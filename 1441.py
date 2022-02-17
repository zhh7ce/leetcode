#
# @lc app=leetcode.cn id=1441 lang=python3
#
# [1441] 用栈操作构建数组
#

# @lc code=start
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        answer = []
        n = target[-1]
        i = 0
        for j in range(1, n+1):
            answer.append('Push')
            if j == target[i]:
                i += 1
            else:
                answer.append('Pop')
        return answer
# @lc code=end

