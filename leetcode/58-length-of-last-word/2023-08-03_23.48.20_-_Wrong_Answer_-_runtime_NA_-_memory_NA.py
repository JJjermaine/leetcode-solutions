class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for i in range(len(s)-1, 0, -1):
            if s[i] == ' ' and count > 0:
                break
            if s[i] != ' ':
                count += 1
        return count
