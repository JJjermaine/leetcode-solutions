class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        # compare first x amount of words and if no match, continue from back to compare x amount of words

        s1 = sentence1.split()
        s2 = sentence2.split()

        if len(s1) < len(s2): # only flip bigger sentence's bits as the sentence cannot be reduced to smaller sentence
            s1, s2 = s2, s1

        start, end = 0, 0
        # compare from start
        while start < len(s2) and s1[start] == s2[start]:
            start += 1

        while end < len(s2) and s1[len(s1) - end - 1] == s2[len(s2) - end - 1]:
            end += 1

        return start + end >= len(s2) 


       


        