#
# @lc app=leetcode.cn id=406 lang=python3
#
# [406] 根据身高重建队列
#
from typing import List
# @lc code=start
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        n = len(people)
        answer = []
        for i in range(n):
            for j in range(1, n-i):
                if people[j-1][0] < people[j][0]:
                    tmp = people[j-1]
                    people[j-1] = people[j]
                    people[j] = tmp
                elif people[j-1][0] == people[j][0] and people[j-1][1] > people[j][1]:
                    tmp = people[j-1]
                    people[j-1] = people[j]
                    people[j] = tmp
        for i in people:
            index = i[1]
            answer.insert(index, i)
        return answer
# @lc code=end
people = [[9,0],[7,0],[1,9],[3,0],[2,7],[5,3],[6,0],[3,4],[6,2],[5,2]]
s = Solution()
print(s.reconstructQueue(people))
