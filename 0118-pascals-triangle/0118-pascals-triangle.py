class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[]
        for rowlen in range(numRows):
            row=[]
            for val in range (rowlen+1):
                if rowlen==0:
                    row.append(1)
                elif val==0 or val==rowlen:
                    row.append(1)
                else:
                    row.append(res[rowlen-1][val-1]+res[rowlen-1][val])
            res.append(row)
        return res