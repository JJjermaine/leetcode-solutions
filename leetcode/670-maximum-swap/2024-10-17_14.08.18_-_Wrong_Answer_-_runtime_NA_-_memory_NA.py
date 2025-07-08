class Solution:
    def maximumSwap(self, num: int) -> int:
        # base case, return the num if we cant swap
        if num < 10:
            return num

        # greedily put the largest number 
        # on the right the leftmost number if its at least greater
        str_num = str(num)
        
        index_to_iterate_to = 0
        for i in range(len(str_num)):
            if str_num[i] != str_num[0]:
                index_to_iterate_to = i
                break

        max_num = [0]
        for i in range(len(str_num)-1, int(index_to_iterate_to)-1, -1):
            
            if int(str_num[i]) > max_num[0]:
                max_num = ((int(str_num[i]), i)) # value, index

        first = []
        for i in range(len(str_num)):
            if max_num[0] > int(str_num[i]):
                first = [int(str_num[i]), i] # value index
                break

        if not first or max_num[1] < first[1]:
            return num # no swaps are necessary if index for max_num on right < index for first smaller number encountered

            

        # swap the value and index from the max_num and first number that is smaller than it
        # Convert the string to a list
        s_list = list(str_num)
        # Swap the elements at index1 and index2
        s_list[max_num[1]], s_list[first[1]] = s_list[first[1]], s_list[max_num[1]]
        # Convert the list back to a string and return
        return int(''.join(s_list))
                

                


        