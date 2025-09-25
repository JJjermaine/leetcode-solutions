class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # intuition: if s = "catsand", wordDict = ["cats", "cat", "and", "sand"]
        # we traverse both cats and cat through tries? 
        # c -> a -> t -> s
        # -> a -> n -> d
        # -> s -> a -> n ->d
        # looked at neetcode

        word_set = set(wordDict)

        # dp[i] will be True if s[0:i] can be segmented into words
        dp = [False] * (len(s) + 1)
        dp[0] = True # Base case: empty string (s[0:0]) can always be segmented

        # Iterate through all possible end points 'i' of a prefix
        for i in range(1, len(s) + 1):
            # Iterate through all possible split points 'j'
            # s[0:j] is the first part, s[j:i] is the second part
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break # If s[0:i] can be segmented, no need to check further split points
        
        return dp[len(s)]