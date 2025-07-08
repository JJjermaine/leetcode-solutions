class Solution:
    def longestWord(self, words: List[str]) -> str:
        # for each one letter word, see if it can build something larger
        words.sort()
        s = set()
        n = len(words)
        largest = ""
        for i in range(n):
            # if same length, add it to set and check the next one after it
            # or if start of a word, add to set
            if words[i][:-1] in s or len(words[i]) == 1:

                s.add(words[i])
                # if lexilogically smaller, keep the old one
                if len(words[i]) == len(largest):
                    largest = min(largest, words[i])
                else:
                    largest = max(largest, words[i])


        return largest


        