class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # keep track of the 2 largest and 2 smallest seen
        # pick from the largest difference as long as theyre not from the same array
        smallest = [float("inf"), None]
        sec_smallest = [float("inf"), None]
        largest = [float("-inf"), None]
        sec_largest = [float("inf"), None]

        for i in range(len(arrays)):
            if arrays[i][0] < smallest[0]:
                if smallest[0] != float("inf"):
                    sec_smallest = smallest.copy()
                smallest = [arrays[i][0], i]
            elif arrays[i][0] < sec_smallest[0]:
                sec_smallest = [arrays[i][0], i]
            
                
            if arrays[i][-1] > largest[0]:
                if largest[0] != float("inf"):
                    sec_largest = largest.copy()
                largest = [arrays[i][-1], i]
            elif arrays[i][-1] > sec_largest[0]:
                sec_largest = [arrays[i][-1], i]
            
            if smallest == largest:
                smallest = [arrays[i][0], i]

        if largest[1] != smallest[1]: # regular case of the smallest and largest not being in the same array
            return abs(smallest[0] - largest[0])
        
        # if in case of them being in the same array
        max_diff = 0
        if sec_smallest[1] != largest[1]:
            max_diff = max(max_diff, abs(sec_smallest[0] - largest[0]))

        if sec_smallest[1] != sec_largest[1]:
            max_diff = max(max_diff, abs(sec_smallest[0] - sec_largest[0]))
        
        if sec_largest[1] != smallest[1]:
            max_diff = max(max_diff, abs(sec_largest[0] - smallest[0]))
        
        return max_diff
        