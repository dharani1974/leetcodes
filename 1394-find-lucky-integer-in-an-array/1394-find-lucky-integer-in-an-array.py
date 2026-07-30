class Solution:
    def findLucky(self, arr: List[int]) -> int:
        seen={}
        res=-1
        for i in arr:
            if i in seen:
                seen[i]+=1
            else:
                seen[i]=1
        for key,values in seen.items():
            if key==values and res<key:
                res=key
        return res