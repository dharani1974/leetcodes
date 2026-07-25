class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftsum=0
        rightsum=sum(nums[1:])
        res=[0]*len (nums)
        for num in range (0,len(nums)):
            res[num]=abs(leftsum-rightsum)
            leftsum+=nums[num]
            if num <len(nums)-1:
                rightsum-=nums[num+1]
        return(res)