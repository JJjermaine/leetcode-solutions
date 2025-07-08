class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # build dp table, +1 if same letter
        # traverse back the dp table, if top bigger, take it, if left bigger, take it
        # append any remaining from str1 or str2
        rows, cols = len(str1)+1, len(str2)+1
        dp = [[0] * cols for _ in range(rows)]
        for i in range(1, rows):
            for j in range(1, cols):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = 1 + (dp[i-1][j-1])
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                
        i, j = rows-1, cols-1
        res = []
        while i > 0 and j > 0:
            if str1[i-1] == str2[j-1]: # if both are the same
                res.append(str1[i-1])
                i -= 1
                j -= 1
            elif dp[i-1][j] > dp[i][j-1]: # if top > left, take top in dp table
                res.append(str1[i-1])
                i -= 1
            else: # if left > top, take left in dp table
                res.append(str2[j-1])
                j -= 1
                
        while i > 0:
            res.append(str1[i-1])
            i -= 1
            
        while j > 0:
            res.append(str2[j-1])
            j -= 1
        return "".join(res[::-1])
                
        