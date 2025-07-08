class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        # is it the same if we eliminate all X
        # AND if a L and R can reach its destination
        start_new, result_new = [], []
        for i in range(len(start)):
            if start[i] == "L" or start[i] == "R":
                start_new.append([start[i], i])
            if result[i] == "L" or result[i] == "R":
                result_new.append([result[i], i])

        if len(start_new) != len(result_new):
            return False

        for i in range(len(start_new)):
            if start_new[i][0] != result_new[i][0]:
                return False
            
            if start_new[i][0] == "L" == result_new[i][0] and start_new[i][1] < result_new[i][1]:
                return False
            
            if start_new[i][0] == "R" == result_new[i][0] and start_new[i][1] > result_new[i][1]:
                return False
        return True
