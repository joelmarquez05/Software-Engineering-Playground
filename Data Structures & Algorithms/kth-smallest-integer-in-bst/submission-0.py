# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ordered_list = []

        def dfs(root):
            if not root:
                return

            dfs(root.left)
            ordered_list.append(root.val)
            dfs(root.right)

            return
        
        dfs(root)

        return ordered_list[k-1]

                




        