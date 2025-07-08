class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # ans my own, used hints

        lst = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                lst.append([nums[i][j], i])

        lst.sort() # sort by nums

        k = len(nums)
        count = {}
        minimum = [lst[0][0], lst[-1][0]]
        left = 0
        
        for i in range(k):
            count[lst[i][1]] = count.get(lst[i][1], 0) + 1

        for i in range(k, len(lst)): # try to get k amount of nums in dic, then use it as smallest range
            

            if len(count) == k:
                if (lst[i-1][0] - lst[left][0]) < (minimum[1] - minimum[0]):
                    minimum = [lst[left][0], lst[i-1][0]]
            
            #slide the window
            count[lst[i][1]] = count.get(lst[i][1], 0) + 1
            count[lst[left][1]] -= 1 
            if count[lst[left][1]] == 0:
                del count[lst[i-k][1]]
                
            left += 1
        
            

        return minimum

        