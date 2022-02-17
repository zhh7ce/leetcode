class Solution:
    def minDominoRotations(self, A, B) -> int:
        x = min(self.checkOne(A, B), self.checkOne(B, A))
        if x == float('inf'):
            return -1
        else:
            return x

    def checkOne(self, A, B):
        x = A[0]
        x_need = 0
        x_all = len(A)
        for i in range(1, len(A)):
            if x != A[i]:
                if x != B[i]:
                    break
                else:
                    x_need += 1
            elif A[i] == B[i]:
                x_all -= 1
        else:
            return min(x_need, x_all-x_need)
        return float('inf')
        

A=[2,1,2,4,2,2]
B=[5,2,6,2,3,2]


print(len(A))
sol = Solution()
print(sol.minDominoRotations(A, B))
