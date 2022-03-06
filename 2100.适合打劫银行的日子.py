#
# @lc app=leetcode.cn id=2100 lang=python3
#
# [2100] 适合打劫银行的日子
#

# @lc code=start
class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        if time == 0:
            return [_ for _ in range(n)]
        s = set()
        dp = 0
        res = []
        for i in range(1, n):
            if security[i-1] >= security[i]:
                dp += 1
            else:
                dp = 0
            if dp >= time:
                s.add(i)
        dp = 0
        for i in range(n-2, -1, -1):
            if security[i] <= security[i+1]:
                dp += 1
            else:
                dp = 0
            if dp >= time and i in s:
                res.append(i)
        return res

# @lc code=end

