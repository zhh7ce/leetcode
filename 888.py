#
# @lc app=leetcode.cn id=888 lang=python3
#
# [888] 公平的糖果交换
#

# @lc code=start
class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        a = sum(A)
        b = sum(B)
        n = (a - b) // 2
        s = set()
        for i in B:
            s.add(i+n)
        for i in A:
            if i in s:
                return [i, i-n]

# @lc code=end

