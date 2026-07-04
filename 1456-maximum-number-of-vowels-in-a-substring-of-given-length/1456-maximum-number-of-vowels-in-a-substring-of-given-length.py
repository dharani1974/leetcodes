class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        x=set("aeiou")
        curv=0
        for char in range (k):
            if s[char]in x:
                curv+=1
        maxv=curv
        if maxv == k:
            return k
        for char in range (k,len(s)):
            if s[char] in x:
                curv+=1
            if s[char-k]in x:
                curv-=1
            maxv=max(curv,maxv)
        return maxv
        

