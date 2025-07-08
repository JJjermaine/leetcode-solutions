class Solution:
    def similarPairs(self, words: List[str]) -> int:
        sets = [set() for i in range(len(words))]

        # create a set for each word in words
        for i in range(len(words)):
            for j in range(len(words[i])):
                sets[i].add(words[i][j])

        # compare each set to see if theyre unique
        count = 0
        for i in range(len(sets)):
            for j in range(i + 1, len(sets)):
                if sets[i] == sets[j]:
                    count += 1

        return count


        


        