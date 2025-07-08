class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = {}
        
        for ch in s:
            if dict.get(ch):
                dict[ch] += 1
            else:
                dict[ch] = 1

        index = 0
        for ch in dict:
            if dict[ch] == 1:
                return index
            index += dict[ch]
        return -1