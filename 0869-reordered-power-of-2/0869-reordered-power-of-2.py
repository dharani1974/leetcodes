class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        a=str(n)
        l=len(a)
        ogseen={}
        for char in a:
            if char in ogseen:
                ogseen[char]+=1
            else:
                ogseen[char]=1
        for i in range(0,30):
            if len(str(2**i))==l:
                cur=str(2**i)
                seen=ogseen.copy()
                match=True
                for j in range (0,len(cur)):
                    if cur[j] in seen and seen[cur[j]]>0:
                        seen[cur[j]]-=1
                    else:
                        match=False
                        break
                if match:
                    return True
        return False