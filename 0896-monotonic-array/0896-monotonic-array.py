class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums)<=2:
            return True
        if nums[0]==nums[-1]:
            direction=0
        elif nums[0]<nums[-1]:
            direction=1
        else:
            direction=-1
        for i in range(1,len(nums)):
            if direction==1:
                if nums[i-1]>nums[i]:
                    return False
            elif direction==-1:
                if nums[i-1]<nums[i]:
                    return False
            else:
                if nums[i-1]!=nums[i]:
                    return False
        return True
