class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        esum=0
        dsum=0
        for i in nums:
            esum+=i
            while i>0:
                dig=i%10
                i=i//10
                dsum+=dig
        return esum-dsum