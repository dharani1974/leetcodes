class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        store={}
        for i in nums2:
            while stack and stack[-1]<i:
                cur=stack.pop()
                store[cur]=i
            stack.append(i)
        res=[]
        for i in nums1:
            if i in store:
                res.append(store[i])
            else:
                res.append(-1)
        return res