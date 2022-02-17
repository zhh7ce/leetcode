#
# @lc app=leetcode.cn id=566 lang=python3
#
# [566] 重塑矩阵
#

# @lc code=start
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(nums)
        n = len(nums[0])
        if m*n == r*c:
            ans = []
            x = 0
            y = 0
            for i in range(r):
                row = [0] * c
                for j in range(c):
                    row[j] = (nums[x][y])
                    y += 1
                    if y == n:
                        x += 1
                        y = 0
                ans.append(row)
            return ans
        else:
            return nums
# @lc code=end

