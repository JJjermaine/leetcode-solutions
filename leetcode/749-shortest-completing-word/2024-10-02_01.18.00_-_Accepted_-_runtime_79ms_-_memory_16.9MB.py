class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        # Step 1: Build the count of letters in the license plate
        count = {}
        for char in licensePlate:
            if char.isalpha():
                char = char.lower()
                count[char] = count.get(char, 0) + 1

        # Initialize the result variable
        res = None

        # Step 2: Iterate over each word to find the shortest completing word
        for word in words:
            word_count = {}
            for char in word:
                word_count[char] = word_count.get(char, 0) + 1

            # Check if the word contains all required letters with sufficient counts
            is_completing = True
            for char in count:
                if word_count.get(char, 0) < count[char]:
                    is_completing = False
                    break

            # Update the result if this word is a shorter completing word
            if is_completing:
                if res is None or len(word) < len(res):
                    res = word

        return res


        