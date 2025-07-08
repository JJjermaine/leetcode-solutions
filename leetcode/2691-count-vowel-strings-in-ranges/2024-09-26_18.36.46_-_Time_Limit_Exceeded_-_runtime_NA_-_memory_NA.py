class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set('aeiou')
        satisfied_indices = set()
        # indices where it starts and end in vowels
        for i in range(len(words)):
            if words[i][0] in vowels and words[i][-1] in vowels:
                satisfied_indices.add(i)

        res = []
        for query in queries:
            curr = 0
            for j in range(query[0], query[1]+1): # if from query x to y contains z amount of satisfied conditions, add to res
                if j in satisfied_indices:
                    curr += 1 

            res.append(curr)

        return res

        