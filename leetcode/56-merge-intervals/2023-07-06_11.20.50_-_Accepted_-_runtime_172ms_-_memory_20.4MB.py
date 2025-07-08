class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        curr = 0
        for i in range(0, len(intervals)-1):
            if (intervals[curr][1] >= intervals[curr + 1][0]):
                if (intervals[curr][1] < intervals[curr+1][1]):
                    intervals[curr][1] = intervals[curr+1][1]
                intervals.pop(curr + 1)
            else: 
                curr += 1
            
        return intervals