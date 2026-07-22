class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen=[]
        duplicat=[]
        for c in s:
            if c not in duplicat:
                if c not in seen:
                    seen.append(c)
                else:
                    seen.remove(c)
                    duplicat.append(c)
        if len(seen)>0:
            return s.index(seen[0])
        return -1