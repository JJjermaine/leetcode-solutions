class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        min_length = min(len(s1), len(s2), len(s3))
        L = 0  # Length of the common prefix

        # Find the length of the common prefix
        while L < min_length and s1[L] == s2[L] == s3[L]:
            L += 1

        # If the common prefix length is zero, it's impossible to make the strings equal
        if L == 0:
            return -1

        # Calculate the total deletions required
        total_deletions = (len(s1) - L) + (len(s2) - L) + (len(s3) - L)
        return total_deletions

        