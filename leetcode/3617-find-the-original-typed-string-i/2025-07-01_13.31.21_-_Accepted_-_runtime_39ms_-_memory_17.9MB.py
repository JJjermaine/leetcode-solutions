class Solution:
    def possibleStringCount(self, word: str) -> int:
        res = 0
        for i in range(len(word)-2,-1,-1):
            if word[i] == word[i+1]:
                res += 1
        return res + 1