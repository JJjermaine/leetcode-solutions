class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        count = 0
        for c in word:
            if c == c.upper():
                count += 1

        if word[0] == word[0].upper() and count > 0 and count - len(word) != 0:
            return False 
        return True

        