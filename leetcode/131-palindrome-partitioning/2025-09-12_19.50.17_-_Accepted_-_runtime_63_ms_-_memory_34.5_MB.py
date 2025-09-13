class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res = []
        def backtrack(start, path):
            if start == len(s):
                self.res.append(path[:])
                return

            for i in range(start + 1, len(s) + 1):
                if s[start:i] == s[start:i][::-1]:
                    backtrack(i, path + [s[start:i]])



        backtrack(0, [])
        return self.res