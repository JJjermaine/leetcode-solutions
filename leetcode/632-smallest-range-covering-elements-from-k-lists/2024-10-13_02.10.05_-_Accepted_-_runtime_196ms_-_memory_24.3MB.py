class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # used hints and chatgpt

        lst = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                lst.append([nums[i][j], i])

        lst.sort() # sort by nums

        k = len(nums)
        count = defaultdict(int)
        minimum = [lst[0][0], lst[-1][0]]
        left = 0
        inside_window = 0
        
        for right in range(len(lst)): # try to get k amount of nums in dic, then use it as smallest range
            num, index = lst[right]
            count[index] += 1

            if count[index] == 1:
                inside_window += 1

            while inside_window == k:
                if (lst[right][0] - lst[left][0]) < (minimum[1] - minimum[0]):
                    minimum = [lst[left][0], lst[right][0]]
            
                # slide the window
                count[lst[left][1]] -= 1 
                if count[lst[left][1]] == 0:
                    inside_window -= 1
                    
                left += 1
   

        return minimum
