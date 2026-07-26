class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        maxsum=0
        cursum=0
        left=0
        seen=set()
        for num in range (0,len(nums)):
            while nums[num] in seen:
                seen.remove(nums[left])
                cursum-=nums[left]
                left+=1
            seen.add(nums[num])
            cursum+=nums[num]
            maxsum=max(maxsum,cursum)
        return maxsum