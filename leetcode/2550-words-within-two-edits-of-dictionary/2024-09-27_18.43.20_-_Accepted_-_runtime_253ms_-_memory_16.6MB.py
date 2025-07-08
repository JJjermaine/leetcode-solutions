class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        res = []
        for i in range(len(queries)):
            for j in range(len(dictionary)):
                non_matching_letters = 0
                pointer = 0
                while pointer < len(queries[i]):
                    if queries[i][pointer] != dictionary[j][pointer]:
                        non_matching_letters += 1
                    pointer += 1
                
                
                if non_matching_letters <= 2:
                    res.append(queries[i])
                    break # break out of loop because one solution found

        return res

        