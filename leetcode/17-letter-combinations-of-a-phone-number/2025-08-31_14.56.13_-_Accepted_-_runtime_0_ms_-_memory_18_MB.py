class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {'2': "abc",'3': "def",'4': "ghi", '5': "jkl",'6': "mno",'7': "pqrs",'8': "tuv",'9': "wxyz"}
        if digits == "":
            return []
        res = []

        def backtrack(path, remaining):
            if len(remaining) == 0:
                res.append(path)
            else:
                for letter in d[remaining[0]]:
                    backtrack(path + letter, remaining[1:])
        backtrack("", digits)
        
        return res
