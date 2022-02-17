#
# @lc app=leetcode.cn id=874 lang=python3
#
# [874] 模拟行走机器人
#
from typing import List
# @lc code=start
import numpy as np
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        r = np.asarray([0, 0])
        d = np.asarray([0, 1])
        left = np.asarray([[0, -1], [1, 0]])
        right = np.asarray([[0, 1], [-1, 0]])
        maximum = 0
        obs = set()
        for i in obstacles:
            obs.add((i[0], i[1]))
        for i in commands:
            if i == -2:
                d = np.dot(left, d)
            elif i == -1:
                d = np.dot(right, d)
            else:
                for j in range(i):
                    r += d
                    if (r[0], r[1]) in obs:
                        r -= d
                        break
                maximum = max(maximum, np.dot(r, r.T))
        return maximum
# @lc code=end
commands = [4,-1,4,-2,4]
obstacles = [[2,4]]
s = Solution()
print(s.robotSim(commands, obstacles))