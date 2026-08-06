class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        seen={}
        a=97
        res=[]
        for i in key:
            if i !=" "and i not in seen:
                seen[i]=chr(a)
                a+=1
        for i in message:
            if i==" ":
                res.append(" ")
            else:
                res.append(seen[i])
        return "".join(res)