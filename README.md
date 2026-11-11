# Algorithm Patterns in Python

A curated set of practice solutions and notes on the decisions behind them. The Python modules run without the LeetCode environment and use only the standard library. The problem titles link to LeetCode.

Run the examples and regression checks with Python 3.10 or later:

```sh
python -m unittest -v
```

## Solutions

| Problem | Implementation | Approach | Complexity |
|---|---|---|---|
| [15. Three Sum](https://leetcode.com/problems/3sum/) | [Python](solutions/three_sum.py) | Sort and move two pointers, skipping duplicate values. | O(n²) time |
| [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | [Python](solutions/rotated_search.py) | Identify the sorted half before shrinking the search range. | O(log n) time, O(1) space |
| [380. Randomized Set](https://leetcode.com/problems/insert-delete-getrandom-o1/) | [Python](solutions/randomized_set.py) | Swap the removed item with the final item and repair its index. | Expected amortized O(1) per operation |
| [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) | [Python](solutions/subarray_sum.py) | Count earlier prefix sums before inserting the current prefix. | O(n) expected time, O(n) space |
| [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | [Python](solutions/trapping_rain_water.py) | Compare a monotonic stack with a two-pointer scan. | Both O(n) time, O(n) versus O(1) space |
| [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | [Python](solutions/sliding_window_maximum.py) | Compare lazy heap eviction with a monotonic deque. | Heap O(n log n) time, O(n) space in the worst case. Deque O(n) time, O(k) space. |
| [124. Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | [Python](solutions/tree_max_path.py) | Use one branch for the parent and both branches for the best path through a node. | O(n) time, O(h) stack |
| [207. Course Schedule](https://leetcode.com/problems/course-schedule/) | [Python](solutions/course_schedule.py) | Remove zero-indegree nodes and count how many were processed. | O(V + E) time and space |
| [994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) | [Python](solutions/rotting_oranges.py) | Start BFS from all sources and track time in layers. | O(rows × cols) time and space |
| [51. N-Queens](https://leetcode.com/problems/n-queens/) | [Python](solutions/n_queens.py) | Place one queen per row and undo invalid branches. | Exponential search plus output construction |
| [322. Coin Change](https://leetcode.com/problems/coin-change/) | [Python](solutions/coin_change.py) | Scan amounts forward to permit reuse of each denomination. | O(coins × amount) time, O(amount) space |
| [72. Edit Distance](https://leetcode.com/problems/edit-distance/) | [Python](solutions/edit_distance.py) | Model operations on prefixes and initialize empty-prefix costs. | O(mn) time and space |

## Notes

- [Graph traversal](notes/graphs.md)
- [Binary tree recursion](notes/trees.md)
- [Dynamic programming](notes/dynamic_programming.md)

Solutions assume the problem constraints. Three Sum sorts its input in place, and Rotting Oranges marks visited cells in place.
