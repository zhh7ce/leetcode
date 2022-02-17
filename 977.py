#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#
from typing import List
# @lc code=start
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        length = len(A)
        start = 0
        end = length-1
        array = [0] * length
        for i in range(length):
            if abs(A[start]) > abs(A[end]):
                array[length-i-1] = A[start] * A[start]
                start += 1
            else:
                array[length-i-1] = A[end] * A[end]
                end -= 1
        return array

# @lc code=end

n = []
sol = Solution()
print(sol.sortedSquares(n))