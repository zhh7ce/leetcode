#
# @lc app=leetcode.cn id=1232 lang=python3
#
# [1232] 缀点成线
#

# @lc code=start
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        vectors = []
        [x, y] = coordinates[0]
        for [a, b] in coordinates:
            vectors.append([x-a, y-b])
        u = [0, 0]
        for v in vectors:
            if u[0] * v[1] - u[1] * v[0] != 0:
                return False
            u = v
        return True
# @lc code=end

