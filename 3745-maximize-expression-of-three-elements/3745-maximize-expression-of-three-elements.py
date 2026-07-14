class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        min1=float("inf")
        max1=float("-inf")
        max2=float("-inf")
        for i in nums:
            min1=min(min1,i)
            if i>=max1:
                max2=max1
                max1=i
            elif i>max2 :
                max2=i
        return (max1+max2-min1)