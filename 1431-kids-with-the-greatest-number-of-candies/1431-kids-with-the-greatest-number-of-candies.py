class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        hig=0
        res=[False]*len(candies)
        # hig=max(candies)
        for i in candies:
            if i>hig:
                hig=i
        for i in range(len(candies)):
            if candies[i]+extraCandies>=hig:
                res[i]=True
        return res