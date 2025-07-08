class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"

        len_prev = (2 **  (n-1)) - 1

        if k <= len_prev:
            return self.findKthBit(n-1, k)
        elif k == len_prev + 1:
            return "1"
        else:
            pos = len_prev - (k - (len_prev + 1)) + 1
            return "0" if self.findKthBit(n-1, pos) == "1" else "1"