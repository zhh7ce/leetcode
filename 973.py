#
# @lc app=leetcode.cn id=973 lang=python3
#
# [973] 最接近原点的 K 个点
#
from typing import List
# @lc code=start
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        n = len(points)
        dis = [0] * n
        for i in range(n):
            for j in points[i]:
                dis[i] += j * j
        nums = [0] * n
        for i in range(n):
            nums[i] = i
        answer = [0] * K
        count = 0
        while count < K:
            left = []
            right = []
            pivot = nums[0]
            for i in nums[1:]:
                if dis[i] < dis[pivot]:
                    left.append(i)
                else:
                    right.append(i)
            if len(left)+1 <= K-count:
                for i in left:
                    answer[count] = i
                    count += 1
                answer[count] = pivot
                count += 1
                nums = right
            elif len(left) <= K-count:
                for i in left:
                    answer[count] = i
                    count += 1
                nums = right
            else:
                nums = left
        res = []
        for i in answer:
            res.append(points[i])
        return res
# @lc code=end
points = [[1,3],[-2,2]]
s = Solution()
print(s.kClosest(points, 2))