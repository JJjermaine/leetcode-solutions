class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        count = 0
        for i in range(len(word)):
            if word[i].isupper():
                count += 1
        if word.isupper() or word.islower() or word[0].isupper() and count == 1:
            return True
        return False
        