class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        count=0
        for i in range (0,len(nums)-1):
            for j in range (i+1,len(nums)):
                gcd=1
                f=nums[i]
                while f>=10:
                    f//=10
                l=nums[j]%10
                r=min(f,l)
                x=1
                while x <=r:
                    if f%x==0 and l%x==0:
                        gcd=x
                    x+=1
                if gcd==1:
                    count+=1
        return count