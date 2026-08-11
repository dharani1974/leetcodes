class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        seen={}
        res=[]
        num1=set(nums1)
        num2=set(nums2)
        num3=set(nums3)
        for i in num1:
                seen[i]=1
        for i in num2:
            if i in seen:
                seen[i]+=1
            else:
                seen[i]=1
        for i in num3:
            if i in seen:
                seen[i]+=1
            else:
                seen[i]=1
        for key ,values in seen.items():
            if values>=2:
                res.append(key)
        return res