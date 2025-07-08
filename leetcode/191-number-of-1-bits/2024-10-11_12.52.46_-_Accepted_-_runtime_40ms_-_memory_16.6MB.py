class Solution:
    def hammingWeight(self, n: int) -> int:
        num = bin(n)
        count = 0

        for bit in str(num):
            if bit == "1":
                count += 1

        return count