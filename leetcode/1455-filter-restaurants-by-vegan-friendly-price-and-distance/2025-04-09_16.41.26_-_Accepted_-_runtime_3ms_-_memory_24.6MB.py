class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        afterSort = []
        for id, rating, vegan, price, distance in restaurants:
            # ignore if not within bounds
            if price > maxPrice or distance > maxDistance:
                continue
            # else if not veganfriendly, include all
            elif not veganFriendly:
                afterSort.append([rating, id])
            # else veganfriendly, include only veganfriendly
            else:
                if vegan == veganFriendly:
                    afterSort.append([rating, id])
                    
        afterSort.sort(reverse=True)
        return [afterSort[i][1] for i in range(len(afterSort))]


        