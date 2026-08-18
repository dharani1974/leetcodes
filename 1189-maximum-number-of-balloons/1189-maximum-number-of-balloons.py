class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon={"b":1,"a":1,"l":2,"o":2,"n":1}
        seen={}
        res=[0]*len(balloon)
        for char in text:
            if char in balloon:
                if char in seen:
                    seen[char]+=1
                else:
                    seen[char]=1
        i=0
        for key,values in balloon.items():
            if key in seen and values<=seen[key]:
                res[i]=seen[key]//values
            i+=1
        return min(res)