# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        visited_nodes = 0
        result = None

        def dfs(root):
            nonlocal visited_nodes
            nonlocal result
            if not root:
                return

            if result is not None:
                return

            dfs(root.left)
            visited_nodes += 1
            if visited_nodes == k:
                result = root.val
                return
            dfs(root.right)

            return
        
        dfs(root)

        return result

                




        