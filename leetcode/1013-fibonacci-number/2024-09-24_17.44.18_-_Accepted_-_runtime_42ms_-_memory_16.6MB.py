class Solution:
    def fib(self, n: int) -> int:
        if n == 1: return 1 # base cases
        if n == 0: return 0
        
        zero, one = 0, 1

        curr = 0
        for i in range(n-1):
            curr = zero + one
            zero, one = one, curr

        return curr
        