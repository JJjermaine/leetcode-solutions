class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        def encrypt(x):
            x = str(x)
            largest = float("-inf")
            for i in range(len(x)):
                largest = max(largest, int(x[i]))
            return int(str(largest) * len(x))
        res = 0
        for num in nums:
            res += encrypt(num)
        return res

        