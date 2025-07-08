class Solution:
    def isValid(self, word: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        if len(word) <= 3: # contains min of 3 chars
            return False

        for c in word:
            if not c.isalnum():
                return False

        vowel_count = 0
        consonant_count = 0
        for vowel in vowels:
            if vowel in word:
                vowel_count += 1
            elif vowel not in word and vowel.isalpha():
                consonant_count += 1
        
        if vowel_count <= 0 and consonant_count <= 0:
            return False

        return True


             

        