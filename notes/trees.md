# Binary tree recursion

Decide what the recursive call returns before deciding what the overall algorithm records. In maximum path sum, a subtree can offer its parent only a downward chain. A path that ends within that subtree can include both children, so the running maximum considers a different expression from the return value. Ignoring negative child contributions is useful, but initializing the overall maximum to zero would lose the correct answer for an all-negative tree.

- [Binary Tree Maximum Path Sum](../solutions/tree_max_path.py)
