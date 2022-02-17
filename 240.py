#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#

# @lc code=start
import numpy as np
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        matrix = np.array(matrix)
        if self.recursion(matrix, target):
            return True
        return False

    def recursion(self, matrix, target):
        # print(matrix)
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        if target < matrix[0][0] or matrix[-1][-1] < target:
            return False
        if len(matrix) == 1:
            for i in matrix[0]:
                if i == target:
                    return True
            return False
        if len(matrix[0]) == 1:
            for i in matrix:
                if i[0] == target:
                    return True
            return False
        m = len(matrix)
        n = len(matrix[0])
        start = -1
        end = max(m, n)
        mid = (start + end) // 2
        while start < end-1:
            # print(mid)
            if mid >= min(m, n):
                value = float('inf')
            else:
                value = matrix[mid][mid]
            if target == value:
                return True
            elif target < value:
                end = mid
            else:
                start = mid
            mid = (start + end) // 2
        # print(start, mid, end)
        # print(matrix[end:, :end])
        # print(matrix[:end, end:])
        if self.recursion(matrix[end:, :end], target) or self.recursion(matrix[:end, end:], target):
            return True
        return False
        
        
# @lc code=end
matrix = [[4,5,10,15,19,20,20],[4,9,12,15,22,23,26],[7,11,12,20,25,27,27],[10,14,17,23,27,30,32],[11,18,19,24,28,34,39]]
s = Solution()
print(s.searchMatrix(matrix, 25))