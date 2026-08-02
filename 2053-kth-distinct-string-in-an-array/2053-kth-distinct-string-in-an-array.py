class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        seen={}
        for c in arr:
            if c in seen:
                seen[c]+=1
            else:
                seen[c]=1
        for c in arr:
            if seen[c]==1:
                k-=1
                if k==0:
                    return c
        return ""