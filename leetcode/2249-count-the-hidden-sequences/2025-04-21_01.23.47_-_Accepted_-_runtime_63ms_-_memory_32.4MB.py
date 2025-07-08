class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        n = len(differences)
        hidden = [0] * (n+1)
        curr = 0
        for i in range(1, n+1):
            curr += differences[i-1]
            hidden[i] = curr
        l = lower - min(hidden)
        h = upper - max(hidden)
        if l > h:
            return 0
        return h - l + 1
        