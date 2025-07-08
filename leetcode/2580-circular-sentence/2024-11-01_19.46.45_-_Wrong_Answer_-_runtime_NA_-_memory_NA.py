class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        for i in range(1, len(words)):
            if words[i-1][-1].lower() != words[i][0].lower():
                return False

        if words[-1][-1].lower() != words[0][0].lower():
            return False

        return True