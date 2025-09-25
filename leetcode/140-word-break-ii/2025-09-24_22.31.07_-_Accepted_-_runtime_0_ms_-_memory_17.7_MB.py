class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # For efficient lookup, convert wordDict to a set
        word_set = set(wordDict)

        # dp[i] will store a list of all possible valid sentences for s[0:i]
        dp = [[] for _ in range(len(s) + 1)]

        # Base case: An empty string has one "segmentation" - an empty string.
        # This allows us to start building sentences.
        dp[0] = [""] 

        # Iterate through all possible end points 'i' of a prefix
        for i in range(1, len(s) + 1):
            # Iterate through all possible split points 'j'
            # s[0:j] is the first part, s[j:i] is the second part
            for j in range(i):
                # If s[0:j] can be segmented (i.e., dp[j] is not empty)
                # AND the substring s[j:i] is a valid word
                if dp[j] and s[j:i] in word_set:
                    current_word = s[j:i]
                    # For each sentence already formed for s[0:j]
                    for prev_sentence in dp[j]:
                        # Combine it with the current_word
                        if prev_sentence == "":
                            # If it's the first word, no leading space
                            dp[i].append(current_word)
                        else:
                            # Otherwise, add a space before the current_word
                            dp[i].append(prev_sentence + " " + current_word)
        
        return dp[len(s)]