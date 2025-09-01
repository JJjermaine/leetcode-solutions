class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        sorted_freq = sorted(freq.items(), key = lambda item: item[1], reverse=True)
        res = ""
        print(sorted_freq)
        for char, amount in sorted_freq:
            res += char * amount

        return res