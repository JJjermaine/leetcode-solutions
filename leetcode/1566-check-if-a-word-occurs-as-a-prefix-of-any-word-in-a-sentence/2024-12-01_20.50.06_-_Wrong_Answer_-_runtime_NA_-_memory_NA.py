class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        split = sentence.split()
        for i in range(len(split)):
            if len(searchWord) > len(split[i]):
                continue
            p = 0
            while p < len(searchWord):
                if p == len(searchWord) - 1:
                    return i + 1
                if split[i][p] != searchWord[p]:
                    break
                p += 1
        return -1


        