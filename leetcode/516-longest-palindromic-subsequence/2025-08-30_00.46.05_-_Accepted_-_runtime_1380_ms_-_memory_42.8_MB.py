class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # its just longest common subsequence between s and the reverse of s
        n = len(s)
        reverse = s[::-1]

        dp = [[0] * (n+1) for _ in range(n+1)]

        for i in range(n):
            for j in range(n):
                if s[i] == reverse[j]:
                    dp[i+1][j+1] = 1 + dp[i][j]
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        return dp[-1][-1]