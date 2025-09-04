class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        n = len(timeSeries)
        if n == 1:
            return duration
        
        res = 0
        for i in range(n-1):
            if timeSeries[i+1] - timeSeries[i] < duration:
                res += timeSeries[i+1] - timeSeries[i]
            else:
                res += duration
        
        res += duration
        return res