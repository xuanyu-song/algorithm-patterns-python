# Graph traversal

In Kahn's algorithm, a node's remaining indegree counts the prerequisites that have yet to be processed. Every node removed from the ready queue unlocks its outgoing neighbors. If the ready queue empties before all nodes have been processed, the remaining graph contains a cycle. Compare with DFS cycle detection, where an edge back to a node on the active recursion path identifies a cycle.

For multi-source BFS, add every source to the queue at the start. All nodes reached in the same layer have the same distance from their nearest source.

- [Course Schedule](../solutions/course_schedule.py)
- [Rotting Oranges](../solutions/rotting_oranges.py)
