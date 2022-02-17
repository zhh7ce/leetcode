#
# @lc app=leetcode.cn id=1282 lang=python3
#
# [1282] 用户分组
#
from typing import List
# @lc code=start
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        full = []
        dictory = dict()
        for i in range(len(groupSizes)):
            if groupSizes[i] in dictory:
                dictory[groupSizes[i]].append(i)
            else:
                dictory[groupSizes[i]] = [i]
            if groupSizes[i] == len(dictory[groupSizes[i]]):
                full.append(dictory[groupSizes[i]].copy())
                dictory[groupSizes[i]] = []
        return full
# @lc code=end
groupSizes = [2,1,3,3,3,2]
s = Solution()
print(s.groupThePeople(groupSizes))
