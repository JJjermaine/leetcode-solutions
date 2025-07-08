class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        count = {}
        # group by creator and add all their ids and views
        for i in range(len(creators)):
            if creators[i] not in count:
                count[creators[i]] = [ids[i], views[i]]
            else:
                count[creators[i]] += [ids[i], views[i]]

        total_max_views = 0

        for key, value in count.items():
            max_views = 0
            total_views = 0
            # for each creator get max (id, views) pair
            for i in range(0, len(value), 2):
                if value[i+1] > max_views:
                    id_with_max_views, max_views = value[i], value[i+1]
                total_views += value[i+1]

            # replace tuple with singular (id, view) pair
            count[key] = [id_with_max_views, total_views]
            total_max_views = max(total_max_views, total_views)


        res = []
        # add (creator, id) pair if it has highest views
        for key, value in count.items():
            if value[1] == total_max_views:
                res.append([key , value[0]])

        return res

                


        