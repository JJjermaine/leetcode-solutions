class Solution:
    def maxSum(self, nums: List[int]) -> int:
        dic = defaultdict(list)

        # for each int, turn into str where you can iterate and get the max
        for i in range(len(nums)):
            max_dig = 0
            num_str = str(nums[i])

            for j in range(len(num_str)):
                max_dig = max(max_dig, int(num_str[j]))
            
            dic[max_dig].append(nums[i])

        max_num = 0
        for key, values in dic.items():
            if len(values) < 2:
                continue
            sorted_values_sum = sum(sorted(values, reverse = True)[:2]) # get two largest number from each int with same largest num
            max_num = max(max_num, sorted_values_sum)

        if max_num > 0:
            return max_num
        return -1


        

        

        