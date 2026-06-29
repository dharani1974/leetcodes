class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # i=0
        # while i<=len(letters)-1:
        #     if letters[i]<=target:
        #         if i<len(letters)-1:
        #             i+=1
        #         else:
        #             return letters[0]
        #     else:
        #         return letters[i]  
        l=0
        r=len(letters)-1
        while l<=r:
            mid=(l+r)//2
            if letters[mid]<=target:
                l=mid+1
            else:
                r=mid-1
        if l==len(letters):
            return letters[0]
        return letters[l]