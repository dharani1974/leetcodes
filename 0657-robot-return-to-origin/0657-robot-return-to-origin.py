class Solution:
    def judgeCircle(self, moves: str) -> bool:
        a=0
        v=0
        for char in moves:
            if char=="U":
                v+=1
            elif char=="D":
                v-=1
            elif char=="R":
                a+=1
            else:
                a-=1
        return a==0 and v==0