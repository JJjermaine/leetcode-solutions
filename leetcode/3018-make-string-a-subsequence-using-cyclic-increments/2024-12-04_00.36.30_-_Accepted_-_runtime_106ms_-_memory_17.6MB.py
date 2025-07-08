class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i = 0
        j = 0
        while i < len(str1) and j < len(str2):
            if str1[i] == str2[j] or (ord(str1[i]) - ord('a') + 1) % 26 == ord(str2[j]) - ord('a'):
                i += 1
                j += 1
            else:
                i += 1
        if j == len(str2):
            return True
        return False
        