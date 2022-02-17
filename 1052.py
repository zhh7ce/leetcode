#
# @lc app=leetcode.cn id=1052 lang=python3
#
# [1052] 爱生气的书店老板
#

# @lc code=start
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        basic = 0
        for (c, g) in zip(customers, grumpy):
            if not g:
                basic += c
        left = 0
        right = X
        extra = 0
        for (c, g) in zip(customers[:right], grumpy[:right]):
            if g:
                extra += c
        maxCount = extra
        while right < len(customers):
            if grumpy[left]:
                extra -= customers[left]
            if grumpy[right]:
                extra += customers[right]
            maxCount = max(maxCount, extra)
            left += 1
            right += 1
        return basic + maxCount


# @lc code=end

