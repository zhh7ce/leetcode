#
# @lc app=leetcode.cn id=1423 lang=python3
#
# [1423] 可获得的最大点数
#

# @lc code=start
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        left = 0
        right = n-k
        s = sum(cardPoints[left:right])
        minCount = s
        while right < n:
            s += cardPoints[right]
            s -= cardPoints[left]
            minCount = min(minCount, s)
            left += 1
            right += 1
        return sum(cardPoints) - minCount
# @lc code=end

