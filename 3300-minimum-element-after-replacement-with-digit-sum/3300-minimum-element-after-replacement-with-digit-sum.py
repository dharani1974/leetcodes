class Solution:
    def minElement(self, nums: List[int]) -> int:
        for i in range(0,len(nums)):
            if nums[i]>9:
                st=str(nums[i])
                temp=0
                for j in range (0,len(st)):
                    temp+=int(st[j])
                nums[i]=temp
        return(min(nums))
