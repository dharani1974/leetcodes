class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        count=duration
        i=len(timeSeries)-1
        while i>0:
            if timeSeries[i]-timeSeries[i-1]<duration:
                count+=timeSeries[i]-timeSeries[i-1]
                i-=1
            else:
                count+=duration
                i-=1
        return count