class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        item_idx = 0
        res = []
        for i in range(len(queries)):
            most_beautiful = 0
            while queries[i] >= items[item_idx][0]:
                most_beautiful = items[item_idx][1]
                if item_idx == len(items)-1:
                    break
                item_idx += 1
            while queries[i] < items[item_idx][0]:
                item_idx -= 1
                if item_idx < 0:
                    break
            res.append(most_beautiful)

        #if len(res) == 0:
        #    return [0]
        return res

        