class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        count = {}
        for i in range(len(list1)):
            for j in range(len(list2)):
                # first time seeing the match
                if list1[i] == list2[j] and list1[i] not in count:
                    count[list1[i]] = i + j

                # other times checking the match, check which index sum is lower
                elif list[i] == list2[j]:
                    curr = count[list[i]]
                    count[list1[i]] = min(curr, i+j)

        # Find the minimum value
        min_value = min(count.values())

        # Get all keys that have the minimum value
        return [key for key, value in count.items() if value == min_value]   


            