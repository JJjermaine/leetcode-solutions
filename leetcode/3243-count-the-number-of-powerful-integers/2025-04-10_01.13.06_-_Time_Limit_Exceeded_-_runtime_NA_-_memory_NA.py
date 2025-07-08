class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        # all digits must be <= limit
        # generate all numbers that end with s

        from functools import lru_cache

        suffix = int(s)
        suffix_len = len(s)
        base = 10 ** suffix_len

        # Calculate valid range of multipliers such that multiplier * base + suffix is in [start, finish]
        low = (start - suffix + base - 1) // base  # ceil((start - suffix) / base)
        high = (finish - suffix) // base          # floor((finish - suffix) / base)

        result = 0

        @lru_cache(maxsize=None)
        def all_digits_ok(n: int) -> bool:
            return all(int(c) <= limit for c in str(n))

        for multiplier in range(low, high + 1):
            num = multiplier * base + suffix
            if all_digits_ok(num):
                result += 1

        return result



        