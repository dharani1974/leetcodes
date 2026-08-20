class Solution:
    def removeDuplicates(self, s: str) -> str:
        res=[]
        for char in s:
            if not res:
                res.append(char)
            elif (res[-1]==char):
                res.pop()
            else:
                res.append(char)
        return "".join(res)