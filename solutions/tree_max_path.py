"""Binary Tree Maximum Path Sum (LeetCode 124). Use one branch for the parent and both branches for the best path through a node."""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.ans = float('-inf')

    def dfs(self, node):
        if not node:
            return 0
        left_max = max(self.dfs(node.left), 0)
        right_max = max(self.dfs(node.right), 0)
        cur_max = left_max + right_max + node.val
        self.ans = max(self.ans, cur_max)
        return max(left_max, right_max) + node.val

    def maxPathSum(self, root: TreeNode | None) -> int:
        self.ans = float('-inf')
        self.dfs(root)
        return self.ans
