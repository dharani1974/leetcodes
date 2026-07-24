class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l=0
        r=0
        _=0
        for char in moves:
            if char=="L":
                l+=1
            elif char=="R":
                r+=1
            else:
                _+=1
        return (abs(l-r))+_