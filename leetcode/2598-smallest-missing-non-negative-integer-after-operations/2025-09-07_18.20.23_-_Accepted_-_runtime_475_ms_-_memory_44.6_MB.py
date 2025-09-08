class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        # return maximum MEX 
        # turn all values into lowest forms and put into dictionary
        # example: value = 5... -10 -> 0, if 0 already in dictionary, -10 -> 5
        d = defaultdict(int)
        n = len(nums)
        for i in range(n):
            smallest_it_can_be = nums[i] % value
            d[smallest_it_can_be] += 1

                
        # carry each 
        # example        1: 3, 2: 0 -> 1: 1, 2: 1
        d = sorted(d.items(), reverse = True)
        print(d)
        new = defaultdict(int)
        for key, val in d:
            new[key] += 1    
            curr_key = key + value
            curr_val = val
            
            while curr_val > 1:
                if curr_key in new:
                    curr_key += value
                else:
                    new[curr_key] += 1
                    curr_val -= 1
        print(new)
        curr = 0
        while curr in new:
            curr += 1
        return curr

