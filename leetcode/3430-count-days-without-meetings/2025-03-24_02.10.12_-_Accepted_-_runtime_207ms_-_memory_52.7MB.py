class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        # If there are no meetings, all days are free.
        if not meetings:
            return days

        # Sort meetings based on the start day.
        meetings.sort()
        
        # Merge overlapping intervals.
        merged = []
        for interval in meetings:
            start, end = interval
            # If there's an overlap with the last interval in merged, merge them.
            if merged and start <= merged[-1][1] + 1:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])
        
        # Calculate total meeting days while ensuring we only count within the range [1, days]
        meeting_days = 0
        for interval in merged:
            # Clamp the interval to the range [1, days]
            start = max(interval[0], 1)
            end = min(interval[1], days)
            # If the clamped interval is valid, add its length.
            if start <= end:
                meeting_days += (end - start + 1)
        
        # The days without meetings are total days minus the days with meetings.
        return days - meeting_days
            