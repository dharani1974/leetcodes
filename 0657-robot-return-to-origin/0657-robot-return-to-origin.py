class Solution:
    def judgeCircle(self, moves: str) -> bool:
        start=[0,0]
        for ch in moves:
            if ch=='U':
                start[1]+=1
            elif ch=='D':
                start[1]-=1
            elif ch=='L':
                start[0]-=1
            else:
                start[0]+=1
        if start==[0,0]:
            return True
        return False
