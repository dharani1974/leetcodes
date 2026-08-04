class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        seen=set()
        res=0
        for i in nums:
                seen.add(i)
                if ((-1)*i) in seen:
                    res=max(abs(i),res)
        if res!=0:
            return res
        return -1