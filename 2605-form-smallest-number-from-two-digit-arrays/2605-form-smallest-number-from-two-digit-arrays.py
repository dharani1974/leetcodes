class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        seen={}
        common=[]
        for i in nums1:
            if i not in seen:
                seen[i]=1
            else:
                seen[i]+=1
        for j in nums2:
            if j not in seen:
                seen[j]=1
            else:
                seen[j]+=1
                if seen[j]==2:
                    common.append(j)
        if len(common) !=0:
            n0=9
            for x in common:
                if x<n0:
                    n0=x
            return n0
        n1=9
        n2=9
        i=0
        while i<len(nums1):
            if nums1[i]<n1:
                n1=nums1[i]
            i+=1
        j=0
        while j<len(nums2):
            if nums2[j]<n2:
                n2=nums2[j]
            j+=1
        if n1>n2:
            res=(n2*10)+n1
        else:
            res=(n1*10)+n2
        return res