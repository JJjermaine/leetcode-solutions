class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        
        # prepend and append the words array to make it circular
        w = words + words + words
        startIndex = len(words) + startIndex
        l = startIndex
        r = startIndex
        curr = 0
        while l > 0 and r < len(w):
            if w[l] == target or w[r] == target:
                return curr
            curr += 1
            l -= 1
            r += 1
        return -1