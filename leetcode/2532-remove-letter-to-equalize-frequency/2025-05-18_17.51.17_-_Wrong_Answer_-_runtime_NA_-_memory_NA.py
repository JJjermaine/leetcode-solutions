class Solution:
    def equalFrequency(self, word: str) -> bool:
        d = Counter(word)
        d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        freq = 1 if next(iter(d.values())) - 1 < 1 else next(iter(d.values())) - 1
        first = False
        for k, v in d.items():
            # skip first one
            if not first:
                first = True
                continue
            if v != freq:
                return False
        
        return True