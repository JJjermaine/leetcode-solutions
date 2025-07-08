class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # instead of shifting each time, merge the shifts, then start shifting
        n = len(s)
        merge = [0] * (n+1)
        for start, end, direction in shifts:
            if direction == 1:
                merge[start] += 1
                merge[end+1] -=1
            else:
                merge[start] -= 1
                merge[end+1] += 1
 
        curr = 0
        res = ""
        for i in range(n):
            curr += merge[i]
            new_ord = (ord(s[i]) - 97 + curr) % 26 + 97
            res += chr(new_ord)
        return res





