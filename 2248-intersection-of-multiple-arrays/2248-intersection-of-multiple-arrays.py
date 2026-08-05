class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        if len(nums)==1:
            return sorted(nums[0])
        res=set()
        set1=set(nums[1])
        for i in range (len(nums[0])):
            if nums[0][i] in set1:
                res.add(nums[0][i]) 
        if len(nums)>2:
            i=2
            while i<len(nums):
                temp=set(nums[i])
                rescopy=res.copy()
                for x in res:
                    if x not in temp:
                        rescopy.remove(x)
                res=rescopy
                i+=1

                
        return sorted(list(res))
        