class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        seen={}
        res=0
        for char in stones:
            if char in seen:
                seen[char]+=1
            else:
                seen[char]=1
        for i in jewels:
            if i in seen:
                res+=seen[i]
        return res