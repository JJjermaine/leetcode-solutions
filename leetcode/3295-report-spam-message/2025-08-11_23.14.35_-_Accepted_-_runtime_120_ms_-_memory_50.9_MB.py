class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        d = Counter(bannedWords)
        amount = 0
        for m in message:
            if d[m]:
                amount += 1
        
        return True if amount >= 2 else False

        