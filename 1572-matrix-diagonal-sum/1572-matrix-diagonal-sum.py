class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res=0
        row=0
        l=0
        r=len(mat)-1
        while row < len(mat):
            if l==r:
                res+=mat[row][l]
            else:
                res+=mat[row][l]+mat[row][r]
            row+=1
            l+=1
            r-=1
        return res