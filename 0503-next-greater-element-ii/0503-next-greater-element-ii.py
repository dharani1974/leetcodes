class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        res=[-1]*len(nums)
        num=nums+nums
        for i in range(0,len(num)):
            while stack and num[stack[-1]]<num[i]:
                pre=stack.pop()
                res[pre]=num[i]
            if i<len(res):
                stack.append(i)
        return res
