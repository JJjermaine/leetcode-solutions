class Solution:
    def stringHash(self, s: str, k: int) -> str:
        n = len(s)
        if n == 1:
            return s
        curr = 0
        res = ""
        for i in range(n):
            curr += ord(s[i]) - 97
            # if on the kth iteration, calculate the char and reset current
            if (i+1) % k == 0 and i > 0:
                string = curr % 26
                res += chr(string + 97) 
                curr = 0
        return res
            


        