class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        arr=set(nums)
        res=[]
        for i in range (1,len(nums)+1):
            if i not in arr:
                res.append(i)
        return res