class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sstr=[]
        tstr=[]
        for char in s:
            if char=="#":
                if sstr:
                    sstr.pop()
            else:
                sstr.append(char)
        for char in t:
            if char =="#":
                if tstr:
                    tstr.pop()
            else:
                tstr.append(char)
        if sstr==tstr:
            return True
        return False