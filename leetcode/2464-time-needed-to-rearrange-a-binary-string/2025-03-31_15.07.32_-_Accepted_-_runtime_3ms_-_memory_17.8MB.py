class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        zeros = 0
        seconds = 0
        for c in s:
            if c == "0":
                zeros += 1
            if c == "1" and zeros:
                seconds = max(seconds + 1, zeros)
        return seconds
        