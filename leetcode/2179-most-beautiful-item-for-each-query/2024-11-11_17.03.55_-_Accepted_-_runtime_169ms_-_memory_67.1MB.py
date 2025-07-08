class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        # Sort items by price and maintain maximum beauty as we progress
        items.sort()
        
        # Pair queries with their indices, then sort by query price
        queries_with_indices = sorted((q, i) for i, q in enumerate(queries))
        result = [0] * len(queries)
        
        # Track maximum beauty encountered so far
        max_beauty = 0
        item_idx = 0
        
        for query_price, original_index in queries_with_indices:
            # Move item index up to the maximum items affordable by query_price
            while item_idx < len(items) and items[item_idx][0] <= query_price:
                max_beauty = max(max_beauty, items[item_idx][1])
                item_idx += 1
                
            # Store the max beauty found for this query
            result[original_index] = max_beauty
        
        return result

        