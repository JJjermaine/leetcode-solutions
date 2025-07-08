class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        arr = [0] * (days+1)
        for start, end in meetings:
            for i in range(start, end+1):
                arr[i] += 1

        res = 0
        for num in arr:
            if num == 0:
                res += 1
        return res - 1
            