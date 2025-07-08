class Solution:
    def countVowels(self, word: str) -> int:
        s = set('aeiou')
        n = len(word)
        
        dp = [0] * n
        curr = 0
        
        for i in range(n):
            if word[i] in s:
                curr += (i + 1)
            dp[i] = (dp[i-1]) + curr
        
        return dp[-1]
            
        