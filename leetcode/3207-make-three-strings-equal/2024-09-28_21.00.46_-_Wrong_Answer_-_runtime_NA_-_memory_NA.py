class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        smallest_len = min(len(s1), len(s2), len(s3))

        if len(s1) == len(s2) == len(s3):
            for i in range(len(s1)-1):
                if s1[i] != s2[i] or s1[i] != s3[i] or s2[i] != s3[i]:
                    # base case, all characters up until the last one of the smallest string need to match
                    return -1
            return 3
        else:
            for i in range(smallest_len):
                if s1[i] != s2[i] or s1[i] != s3[i] or s2[i] != s3[i]:
                    # base case, all characters up until the last one of the smallest string need to match
                    return -1

        

        count = 0
        count += len(s1) - smallest_len  # Operations to shorten s1
        count += len(s2) - smallest_len  # Operations to shorten s2
        count += len(s3) - smallest_len  # Operations to shorten s3

        return count

        