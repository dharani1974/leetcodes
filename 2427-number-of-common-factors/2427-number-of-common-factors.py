class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        n=min(a,b)
        count=1
        for i in range(2,n+1):
            if a%i==0 and b%i==0:
                count+=1
        return count
        # gcd=1
        # for i in range (n,1,-1):
        #     if a%i==0 and b%i==0:
        #         gcd=i
        #         break
        # for i in range(2,gcd+1):
        #     if gcd%i==0:
        #         count+=1
        # return count
