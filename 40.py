#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#
from typing import List
# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        array = [[]]
        sums = [0]
        starts = [0]
        answer = []
        n = len(candidates)
        while array:
            tmp = array.pop()
            s = sums.pop()
            start = starts.pop()
            if s == target:
                answer.append(tmp)
                continue
            # it may be duplicated, but if we sort the answer
            # we can get all non-decrease solutions
            # use prev to avoid the same number
            prev = -1
            for i in range(start, n):
                if s + candidates[i] > target:
                    break
                if prev == candidates[i]:
                    continue
                else:
                    prev = candidates[i]
                t = tmp.copy()
                t.append(candidates[i])
                array.append(t)
                sums.append(s+candidates[i])
                starts.append(i+1)
        return answer
# @lc code=end

candidates = [10,1,2,7,6,1,5]
target = 8
s = Solution()
print(s.combinationSum2(candidates, target))