class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i','o', 'u', 'A', 'E', 'I', 'O', 'U']
        sort = []
        for letter in s:
            if letter in vowels:
                sort.append(letter)

        sort.sort()
        
        res = []
        sort_p = 0
        for i in range(len(s)):
            if s[i] in vowels:
                res.append(sort[sort_p])
                sort_p += 1
            else:
                res.append(s[i])

        return ''.join(res)

        