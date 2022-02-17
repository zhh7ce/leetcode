#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#
from typing import List
# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        array = [[]]
        sums = [0]
        answer = []
        while array:
            tmp = array.pop()
            s = sums.pop()
            if s == target:
                answer.append(tmp)
                continue
            if tmp:
                value = tmp[-1]
            else:
                value = 0
            # it may be duplicated, but if we sort the answer
            # we can get all non-decrease solutions
            for i in candidates:
                if s + i > target:
                    break
                if i < value:
                    continue
                t = tmp.copy()
                t.append(i)
                array.append(t)
                sums.append(s+i)
        return answer

# @lc code=end
candidates = [2,3,6,7]
target = 7
s = Solution()
print(s.combinationSum(candidates, 0))
