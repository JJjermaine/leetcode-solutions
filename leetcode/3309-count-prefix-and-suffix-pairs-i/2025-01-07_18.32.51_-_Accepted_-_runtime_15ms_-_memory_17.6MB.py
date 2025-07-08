class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:

        def isPrefixAndSuffix(str1, str2):
            if len(str1) > len(str2):
                return False
            
            prefix = str2[:len(str1)] == str1

            suffix = str2[-len(str1):] == str1

            return prefix and suffix
            
        count = 0

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if isPrefixAndSuffix(words[i], words[j]):
                    count += 1

        return count 

        