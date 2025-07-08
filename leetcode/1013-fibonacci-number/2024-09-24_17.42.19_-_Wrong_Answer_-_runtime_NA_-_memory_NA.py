class Solution:
    def fib(self, n: int) -> int:
        zero, one = 0, 1

        curr = 0
        for i in range(n-1):
            curr = zero + one
            zero, one = one, curr

        return curr
        