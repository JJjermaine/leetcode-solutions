class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        curr = 0
        for i in range(len(intervals)-1):
            if intervals[curr][1] >= intervals[curr+1][0]:
                if intervals[curr][1] < intervals[curr+1][1]:
                    intervals[curr][1] = intervals[curr+1][1] 
                intervals.pop(curr+1)
            else:
                curr += 1
        return intervals
        