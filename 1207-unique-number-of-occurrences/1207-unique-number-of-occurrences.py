class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        seen={}
        for i in arr:
            if i in seen:
                seen[i]+=1
            else:
                seen[i]=1
        res1=len(seen)
        res2=len(set(seen.values()))
        return res1==res2