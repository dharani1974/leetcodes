class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        seen={}
        res=[]
        for i in nums:
            for j in i:
                if j in seen:
                    seen[j]+=1
                else:
                    seen[j]=1
        for key,values in seen.items():
            if values==len(nums):
                res.append(key)
        return sorted(res)