class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        seen={}
        res=0
        for i in range(0,len(nums)):
            if nums[i] not in seen:
                seen[nums[i]]=1
            else:
                res+=seen[nums[i]]
                seen[nums[i]]+=1
        return res