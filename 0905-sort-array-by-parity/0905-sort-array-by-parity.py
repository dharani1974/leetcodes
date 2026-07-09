class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        pos=0
        even=len(nums)-1
        while pos<=even:
            if (nums[pos]%2)>(nums[even]%2):
                nums[pos],nums[even]=nums[even],nums[pos]
            if (nums[pos]%2==0):
                pos+=1
            if(nums[even]%2==1):
                even-=1
        return nums