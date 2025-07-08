class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def backtrack(path):
            if len(happy_strings) == k:
                return happy_strings[-1]
            if len(path) == n:
                happy_strings.append("".join(path))
                return
            for char in "abc":
                if not path or path[-1] != char:  
                    path.append(char)
                    backtrack(path)
                    path.pop()
        
        happy_strings = []
        backtrack([])
        
        return happy_strings[k - 1] if k <= len(happy_strings) else ""

        