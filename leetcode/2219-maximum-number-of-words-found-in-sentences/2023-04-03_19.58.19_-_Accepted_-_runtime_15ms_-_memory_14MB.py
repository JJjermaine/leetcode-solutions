class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        # ORIGINAL CODE
        #count = 0
        #max = 0
        #for i in range(len(sentences)):
        #    if ' ' in sentences[i]:
        #        for j in sentences[i]:
        #            if j == ' ':
        #                count += 1
        #        if max < count:
        #            max = count
        #        count = 0
        #return max + 1

        # optimized code in solutions tab
        return max(s.count(" ") for s in sentences) + 1
        