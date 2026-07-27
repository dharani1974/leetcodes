class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        num1=set(nums1)
        num2=set(nums2)
        res=[[],[]]
        res1=[]
        res2=[]
        for i in num1:
            if i not in num2:
                res1.append(i)
        for i in num2:
            if i not in num1:
                res2.append(i)
        res[0]=res1
        res[1]=res2
        return res