class Solution:
    def modifyString(self, s: str) -> str:
        arr=list(s)
        if len(s)==1 and s=="?":
            return "a"
        a="a"
        b="b"
        c="c"
        for i in range(0,len(arr)):
            if arr[i]=="?":
                if i==0:
                    if a==arr[i+1]:
                        arr[i]=b
                    else:
                        arr[i]=a
                elif(i==len(arr)-1):
                    if a==arr[i-1]:
                        arr[i]=b
                    else:
                        arr[i]=a
                else:
                    if arr[i-1]!=a and arr[i+1]!=a:
                        arr[i]=a
                    elif arr[i-1]!=b and arr[i+1]!=b:
                        arr[i]=b
                    else:
                        arr[i]=c
        return "".join(arr)
