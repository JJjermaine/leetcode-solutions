class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for word in words:
            if pref == word[0:len(pref)]:
                count += 1
        return count
        