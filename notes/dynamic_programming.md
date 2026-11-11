# Dynamic programming

For coin change, the state for amount a stores the minimum number of coins needed to reach a. When processing a denomination, iterate amounts upward. The state for a minus the denomination can already include that same denomination, which allows reuse. In a 0/1 knapsack, iterate downward to prevent reusing the current item.

For edit distance, the state for two prefix lengths compares the cheapest insertion, deletion, and replacement. The first row and column represent conversions from or to an empty string. Write those boundary values before filling the table.

- [Coin Change](../solutions/coin_change.py)
- [Edit Distance](../solutions/edit_distance.py)
