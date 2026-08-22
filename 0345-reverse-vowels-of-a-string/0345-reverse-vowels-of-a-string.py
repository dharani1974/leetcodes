class Solution:
    def reverseVowels(self, s: str) -> str:
        seen=('a','A','e','E','i','I','o','O','u','U')
        s=list(s)
        l=0
        r=len(s)-1
        while l<=r:
            if s[l] in seen and s[r] in seen:
                s[l],s[r]=s[r],s[l]
                l+=1
                r-=1
            elif s[l] not in seen and s[r] in seen:
                l+=1
            elif s[r] not in seen and s[l] in seen:
                r-=1
            else:
                l+=1
                r-=1
        return "".join(s)
