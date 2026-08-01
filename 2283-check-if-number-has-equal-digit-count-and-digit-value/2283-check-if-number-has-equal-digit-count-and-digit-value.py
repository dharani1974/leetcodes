class Solution:
    def digitCount(self, num: str) -> bool:
        res=[0]*len(num)
        for i in num:
            a=int(i)
            if a <len(num):
                res[a]+=1
        seen=("".join(str(char) for char in res ))
        return seen== num