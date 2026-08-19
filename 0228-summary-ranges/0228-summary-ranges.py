class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        res=[]
        start=nums[0]
        end=start
        for i  in range(1,len(nums)):
            if (nums[i-1]+1)!=nums[i]:
                end=nums[i-1]
                if start ==end:
                    res.append(str(start))
                else:
                    res.append(str(start)+"->"+str(end))
                start=nums[i]
        end=nums[-1]
        if start==end:
            res.append(str(start))
        else:
            res.append(str(start)+"->"+str(end))
        return res
        

