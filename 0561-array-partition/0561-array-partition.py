class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i=1
        res=0
        while i<len(nums):
            res+=nums[i-1]
            i+=2
        return res