class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rCount = {}

        mCount = {}

        for c in ransomNote:
            rCount[c] = rCount.get(c, 0) + 1
        for c in magazine:
            mCount[c] = mCount.get(c, 0) + 1

        for key, value in rCount.items():
            if mCount.get(key, 0) < value:
                return False

        return True

        