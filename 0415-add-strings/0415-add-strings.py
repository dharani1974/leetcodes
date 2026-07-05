class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if num1=="0":
            return num2
        if num2=="0":
            return num1
        n1=len(num1)-1
        n2=len(num2)-1
        dig="0123456789"
        carry=0
        res=[]
        while 0<=n1 or 0<=n2 or 1<=carry:
            val1=dig.index(num1[n1])if n1>=0 else 0
            val2=dig.index(num2[n2])if n2>=0 else 0
            add=val1+val2+carry
            carry=add//10
            res.append(dig[add%10])
            n1-=1
            n2-=1
        return "".join(res[::-1])