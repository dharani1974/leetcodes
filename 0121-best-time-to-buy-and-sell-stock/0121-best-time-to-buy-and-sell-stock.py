class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min1=prices[0]
        max1=0
        curmax=0
        for i in range (1,len(prices)):
            if min1>prices[i]:
                min1=prices[i]
                
            else:
                curmax=prices[i]-min1
                max1=max(max1,curmax)
        return max1