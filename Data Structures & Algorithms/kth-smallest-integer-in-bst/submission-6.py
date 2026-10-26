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
        visited_nodes = 0

        def dfs(root):
            nonlocal visited_nodes
            if not root:
                visited_nodes -= 1
                return
        
            dfs(root.left)
            visited_nodes += 1
            if visited_nodes < k:
                ordered_list.append(root.val)
            dfs(root.right)
            visited_nodes += 1

            return
        
        dfs(root)

        print(ordered_list)
        return ordered_list[k-1]

                




        