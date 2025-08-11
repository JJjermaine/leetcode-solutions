class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # needed help from gpt
        MOD = 10**9 + 7
        
        # Step 1: Get powers from binary representation of n
        powers = []
        bit = 0
        while n > 0:
            if n & 1:
                powers.append(1 << bit)
            n >>= 1
            bit += 1
        
        # Step 2: Compute prefix products
        prefix = [1] * (len(powers) + 1)
        for i in range(len(powers)):
            prefix[i+1] = (prefix[i] * powers[i]) % MOD
        
        # Step 3: Answer queries
        res = []
        for left, right in queries:
            prod = (prefix[right+1] * pow(prefix[left], MOD-2, MOD)) % MOD
            res.append(prod)
        
        return res