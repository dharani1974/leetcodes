class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen={}
        single=0
        count=0
        for i in range (0,len(s)):
            if s[i] in seen:
                seen[s[i]]+=1
            else:
                seen[s[i]]=1
        for key in seen:
            if seen[key]%2==0:
                count+=seen[key]
            elif seen[key]>1 :
                count+=seen[key]-1
                single=1
            else:
                    single=1
        return count+single 