class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        right=len(nums)-1
        left=0
        res=[0]*len(nums)
        pos=len(nums)-1
        for i in range (len(nums)):
            if abs(nums[left])<=abs(nums[right]):
                res[pos]=(nums[right])**2
                right-=1
                pos-=1
            else:
                res[pos]=(nums[left])**2
                left+=1
                pos-=1
        return res