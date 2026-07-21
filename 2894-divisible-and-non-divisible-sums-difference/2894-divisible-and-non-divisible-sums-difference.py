class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        res=0
        i=1
        while i<=n:
            if i%m==0:
                res-=i
            else:
                res+=i
            i+=1
        return res