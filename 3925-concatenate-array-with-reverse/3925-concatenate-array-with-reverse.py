class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        res=[0]*(len(nums)*2)
        for i in range (0,len(nums)):
            res[i]=nums[i]
            res[-i-1]=nums[i]
        return res