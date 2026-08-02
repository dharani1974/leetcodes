class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        seen=[]
        dseen=set()
        for c in arr:
            if c not in dseen:
                if c not in seen:
                    seen.append(c)
                else:
                    dseen.add(c)
                    seen.remove(c)
        res=list(seen)
        if len(res)>k-1:
            return res[k-1]
        return ""