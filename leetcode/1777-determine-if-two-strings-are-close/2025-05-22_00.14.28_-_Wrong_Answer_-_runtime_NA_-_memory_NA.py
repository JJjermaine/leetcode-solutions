class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # conditions must hold
        # all letters in word1 must appear in word2
        # each count of unique letters in word1 are 1:1 with word2
        d1 = Counter(word1)

        d2 = Counter(word2)

        for (k1, v1), (k2, v2) in zip(sorted(d1.items(), key=lambda x: -x[1]), sorted(d2.items(), key=lambda x: -x[1])):
            if not d2[k1] or v1 != v2:
                return False
        return True

