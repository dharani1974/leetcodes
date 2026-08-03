class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        res=0
        seen1={}
        seen2={}
        for c in words1:
            if c in seen1:
                seen1[c]+=1
            else:
                seen1[c]=1
        for c in words2 :
            if c in seen2:
                seen2[c]+=1
            else:
                seen2[c]=1
        for c in seen2:
            if seen2[c]==1 and c in seen1 and seen1[c]==1:
                res+=1
        return res