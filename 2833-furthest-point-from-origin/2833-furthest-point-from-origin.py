class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l=0
        r=0
        _=0
        for ch in moves:
            if ch=='L':
                l+=1
            elif ch=='R':
                r+=1
            else:
                _+=1
        
        if r>l:
            return r-l+_
            
        else:
            return l-r+_
        



