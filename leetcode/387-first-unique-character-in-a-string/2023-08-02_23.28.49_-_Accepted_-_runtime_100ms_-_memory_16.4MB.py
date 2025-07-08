class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = {}
        
        for ch in s:
            if dict.get(ch):
                dict[ch] += 1
            else:
                dict[ch] = 1

        index = -1
        for ch in dict:
            if dict[ch] == 1:
                index = s.index(ch)
                break

        return index