class Solution:
    def isValid(self, word: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        if len(word) < 3: # contains min of 3 chars
            return False

        vowel_count = 0
        consonant_count = 0
        for c in word: 
            if not c.isalnum(): # containts alphanumeric
                return False

            if c in vowels: # checks for vowel
                vowel_count += 1
            elif c not in vowels and c.isalpha(): # checks for consonant
                consonant_count += 1
        
        if vowel_count <= 0 or consonant_count <= 0:
            return False

        return True


             

        