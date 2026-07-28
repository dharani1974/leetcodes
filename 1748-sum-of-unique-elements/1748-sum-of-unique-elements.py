class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        seen={}
        res=0
        for i in nums:
            if i in seen:
                seen[i]+=1
            else:
                seen[i]=1
        for key,value in seen.items():
            if value==1:
                res+=key
        return res