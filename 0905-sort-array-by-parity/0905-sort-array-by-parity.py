class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        pos=0
        even=len(nums)-1
        while pos<=even:
            if nums[pos]%2!=0:
                if nums[even]%2==0:
                    nums[pos],nums[even]=nums[even],nums[pos]
                    pos+=1
                    even-=1
                else:
                    even-=1
            else:
                pos+=1
        return nums