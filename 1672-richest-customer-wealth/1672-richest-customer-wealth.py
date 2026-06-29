class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth=0
        for i in accounts:
            i=sum(i)
            if max_wealth<i:
                max_wealth=i
        return max_wealth